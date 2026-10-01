# External Trigger for Timestamps
Date (UTC): 2026-06-23 17:58
Conversation ID: 6a3ac902-4794-83eb-946d-71e3fcf93276
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-008.json

[M1] ME (2026-06-23 17:58):
When working with labview and pxi hardware how can an external trigger into a controller module help with sub second time stamping where the system usually is unable to do this 

[M2] AI (2026-06-23 17:58):
Yes — an external trigger into a PXI/PXIe controller or timing-capable module can help because it gives the system a **hardware-defined time reference** instead of relying on when Windows/LabVIEW happens to notice something in software.

The key distinction is:

**Software timestamping:**  
LabVIEW code running on the controller sees an event, then calls something like `Get Date/Time in Seconds`. That timestamp depends on Windows scheduling, driver latency, loop timing, PCI/PXI bus latency, and whatever else the controller is doing. So you may only trust it to tens of milliseconds, sometimes worse.

**Hardware-assisted timestamping:**  
An external trigger arrives on a PXI trigger line, timing module, counter/timer, digital input, DAQ card, FPGA card, or sync module. The hardware latches a timestamp or counter value at the instant the edge arrives. LabVIEW reads that value later, but the timestamp was captured at the event time, not when software got around to it.

So the external trigger helps by separating:

> **when the event happened**  
> from  
> **when LabVIEW processed the event**

That is the important bit.

For example, suppose you have a sensor event at 12:00:00.123456.

Without hardware trigger capture, LabVIEW might only read it at:

`12:00:00.170`

because the loop was delayed. You would think the event happened 46 ms later than it really did.

With external trigger capture, the PXI hardware can latch the edge at something like:

`counter value = 123456 ticks`

or

`12:00:00.123456`

Then LabVIEW can read that value 50 ms later and still know the real event time.

In PXI systems this is especially useful because PXI has dedicated timing and trigger infrastructure: backplane trigger lines, star triggers, reference clocks, and timing slots depending on chassis/module type. That means multiple instruments can be aligned to the same trigger or clock rather than each module relying on its own software timing.

A typical architecture would be:

```text
External event / pulse
        │
        ▼
PXI trigger input / DAQ / timing module / counter
        │
        ├── Hardware latches timestamp or counter value
        │
        ├── Trigger routed across PXI backplane
        │
        └── Other PXI modules start acquisition at same event

LabVIEW reads result later
```

This can give sub-second, millisecond, microsecond, or even better timing depending on the hardware. The controller itself is usually not what gives you the precision; the precision comes from the **PXI timing hardware, counter clock, FPGA, DAQ sample clock, or sync module**.

The controller module input can help in several ways:

1. **Event alignment**  
   The external trigger marks a real-world event, such as “test started”, “beam fired”, “motor reached position”, “supply enabled”, or “fault occurred”.

2. **Start-of-acquisition synchronisation**  
   Multiple PXI cards can begin sampling at the same hardware edge. Their data arrays then share a common time zero.

3. **Counter-based timestamping**  
   A counter running from a stable reference clock can latch its count on the trigger edge. That gives much finer timing than a LabVIEW loop.

4. **Removing Windows jitter**  
   Even if LabVIEW is delayed, the event time has already been captured by hardware.

5. **Correlating separate systems**  
   If the same external pulse goes to several systems, each one can mark the same event and later align logs/data.

The limitation is that just wiring a trigger into a controller does not magically make normal LabVIEW timestamps precise. It only helps if the input is connected to hardware that can **capture, latch, route, or synchronise** the event. If LabVIEW is merely polling a digital input and timestamping it in software, you still have software jitter.

A good way to think of it:

```text
Bad:
External trigger → LabVIEW loop notices input → software timestamp

Good:
External trigger → hardware captures edge time → LabVIEW reads captured timestamp
```

For your case, the sensible question is: **which PXI module receives the trigger, and can it latch the event against a hardware clock?** If it is just a controller GPIO line read by software, improvement may be limited. If it is a DAQ/counter/timing/FPGA module, it can genuinely solve the sub-second timestamping problem.

[M3] ME (2026-06-23 18:04):
In an FPGA system is it best for that to produce the master clock. How could a single external trigger sync the run state of a test mode whilst at the same time serving as a fault flag during fault modes.

[M4] AI (2026-06-23 18:05):
In an FPGA-based PXI/LabVIEW system, I would **not automatically make the FPGA “the master clock”**. I would make the FPGA the **master timing/state authority**, but ideally discipline it from a stable system reference clock.

A good split is:

```text
Reference clock source     = stable oscillator / PXI backplane / timing module
FPGA                       = deterministic sequencer, timestamp engine, state machine
External trigger input     = event marker / sync edge / fault indication depending on mode
LabVIEW / controller       = supervisory control, logging, UI, non-deterministic layer
```

So the FPGA does not necessarily “produce” the best master clock. It often **consumes a good master clock** and then produces deterministic enables, timestamps, strobes, trigger outputs and state transitions from that clock.

## Should the FPGA produce the master clock?

Usually:

**Best case:**  
Use a proper low-jitter reference clock from a PXI timing module, chassis reference, OCXO, GPS-disciplined clock, IRIG/PTP timing source, or dedicated oscillator, then feed that into the FPGA.

**FPGA role:**  
The FPGA uses that reference to maintain a counter/timestamp and controls the test state machine.

For example:

```text
10 MHz PXI reference / timing module
        │
        ▼
FPGA clock domain
        │
        ├── timestamp counter
        ├── test state machine
        ├── trigger edge capture
        ├── fault latch
        └── deterministic outputs
```

The FPGA is excellent for **deterministic timing**, but it is not automatically the best **absolute timebase** unless its oscillator/reference is good enough. The accuracy and drift come from the clock source; the deterministic behaviour comes from the FPGA logic.

## Single external trigger doing two jobs

Yes, a single external trigger line can sync the **run state** in test mode and act as a **fault flag** in fault mode, but only if the FPGA interprets it according to the current system state.

That means the line itself is just an input event. The FPGA state machine decides what that event means.

Something like this:

```text
External trigger edge
        │
        ▼
FPGA input synchroniser
        │
        ▼
Edge detect
        │
        ▼
Mode-dependent interpretation
        │
        ├── If mode = IDLE / ARMED:
        │       trigger means START TEST / SYNC RUN STATE
        │
        └── If mode = RUNNING / FAULT_MONITOR:
                trigger means FAULT EVENT / LATCH FAULT
```

So the same physical signal can be overloaded, but it must be **state-qualified**.

## Example state-machine behaviour

A robust design might look like this:

```text
IDLE
  │
  │ arm command from LabVIEW/controller
  ▼
ARMED
  │
  │ external trigger rising edge
  ▼
RUNNING
  │
  │ external trigger rising edge during run
  ▼
FAULT_LATCHED
  │
  │ reset/clear command
  ▼
IDLE
```

In words:

- In **IDLE**, the trigger is ignored.
- In **ARMED**, the trigger starts the test and captures `t0`.
- In **RUNNING**, the same trigger input is treated as a fault indication.
- In **FAULT_LATCHED**, the trigger is ignored until the controller explicitly clears the fault.

This lets one wire do both jobs without ambiguity, provided you never have a period where the system cannot tell whether a trigger means “start” or “fault”.

## Timestamping arrangement

Inside the FPGA, you would normally have a free-running counter:

```text
timestamp_counter <= timestamp_counter + 1 every FPGA clock
```

Then on trigger edge:

```text
if state == ARMED:
    run_start_time <= timestamp_counter
    state <= RUNNING

if state == RUNNING:
    fault_time <= timestamp_counter
    fault_latched <= true
    state <= FAULT_LATCHED
```

That gives you deterministic timing because the event is captured in hardware. LabVIEW can read the recorded values later without affecting event timing.

For example:

```text
Clock = 100 MHz
Counter tick = 10 ns

Trigger in ARMED:
    run_start_count = 1,245,500,000

Trigger in RUNNING:
    fault_count = 1,259,200,000

Fault occurred:
    13,700,000 ticks after run start
    = 137 ms after run start
```

That is the proper way to get sub-second timing accuracy. You are not asking Windows or LabVIEW when the event happened; the FPGA has already captured it.

## Important caveat: do not make the meaning ambiguous

The risky version is this:

```text
External trigger = start test
External trigger = fault
```

with no clearly defined mode separation.

That can create edge cases:

- A noise spike starts a test.
- A real fault arrives before the system has fully entered RUNNING.
- A late start pulse is interpreted as a fault.
- A fault pulse during ARMED falsely starts the test.
- LabVIEW thinks the system is armed, but the FPGA state is already running.

So the FPGA must be the authority on state. LabVIEW should request mode changes, but the FPGA should decide what state it is actually in.

## Better design: qualify the trigger by an enable/state signal

If you can spare another line, the cleaner design is:

```text
Line 1: START_TRIGGER
Line 2: FAULT_IN
```

But if you only have one external line, then use internal qualification:

```text
Trigger line + FPGA state = interpreted event
```

For example:

```text
trigger_edge AND state == ARMED   → start/synchronise test
trigger_edge AND state == RUNNING → latch fault
trigger_edge AND state == IDLE    → ignore or log unexpected trigger
```

You can also log unexpected events:

```text
trigger_edge AND state == IDLE → unexpected_trigger_count++
```

That is useful diagnostically.

## External trigger polarity and pulse width

The FPGA input should not just be a raw wire into logic. I would normally include:

```text
External input
   │
   ├── input protection / appropriate voltage translation
   ├── debounce/filter if mechanical or noisy
   ├── synchroniser into FPGA clock domain
   ├── edge detector
   ├── optional pulse stretcher
   └── state machine
```

For an FPGA, any asynchronous external input needs synchronising to avoid metastability. Usually that means a two-flop synchroniser before edge detection:

```text
async_trigger → FF1 → FF2 → edge detect
```

If the pulse is very narrow, you may need pulse stretching or a proper input capture circuit so the FPGA does not miss it.

## Recommended architecture

For your case, I would think of it like this:

```text
Stable reference clock
        │
        ▼
FPGA timestamp counter
        │
        ▼
FPGA state machine
        │
        ├── ARMED:
        │       external trigger = capture t0, enter RUNNING
        │
        ├── RUNNING:
        │       external trigger = capture fault time, latch fault, enter FAULT
        │
        └── FAULT:
                hold fault state until explicit reset
```

LabVIEW then reads:

```text
current_state
run_start_timestamp
fault_timestamp
fault_latched
unexpected_trigger_count
last_trigger_state_context
```

That last one is useful: record what state the FPGA was in when the trigger occurred. Then you can later prove whether the edge was used as a start event, fault event, or ignored event.

## My preferred answer

The FPGA should be the **deterministic timing authority**, but the **master clock should ideally come from the best available reference**, not just whatever oscillator happens to be on the FPGA card.

And yes, one external trigger can serve both functions, but only by using a **state-qualified interpretation**:

```text
ARMED + trigger edge   = start/sync test
RUNNING + trigger edge = fault flag
FAULT + trigger edge   = ignored/logged
```

That is the clean conceptual model. It keeps the hardware simple while preserving deterministic timing and avoiding LabVIEW/software timestamp limitations.

[M5] ME (2026-06-23 18:11):
So I mean ext trigger as pzi input / FPGA output

[M6] AI (2026-06-23 18:11):
Yes — that makes sense.

You mean:

```text
External trigger into PXI/controller side
        │
        ▼
PXI/LabVIEW/controller detects test state
        │
        ▼
FPGA outputs a deterministic signal
```

or more specifically:

```text
PXI external trigger input  →  FPGA-controlled output
```

In that case the clean architecture is:

```text
External trigger into PXI
        │
        ▼
PXI trigger/backplane route
        │
        ▼
FPGA sees trigger
        │
        ▼
FPGA state machine decides meaning
        │
        ├── ARMED state: output RUN/SYNC pulse
        └── RUNNING/FAULT state: output FAULT flag
```

The important point is: **the FPGA output should not simply mirror the external trigger.**  
It should be a **state-qualified output**.

So:

```text
if state == ARMED:
    ext_trigger_edge → FPGA outputs "test_start_sync"

if state == RUNNING:
    ext_trigger_edge → FPGA outputs/latches "fault_flag"
```

That gives you one external trigger input doing two roles, but the FPGA output meaning is controlled by the internal state machine.

A sensible signal set would be:

```text
PXI_EXT_TRIG_IN        external edge into system
FPGA_RUN_SYNC_OUT      pulse generated when trigger starts test
FPGA_FAULT_OUT         latched output generated if trigger occurs during fault-monitoring/run state
FPGA_STATE             IDLE / ARMED / RUNNING / FAULT
```

If you only have **one FPGA output** as well, then you can multiplex the meaning, but I would avoid that unless forced. Better is:

```text
One input:
    EXT_TRIG_IN

Two outputs:
    RUN_SYNC_OUT
    FAULT_OUT
```

If only one output is available:

```text
FPGA_STATUS_OUT = 1 pulse in ARMED means run sync
FPGA_STATUS_OUT = latched high in RUNNING means fault
```

But that is less clean because the receiver also needs to know the current mode.

Best practical version:

```text
EXT_TRIG_IN → FPGA edge capture

When ARMED:
    latch t0
    output RUN_SYNC_OUT pulse
    enter RUNNING

When RUNNING:
    latch fault timestamp
    set FAULT_OUT high
    enter FAULT_LATCHED
```

So yes: **PXI input / FPGA output is a valid way to do it**, but the FPGA should act as the deterministic interpreter, not just a wire-through buffer.

[M7] ME (2026-06-23 18:27):
I’ll explain the problem a little bit more before asking you to consolidate all info and proposals for the enhancement 

The current test system monitors a number of parameters which are biased current event flags per bias exposure shutter status open or closed fluent dose count where each particle represents 100ns pulse received by the system and counts. Finally there is a timestamp and the whole thing logs at about one hertz which doesn’t give a great deal of resolution. With the next generation system there is a king requirements to get better time stamping for different system functions operations modes so that any event can be referenced against the timestampand maybe things are only logged once an event has been acknowledged

[M8] AI (2026-06-23 18:27):
Yes, I follow. The current limitation is not that the system lacks events — it has plenty of useful state/event information — but that the **logging layer is too slow and too coarse**.

At the moment it sounds roughly like this:

```text
System parameters / event flags
    ├── bias current / bias exposure status
    ├── shutter open/closed state
    ├── fluence / dose count
    ├── particle pulse count, where each pulse is ~100 ns
    ├── operating mode / fault mode
    └── timestamp

Logged by LabVIEW/PXI/controller at ~1 Hz
```

So the problem is:

```text
Events may happen at millisecond / microsecond / 100 ns scale
but the system record only updates at ~1 second scale
```

That means the log can tell you **that something happened**, but not reliably:

```text
exactly when it happened
what happened first
how long a state lasted
whether event A caused event B
whether a fault occurred before/after shutter transition
how many dose pulses occurred during a specific exposure window
```

For the next-generation system, the enhancement requirement sounds like it should be reframed as:

> Move from slow periodic logging to deterministic event-based timestamping.

So instead of relying on a 1 Hz LabVIEW/controller log, the FPGA/PXI timing layer should capture events as they happen and attach them to a shared timebase.

A better architecture would be:

```text
Stable reference clock
        │
        ▼
FPGA / timing module timestamp counter
        │
        ▼
Event capture layer
        │
        ├── bias enable/disable
        ├── bias current threshold event
        ├── exposure start/stop
        ├── shutter open/closed transition
        ├── fluence pulse count
        ├── dose count milestone
        ├── operating mode change
        ├── fault assertion
        └── fault acknowledge / clear
        │
        ▼
Event FIFO / buffer
        │
        ▼
LabVIEW/controller reads and logs events
```

The key improvement is that LabVIEW does **not** need to timestamp the event in real time. The FPGA/timing hardware timestamps it, stores it, and LabVIEW can read it later.

For example, instead of a 1 Hz log like:

```text
12:00:01  shutter=open, bias=on, dose=15320, fault=0
12:00:02  shutter=closed, bias=off, dose=17200, fault=1
```

You get event records like:

```text
12:00:01.003421  bias_enabled
12:00:01.004102  shutter_open
12:00:01.004115  exposure_started
12:00:01.153820  dose_count=1000
12:00:01.303821  dose_count=2000
12:00:01.422910  fault_detected
12:00:01.423005  shutter_closed
12:00:01.423180  bias_disabled
12:00:01.700204  fault_acknowledged
```

That gives you a proper sequence of events.

The phrase “maybe things are only logged once an event has been acknowledged” is important. I would separate this into two layers:

```text
1. Event capture
   Must happen immediately and deterministically.

2. Event acknowledgement / logging / reporting
   Can happen later in software.
```

So I would not make acknowledgement a condition for capturing the event. I would capture first, then acknowledge later.

Better:

```text
Event occurs
    ↓
FPGA timestamps and latches event
    ↓
Event goes into FIFO/buffer
    ↓
LabVIEW reads event
    ↓
LabVIEW acknowledges it has consumed/logged event
    ↓
FPGA clears or advances buffer pointer
```

Not:

```text
Event occurs
    ↓
Wait for software acknowledgement
    ↓
Then timestamp/log event
```

because that reintroduces software timing uncertainty.

For the external trigger / PXI input / FPGA output idea, it could fit like this:

```text
External trigger into PXI/FPGA
        │
        ▼
FPGA captures edge time
        │
        ├── If ARMED:
        │       define test t0 / run sync
        │
        ├── If RUNNING:
        │       mark fault/event/special condition
        │
        └── If FAULT:
                mark acknowledge/clear/safe-state transition if required
```

But I would be careful not to overload one trigger too much unless the system state makes the meaning completely unambiguous.

A clean next-gen requirement might be:

```text
The system shall maintain a hardware-derived timestamp counter common to all monitored events.

The system shall timestamp significant state transitions, fault assertions, shutter changes, bias changes, exposure start/stop events, and fluence/dose count milestones at the point of detection in FPGA/timing hardware.

The controller/LabVIEW layer shall read timestamped event records from a hardware buffer and shall not be relied upon for sub-second event timing.
```

For your eventual consolidated proposal, I’d structure it around these headings:

```text
1. Current limitation
   1 Hz polling/logging cannot resolve fast event ordering.

2. Required enhancement
   Hardware timestamping of operational, exposure, dose, shutter, bias, and fault events.

3. Proposed architecture
   Shared reference clock, FPGA timestamp counter, event capture logic, FIFO/event buffer, LabVIEW logger.

4. Event model
   Each event record contains timestamp, event type, state/mode, value/count, and acknowledgement status.

5. External trigger behaviour
   PXI input captured by FPGA; interpreted by state machine; FPGA output used for run sync/fault signalling.

6. Fault handling
   Faults are latched immediately with timestamp; software acknowledgement is separate from event capture.

7. Benefits
   Better ordering, traceability, exposure reconstruction, fault diagnosis, and cross-system correlation.
```

The central concept is:

> The system should stop treating the 1 Hz log as the source of truth. The source of truth should become a hardware-timestamped event stream, with the 1 Hz log becoming only a summary/status layer.

[M9] ME (2026-06-23 18:31):
Summarise this into a one page proposal that responds to the request for improvements in useful meta data and sub one second time stamping

[M10] AI (2026-06-23 18:31):
Here’s a one-page proposal version you can reuse or adapt.

:::writing{variant="document" id="48291"}
# Proposal: Enhanced Metadata and Sub-Second Event Timestamping for Next-Generation PXI/FPGA Test System

## Background

The current test system records a number of useful operational parameters, including bias current status, bias exposure state, shutter open/closed status, fluence/dose count, particle pulse counts, operating mode, fault/event flags, and a timestamp. However, the system presently logs at approximately 1 Hz. This provides a useful high-level status record, but it does not provide sufficient temporal resolution to determine the precise order, timing, or causal relationship between fast-changing system events.

This limitation is particularly relevant where events may occur over milliseconds, microseconds, or shorter timescales, while the data record is only updated once per second. As a result, the existing log may show that a fault, shutter transition, bias state change, or dose-count change occurred, but not exactly when it occurred relative to other system actions.

## Proposed Enhancement

The next-generation system should move from primarily periodic software logging to a hardware-assisted, event-based timestamping architecture. The key proposal is to use the PXI/FPGA layer as the deterministic event-capture and timestamping authority, while LabVIEW/controller software remains responsible for supervisory control, display, data handling, and higher-level logging.

A shared hardware timebase should be established using the most suitable available reference clock, such as the PXI backplane reference, a timing module, or another stable system reference. The FPGA should maintain a free-running timestamp counter derived from this reference. Significant events should then be captured directly in FPGA/timing hardware, with the timestamp latched at the instant the event is detected.

This avoids relying on Windows, LabVIEW loop timing, or controller polling latency for sub-second timestamp accuracy.

## Events to Timestamp

The enhanced system should timestamp, as a minimum:

- Bias enable/disable transitions
- Bias current threshold or out-of-range events
- Exposure start and stop
- Shutter open/closed transitions
- Fluence/dose count milestones
- Particle pulse count activity, where each detected particle pulse represents a 100 ns pulse received by the system
- Operating mode changes
- Fault assertion
- Fault acknowledgement and fault clear events
- External trigger events
- Unexpected or out-of-sequence trigger events

Each event record should include useful metadata, not only a timestamp. A proposed event record format would include:

```text
Timestamp
Event type
System mode/state at time of event
Associated parameter value or count
Fault/status flags
Acknowledgement state
Source of event
Sequence number
```

## External Trigger and FPGA Output Behaviour

The external trigger input to the PXI/FPGA system should be captured by the FPGA and interpreted according to the current system state. The FPGA should not simply mirror the external trigger; it should state-qualify the trigger and generate the appropriate deterministic output or internal event.

For example:

```text
ARMED + external trigger edge   = capture test t0 and generate run/sync output
RUNNING + external trigger edge = capture fault/event timestamp and assert fault flag
FAULT state + trigger edge      = ignore or log as unexpected, depending on requirement
```

This allows a single external trigger input to support both test synchronisation and fault/event signalling, provided that the FPGA state machine makes the meaning unambiguous.

## Logging and Acknowledgement

The system should separate immediate event capture from later software acknowledgement. Events should be timestamped and buffered immediately in FPGA hardware. LabVIEW should then read the event records from an event FIFO or buffer and acknowledge once the event has been consumed, logged, or displayed.

The system should avoid designs where an event is only timestamped after software acknowledgement, as this would reintroduce non-deterministic software timing delays.

## Expected Benefits

This enhancement would provide:

- Sub-second event timing independent of LabVIEW loop rate
- Deterministic ordering of shutter, bias, exposure, dose, trigger, and fault events
- Improved post-test reconstruction of what happened and when
- Clear separation between hardware event capture and software logging
- Better fault diagnosis and causal analysis
- More useful metadata for test reports, fault investigations, and system validation
- Compatibility with existing lower-rate summary logging, while adding a higher-resolution event record

## Summary

The proposed improvement is to make the PXI/FPGA layer responsible for deterministic event capture and timestamping, using a shared hardware timebase and timestamped event buffer. The existing 1 Hz log can remain as a useful status summary, but it should no longer be the primary source of truth for event timing. The next-generation system should instead generate a hardware-timestamped event stream containing meaningful metadata for all significant system functions, operating modes, trigger events, and fault conditions.
:::

=== ALTERNATE BRANCHES (edited/regenerated messages not on the final thread) ===

[A1] AI (2026-06-23 18:11):
Yes — that makes sense.

You mean:

```text
PXI / controller external trigger input
        │
        ▼
PXI system / LabVIEW sees trigger
        │
        ▼
FPGA outputs a deterministic run/fault signal
```

In that case, I’d be careful with one thing: **the PXI controller should not be in the timing-critical path** if you need precise timing.

Better architecture:

```text
External trigger
        │
        ▼
FPGA / timing-capable PXI module input
        │
        ├── timestamps trigger
        ├── updates internal state
        └── drives FPGA output
```

So the FPGA output becomes the clean, deterministic signal distributed to the rest of the system.

The external trigger into PXI can mean:

```text
if FPGA/test state == ARMED:
    FPGA output = RUN_SYNC / TEST_ACTIVE

if FPGA/test state == RUNNING:
    FPGA output = FAULT_FLAG
```

But I would avoid using the **same physical FPGA output** to mean both things unless the receiving system also knows the mode.

Cleaner:

```text
FPGA_OUT_1 = TEST_RUNNING
FPGA_OUT_2 = FAULT_LATCHED
```

If you only have one FPGA output available, then use level/state encoding:

```text
LOW  = not running / no fault
HIGH = running
PULSE or latched change during RUNNING = fault
```

But that can get ambiguous.

Better single-line encoding would be:

```text
Before test:
    output LOW

On valid start trigger:
    output HIGH = test running

On fault:
    output LOW again, plus FPGA logs fault timestamp
```

Then the external system interprets:

```text
Rising edge = test started
Falling edge during run = fault/abort
```

That is much less ambiguous than “same edge sometimes means start, sometimes means fault.”

So in your case I’d do:

```text
External trigger into PXI/FPGA
        │
        ▼
FPGA state machine
        │
        ├── captures timestamp
        ├── determines whether trigger means start or fault
        └── drives output line to external system
```

And the key rule:

**PXI/LabVIEW can configure and log; FPGA should decide and output the real-time state.**
