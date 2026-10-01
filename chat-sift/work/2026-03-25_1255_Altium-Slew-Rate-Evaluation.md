# Altium Slew Rate Evaluation
Date (UTC): 2026-03-25 12:55
Conversation ID: 69c3db0d-2ee4-8396-b2a5-df45c3125e0d
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-03-25 12:55):
I need to evaluate the performance of an el driver adjusting slew rates if ccd clocks using asg part. I’ve been directed to spice but keen to use Altium. Please provide a process to the best of you knowledge how to work altium to do this 

[M2] AI (2026-03-25 12:55):
Yes — you can use Altium for this, and it is a sensible first pass for **slew-rate evaluation of CCD clock drive shaping**, provided you treat it as a **circuit-level approximation**, not final truth.

The key point is this:

**Altium’s mixed simulator is SPICE-based**, so it can run transient analyses, parameter sweeps, and measurements directly from the schematic, as long as you have valid simulation models attached to the parts. It supports running transient analysis from the Simulation Dashboard and working from SPICE/PSpice-style models. citeturn618666search0turn618666search1turn618666search9turn618666search14

For your use case — **EL driver + slew-control network + CCD clock load emulation** — the best workflow is:

## 1. Decide what you are actually trying to prove

Before touching Altium, define the exact outputs you want from the simulation.

For a CCD clock slew study, the usual questions are:

- What is the **10–90% rise time** and **90–10% fall time** at the clock output?
- How does that change with the **ASG-selected resistor/cap network**?
- What is the **peak source/sink current** in the driver?
- What is the **dynamic dissipation** in the driver and shaping parts?
- Does the waveform **ring**, overshoot, or undershoot into the expected clock load?
- How sensitive is it to **load capacitance**, cable/parasitic capacitance, or supply spread?

That matters because you should build the simulation around **measurable pass/fail quantities**, not just “does the edge look nice”.

## 2. Build a simulation-only schematic, not your whole project

Do **not** start by simulating the full board.

Make a **dedicated simulation sheet/project** containing only:

- the EL driver
- the ASG switch or equivalent switch element
- the resistor/capacitor slew network
- the CCD clock load model
- supply rails
- input pulse source
- probes/net labels

This is much easier to control and debug.

In practice, I would build a small testbench like this:

**Pulse source → logic interface / input conditioning → EL driver → slew network → CCD clock load**

And then add:
- one ideal ground
- realistic supply decoupling
- optional series trace resistance / inductance
- optional parasitic capacitance at the output node

## 3. Get the right models first

This is the make-or-break step.

Altium can simulate only if the active parts have usable simulation models attached. Altium’s docs explicitly note that simulation depends on having accurate SPICE/IBIS/vendor models correctly linked to schematic pins, and that complex ICs often do not have ideal simulation support. citeturn618666search5turn618666search13turn618666search14

For your case:

### Best case
You have a **vendor SPICE/PSpice model** for:
- the EL driver
- the ASG analogue switch

### Acceptable case
You have:
- vendor model for the EL driver
- simplified switch model for the ASG
- ideal or estimated load

### Realistic fallback
If no good model exists:
- use a **behavioral approximation**
- or use a **voltage-controlled switch**
- or use a **piecewise-linear output stage approximation**

That still gives useful trend data.

## 4. Model the ASG part at the right level

You said “ASG part” — I assume this is the **analog switch selecting different slew-control components**.

For the simulation, what matters most is usually not the digital control internals, but:

- **R\_ON**
- **R\_ON flatness / variation**
- charge injection, if relevant
- switch capacitance
- off leakage, if extreme
- bandwidth / edge interaction

For a first-pass simulation, you can model the ASG in one of three ways:

### Option A — ideal switched resistor/cap network
Fastest and often enough for comparison:
- create separate cases for each RC setting
- bypass actual switch behavior entirely

This is good when you just want:
“what slew rate does this RC option create?”

### Option B — voltage-controlled switch
Better:
- use SPICE switch element with defined on/off resistance
- include output capacitance manually if needed

### Option C — vendor model
Best:
- attach the actual switch macromodel

For early work, I would honestly start with **Option A**, then add switch realism later.

## 5. Model the CCD clock load properly

This is the other critical piece.

If you simulate just into an open circuit or a single capacitor, the result may look flattering but be misleading.

Your load model should include as much of this as you know:

- CCD clock input capacitance
- package parasitics
- flex/cable capacitance
- PCB trace parasitics
- termination or damping resistor if present
- any clamp/protection network
- bias conditions that affect swing

At minimum, build:

- **Cload** representing total effective capacitive load
- small series **Rtrace**
- optional small **Ltrace**
- optional shunt parasitics

Then run the same circuit over a **range of Cload values**.

That is often more valuable than arguing over one exact capacitance figure.

## 6. In Altium, attach simulation models to the parts

Once the schematic is drawn:

- open component properties
- attach/import the SPICE model to the active devices
- map model pins to schematic pins carefully
- verify ground and supply references
- confirm all powered devices actually have their rails connected in the simulation view

Altium’s simulation flow depends on the schematic being prepared correctly with valid models and the project being verified before running analysis. citeturn618666search13turn618666search0

Pin mapping errors are one of the most common reasons simulations silently mislead.

## 7. Drive it with a realistic pulse source

For a CCD clock edge study, your input source should match the real interface as closely as practical.

Usually:
- pulse low/high levels
- repetition rate
- rise/fall time
- duty cycle
- source impedance

In other words, don’t drive the EL input with a mathematically perfect zero-ohm, zero-rise-time source unless that really reflects the upstream logic.

A slightly realistic source often changes the answer.

## 8. Run **transient simulation**

This is the main analysis for slew-rate work.

Altium’s simulation environment supports transient analysis from the Simulation Dashboard, with waveform viewing and measurements. citeturn618666search0turn618666search1turn618666search16

In Altium, the practical sequence is:

1. Open the simulation dashboard/panel.
2. Enable **Transient** analysis.
3. Set:
   - stop time
   - maximum time step
   - startup conditions if needed
4. Run the simulation.
5. Plot:
   - driver input
   - driver output
   - CCD clock node
   - current through driver / shaping resistor / switch
   - supply current if you want dissipation

### Important setup tip
Set the **maximum timestep** much smaller than the edge you are studying.

For example, if your edge is around 10 ns, do not allow a timestep of several ns.  
You want enough resolution to extract proper 10–90% timing and ringing.

## 9. Measure the right things

Do not just eyeball the waveform.

Use waveform measurements or manual cursor extraction to capture:

- rise time
- fall time
- overshoot
- undershoot
- settling time
- peak current
- RMS or average current over a cycle
- power in driver / resistor / switch

If available in your Altium version, automated measurements can help streamline this. Altium has documented measurement-oriented simulation workflows in its newer simulation material. citeturn618666search6turn618666search16

For your note/report, I would tabulate each ASG setting like this:

| Setting | Rsel | Csel | Vhigh | Vlow | Rise 10–90 | Fall 90–10 | Overshoot | Peak Idrv | Avg Power |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|

That becomes your engineering evidence.

## 10. Run **parameter sweeps**

This is where Altium becomes genuinely useful.

Rather than one fixed run, sweep:

- selected resistor value
- selected capacitor value
- load capacitance
- driver supply
- switch R\_ON
- temperature-related component drift if approximated
- series damping resistance

Altium’s simulation environment supports parametric/sensitivity style workflows and simulation configuration beyond one-off runs. citeturn618666search1turn618666search12

For your case, the most useful sweeps are probably:

### Sweep A — per slew setting
Compare each ASG-selected RC option.

### Sweep B — per CCD load corner
For each setting, run:
- nominal Cload
- low Cload
- high Cload

### Sweep C — supply/process realism
Run:
- low rail
- nominal rail
- high rail

That gives you a corner view instead of one pretty waveform.

## 11. Check current and dissipation, not just edge speed

Because you are concerned with the EL driver performance, look at:

- peak output current
- average current per transition
- energy per transition
- part dissipation trend across settings

A slower edge may reduce EMI/ringing but increase time in the linear region. A sharper edge may increase dynamic current and overshoot. The useful answer is usually the **best compromise**, not the absolute fastest or slowest slew.

## 12. Validate the model before trusting it

This is crucial.

Before using the simulation for decisions, ask:

- Does the unloaded or lightly loaded result look physically plausible?
- Do swing levels match what the real driver can produce?
- Does the driver current look sensible versus datasheet limits?
- Does the edge change in the expected direction when R/C changes?
- Does increasing load capacitance slow the edge as expected?

If not, the model is wrong or incomplete.

## 13. Know where Altium is enough, and where it is not

Altium is good here for:

- first-order transient behavior
- RC shaping comparison
- switch-setting comparison
- current trend estimation
- sensitivity sweeps
- documenting design intent directly in your schematic flow

Altium is weaker if you need:

- deep semiconductor-level confidence in a proprietary driver macromodel
- transmission-line fidelity for longer interconnects
- very detailed package parasitics
- robust convergence with awkward vendor models
- advanced scripting/automation compared with dedicated SPICE tools

So my honest view is:

### Use Altium if:
- you want a structured, integrated, schematic-led evaluation
- the circuit is fairly compact
- the key need is comparing settings and trends

### Use LTspice / PSpice as fallback if:
- Altium chokes on the vendor model
- you need faster iteration
- you need more direct control of the raw netlist
- the model support becomes painful

## 14. Recommended practical workflow for your exact task

This is the process I would actually follow:

### Phase 1 — simplest truth model
- Build EL driver output stage
- Represent ASG selection as fixed RC options
- Model CCD load as lumped capacitance
- Run transient
- Measure rise/fall/current

### Phase 2 — realism upgrade
- Add ASG switch R\_ON and capacitance
- Add trace parasitics
- Add decoupling and rail impedance
- Re-run

### Phase 3 — corner analysis
- Sweep load capacitance
- Sweep supply
- Sweep RC settings
- Tabulate results

### Phase 4 — bench correlation
- Compare simulated rise/fall and current trend with first hardware measurements
- Tune parasitics if necessary

That is the fastest route to something engineering-useful.

## 15. Suggested Altium setup checklist

Use this as your working checklist:

**Project setup**
- new simulation-only schematic
- single test channel first
- ground and rails clearly defined

**Models**
- EL driver model attached
- ASG model or substitute attached
- pin mapping checked
- passive values verified

**Stimulus**
- realistic pulse source
- correct amplitude and timing
- source impedance included if relevant

**Load**
- CCD equivalent capacitance included
- trace/cable parasitics included
- damping/protection included if present

**Analysis**
- transient enabled
- stop time sufficient for several cycles
- max timestep small enough for ns-edge capture

**Outputs**
- Vout
- I(driver)
- I(slew resistor)
- supply current
- power/dissipation traces

**Sweeps**
- resistor setting
- capacitor setting
- load capacitance
- supply corners

**Review**
- edge time
- overshoot
- settling
- peak current
- dissipation

## 16. My recommendation in one line

**Use Altium to build a compact transient simulation testbench and compare ASG-selected slew networks by parametric sweep, but keep the model intentionally simple at first and only add realism once the basic trends behave sensibly.**

That will get you to a solid answer much faster than trying to simulate the whole design from day one.

If useful, I can turn this into a **worked Altium procedure** with menu-by-menu steps and a **recommended example testbench topology** for your EL driver + ASG-selected RC network.

[M3] ME (2026-03-29 15:24):
Run me through the stages.
Assuming a 3v input signals with 12ns slew.
Target output 12v with 3rd slew 

[M4] AI (2026-03-29 15:24):
I’m treating “3rd slew” as **3 ns output edge**. I’m checking the Altium-side workflow against current docs, then I’ll map your numbers onto a practical simulation flow.

[M5] AI (2026-03-29 15:25):
Below is the way I’d run it in **stages**, using **Altium transient simulation** as the main vehicle.

I’m assuming your target is:

- **Input:** 0–3 V logic-like signal
- **Input edge:** about **12 ns**
- **Required output:** **0–12 V**
- **Target output edge:** about **3 ns**
- **Application:** CCD clock drive, with selectable slew shaping via an ASG / analog-switch arrangement

The big engineering point first:

A **12 ns input edge does not automatically prevent a 3 ns output edge** if the downstream stage is an **edge-regenerating amplifier/driver** powered from higher rails and not just a passive scaler. But if the output stage is effectively linear and bandwidth-limited, then the slow input edge will simply propagate and you will not magically get 3 ns. So the whole simulation is really about answering: **is the EL driver behaving like a proper high-current thresholded switch/driver, or merely a follower-like amplifier under your conditions?**

Altium supports this kind of work through its SPICE-based simulation flow, including model attachment, transient setup in the Simulation Dashboard, and results viewing. It also supports SPICE2/3 and XSPICE, with some support for PSpice and LTspice variants in newer releases. citeturn562845search0turn562845search1turn562845search2turn562845search5

## Stage 1 — define exactly what you are proving

Before building anything, decide the pass/fail outputs.

For your case I would make the simulation answer these:

1. Does a **3 V / 12 ns** input produce a **12 V** clock with about **3 ns** rise/fall?
2. What slew settings from the ASG network achieve that?
3. What is the **peak driver current**?
4. Is there **overshoot, ringing, or long settling**?
5. How much does the result change with **CCD load capacitance**?

Your report table should eventually look like this:

| Setting | Input edge | Load C | Vout swing | Rise 10–90% | Fall 90–10% | Overshoot | Peak current | Comment |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A | 12 ns | C1 | 12 V | x ns | x ns | x % | x A | pass/fail |

That keeps the whole exercise grounded.

---

## Stage 2 — do the first-order feasibility check by hand

Before opening Altium, do a sanity check.

If the output is **12 V** and the target edge is **3 ns**, then the required average dv/dt is:

\[
dv/dt \approx \frac{12V}{3ns} = 4\ V/ns
\]

If the load is capacitive, the required current is:

\[
I = C \cdot \frac{dV}{dt}
\]

So for example:

- **50 pF** load → \( I = 50pF \cdot 4V/ns = 0.2A \)
- **100 pF** load → \( I = 0.4A \)
- **200 pF** load → \( I = 0.8A \)

That immediately tells you whether the target is even plausible. If your total CCD clock load plus parasitics is high, a 3 ns edge becomes a serious current problem.

So at this stage, estimate:

- CCD input capacitance
- package capacitance
- PCB trace capacitance
- cable/flex capacitance
- switch parasitics

Then set three load cases:

- **Low**
- **Nominal**
- **High**

This is one of the most useful things you’ll do.

---

## Stage 3 — decide what kind of model you have for the EL driver

This is the fork in the road.

### Case A — you have a vendor SPICE/PSpice model
Best route. Use it.

### Case B — you do not have a usable model
Then create a behavioral approximation first.

Because Altium’s simulator depends on linked SPICE-type models and proper project preparation, this part matters a lot. Altium’s documentation also points to the SPICE Model Wizard and supported model types as the foundation for simulation setup. citeturn562845search1turn562845search7turn562845search13

For the first pass, even a simplified model is fine if it captures:

- threshold-ish switching behavior
- finite output resistance
- finite output current
- rail limits
- output capacitance / bandwidth effects

Do **not** wait for a perfect model before you start learning from the circuit.

---

## Stage 4 — build a dedicated simulation sheet in Altium

Do **not** simulate the full board first.

Create a small testbench schematic:

**VPULSE input → input conditioning (if any) → EL driver → slew network / ASG selection → CCD load model**

Also include:

- supply rails
- decoupling capacitors
- ground
- probes / named nets

In Altium, this means:

1. Create a **new schematic** just for simulation.
2. Place only the relevant parts.
3. Keep one clock channel only.
4. Label key nodes:
   - `VIN`
   - `DRV_IN`
   - `DRV_OUT`
   - `CLK_LOAD`
   - `I_SUPPLY`

This is much easier to debug than a full design.

---

## Stage 5 — create the input stimulus correctly

Your input is not “3 V static”; it is a pulse with a controlled edge.

So your source in Altium SPICE should be a **PULSE source** with something like:

- low = 0 V
- high = 3 V
- rise time = 12 ns
- fall time = 12 ns
- pulse width = enough to observe full transition
- period = comfortably longer than the edge, maybe 500 ns or 1 µs for initial work

For example, conceptually:

- `V1 = PULSE(0 3 20n 12n 12n 200n 500n)`

That gives you a clean but realistic 3 V edge to drive the system.

At this stage, also include any **source resistance** if the upstream logic path is not ideal.

---

## Stage 6 — model the ASG-controlled slew network in the simplest useful way

For the first run, do **not** start with the real switch control logic.

Instead, split the problem:

### First-pass approach
Model each ASG setting as a fixed RC/damping case.

So if the ASG selects among resistor values or capacitor values, create separate variants such as:

- Setting A: R1/C1
- Setting B: R2/C1
- Setting C: R3/C1
- Setting D: R2/C2

This gives you immediate engineering value:
“Which network gives the best 3 ns result without ugly ringing?”

Later, you can bring in the actual switch model.

---

## Stage 7 — build the CCD load model

This is where many simulations go wrong.

At minimum, your output load should include:

- **Cload** = CCD clock capacitance plus parasitics
- small **series R** for trace/package path
- optional small **L** if interconnect is non-trivial

[M6] ME (2026-03-29 15:25):
The output part is the ada part

[M7] AI (2026-03-29 15:25):
I’m narrowing this to the **actual output stage device** and the exact simulation path in Altium. I’ll check what Analog Devices provides for the ADA part and then lay out the stages around that.

[M8] AI (2026-03-29 15:26):
Under those assumptions, the **first stage is not Altium — it is feasibility**.

With a **12 V output step** and a **3 ns edge target**, the required slew rate is about:

\[
SR \approx \frac{12\text{ V}}{3\text{ ns}} = 4\text{ V/ns} = 4000\text{ V/}\mu\text{s}
\]

The **ADA4870** is specified at about **2500 V/µs typical**, so on datasheet numbers alone it is **below** the 4000 V/µs you’d need for a full 12 V transition in 3 ns. That means a plain “take 3 V in and amplify to 12 V with 3 ns edges” approach is **not likely achievable with the ADA4870 alone**, especially once real load capacitance is included. citeturn648293search1turn648293search17

Also, if your input edge is **12 ns**, a straightforward linear gain stage will usually **preserve or worsen** edge speed, not magically sharpen it by 4×. To get a faster output edge than the source, you generally need a different mechanism such as a thresholded switching stage, peaking/equalisation, or a dedicated faster driver architecture rather than simple voltage gain. That is an engineering inference from the slew-rate requirement and the device limit. citeturn648293search1turn648293search17

So I’d run this in **six stages** in Altium.

## 1. Define the exact transition you are testing

Before building the schematic, lock down:

- input low/high voltage
- whether the 12 V output means **0 → 12 V**, **−6 → +6 V**, or **some other swing**
- output load capacitance
- repetition rate
- any series resistor / ASG-selected network
- what node you are measuring at

This matters because **3 ns on a 12 V swing** is very different from **3 ns on only part of that swing**.

For simulation, define the measurement as:

- **10–90% rise time**
- **90–10% fall time**
- output overshoot / undershoot
- peak output current
- current through the shaping resistor/switch
- settling time

Altium’s simulation flow is based around preparing the schematic, attaching models, and then running transient analysis from the Simulation Dashboard. citeturn648293search0turn648293search4turn648293search8

## 2. Do the hand-check before you simulate

Use a quick back-of-envelope check first.

For your target:

- **Required output slew** ≈ 4000 V/µs
- **ADA4870 typical slew** ≈ 2500 V/µs

So even before load effects, you are already asking more than the amplifier’s stated typical capability. citeturn648293search1turn648293search17

Then estimate output current for capacitive loading:

\[
I = C \cdot \frac{dV}{dt}
\]

Examples:

- 20 pF at 4 V/ns → 80 mA
- 50 pF at 4 V/ns → 200 mA
- 100 pF at 4 V/ns → 400 mA

That tells you how badly load capacitance will hurt the result.

So the real purpose of the simulation becomes:

- Can the ADA4870 get anywhere near the target?
- What edge do you actually get?
- How much does ASG-selected shaping help or hinder?
- What is the best achievable compromise?

## 3. Build a **simulation-only** Altium schematic

Do not simulate the full PCB project first.

Make a clean testbench with just:

- pulse source
- optional source resistance
- any input conditioning
- ADA4870 stage
- ASG-controlled slew network or its equivalent
- load model
- supply rails and decoupling
- measurement probes/net labels

The structure should be:

**Input pulse → ADA4870 configuration → output node → slew network / selected path → CCD clock load**

For the first pass, I would not even model the real ASG switching logic. I would build **separate test cases**:

- Case A: RC setting 1
- Case B: RC setting 2
- Case C: RC setting 3

That is faster and cleaner than fighting switch models too early.

## 4. Get the simulation model into Altium

This is the practical Altium part.

Altium supports SPICE-based simulation and can work with SPICE/XSPICE and some PSpice/LTspice variants, but model compatibility still matters. citeturn648293search18turn648293search0

The sequence is:

1. Place the ADA4870 symbol on a simulation sheet.
2. Open the component properties.
3. Attach the SPICE model for the ADA part.
4. Map model pins to schematic pins carefully.
5. Verify rails and grounds are connected.
6. Compile/check the project before running simulation.

Altium’s docs explicitly describe preparing the project, configuring analyses in the **Simulation Dashboard**, and then reviewing results in the waveform viewer. citeturn648293search0turn648293search4turn648293search8

If the vendor model is awkward, Altium also provides a **SPICE Model Wizard** for creating/linking models, and it can import LTspice designs with the LTspice Importer extension if you end up taking that route. citeturn648293search15turn648293search12

## 5. Set up the stimulus using your numbers

For your case, start with a pulse source approximating the real input:

- low = 0 V
- high = 3 V
- rise/fall = 12 ns
- realistic period
- realistic source impedance

Then configure the ADA stage exactly as you intend to use it.

But here is the key point: if you are hoping the amplifier alone converts:

- **3 V input**
- **12 ns input edge**
- into
- **12 V output**
- **3 ns output edge**

the simulation is likely going to confirm that this is not realistic for the ADA4870 as a linear output stage, because the required output slew exceeds the part’s stated typical slew capability. citeturn648293search1turn648293search17

## 6. Use a realistic output load model

This is where many simulations become over-optimistic.

At the output node, include:

- CCD clock equivalent capacitance
- PCB trace resistance
- optional small trace inductance
- any series damping resistor
- any clamp/protection parasitics

At minimum, use:

- `Cload`
- `Rseries`
- maybe `Lseries`

Then simulate several load cases, for example:

- 10 pF
- 25 pF
- 50 pF
- 100 pF

That will tell you whether the result is fundamentally source-limited or load-limited.

## 7. Run transient analysis in Altium

In Altium, use the **Simulation Dashboard** and set up **Transient** analysis. Altium documents this flow directly. citeturn648293search4turn648293search0

Use settings along these lines:

- stop time: enough for a few pulses
- max timestep: much smaller than the edge you want to inspect

For a 3 ns target, make the maximum timestep comfortably below that, otherwise the waveform will be too coarse to trust. The same transient-analysis guidance is reflected in Altium’s simulation material. citeturn648293search2turn648293search13

Probe:

- input node
- amplifier output
- final load node
- output current
- supply current

## 8. First run: no ASG shaping, just the bare ADA stage

This is important.

Before trying clever slew networks, simulate the ADA4870 by itself into the load.

You want to answer:

- what rise time do I get with no shaping?
- is it slew-limited?
- how much does load affect it?
- how much current is it sourcing/sinking?

This becomes your baseline.

I would expect this stage to show you whether the whole concept is already outside the amplifier’s natural limit.

## 9. Second run: fixed RC shaping options

Now add your slew-control options one by one.

For early work, don’t simulate the actual analog switch. Just hard-wire each configuration and run them separately:

- RC option 1
- RC option 2
- RC option 3
- etc.

For each run, record:

- 10–90% rise time
- overshoot
- settling
- peak current
- power in the resistor and amplifier

What you will probably see is that the shaping network helps control ringing and current, but it is unlikely to conjure a 3 ns full-swing edge if the amplifier itself cannot slew that fast.

## 10. Third run: include the ASG switch model

Once the fixed RC cases are behaving sensibly, add realism.

Model the ASG part as either:

- a vendor SPICE model
- a voltage-controlled switch
- or a simple switch with on-resistance and parasitic capacitance

At this stage you are checking:

- whether switch Ron changes the edge
- whether switch capacitance adds slowing
- whether the selected path behaves differently from the ideal hard-wired case

## 11. Sweep the variables

Now do the runs that actually answer the engineering question.

Sweep:

- load capacitance
- resistor setting
- capacitor setting
- supply voltage
- source edge rate if relevant

Then table the result.

A simple output table might be:

| Case | Load | Setting | Rise 10–90 | Fall 90–10 | Overshoot | Peak Iout | Notes |
|---|---:|---|---:|---:|---:|---:|---|
| Baseline | 25 pF | none | x ns | x ns | x % | x mA | bare ADA |
| A | 25 pF | RC1 | x ns | x ns | x % | x mA | stable |
| B | 25 pF | RC2 | x ns | x ns | x % | x mA | slower |
| C | 25 pF | RC3 | x ns | x ns | x % | x mA | rings |

That gives you a defensible answer rather than just a pretty plot.

## 12. Interpret the likely result for your numbers

With your present numbers, the likely conclusion is:

- **3 V input with 12 ns slew**
- **target 12 V output with 3 ns slew**
- **ADA4870 output stage**

is probably **not a realistic direct linear gain path**, because the output stage needs about **4000 V/µs**, while the ADA4870 is specified around **2500 V/µs typical**. citeturn648293search1turn648293search17

So the simulation should be used to show one of these:

1. the true achievable edge is slower than 3 ns,
2. the target is only reachable over a smaller swing,
3. the load must be very small,
4. or the architecture needs changing.

## 13. What architecture change may be needed

If 3 ns is genuinely mandatory, you are probably looking at one of these directions instead of relying on the ADA stage alone:

- faster dedicated high-voltage driver
- thresholded switching stage
- different pre-driver/driver partition
- smaller swing at the fast node followed by level translation
- reduced capacitive loading
- transmission-line style approach with damping and tighter load definition

That is the design question the Altium simulation should help you answer.

## 14. Best practical order in Altium

Use this order exactly:

1. Hand-calc required slew and output current.
2. Build a simulation-only schematic.
3. Attach ADA model.
4. Simulate bare amplifier into ideal then realistic load.
5. Add fixed RC settings one at a time.
6. Add ASG switch realism.
7. Sweep load and settings.
8. Tabulate results.
9. Decide whether the architecture is fundamentally viable.

## 15. My honest expectation

I would go into this assuming:

- the ADA4870 may still be useful,
- but **not as the sole mechanism** to turn a **12 ns, 3 V input edge** into a **12 V, 3 ns output edge**.

The simulation is still worth doing, because it will quantify:
- what you actually get,
- where the limit comes from,
- and whether the ASG-controlled shaping is helping stability versus just slowing things.

If you want, I can now give you a **literal Altium click-by-click setup** for this testbench, including what components to place and what transient settings to use.

[M9] ME (2026-03-29 15:27):
Forget simulation for now. What is the circuit flow required 

[M10] AI (2026-03-29 15:27):
At circuit-flow level, the path you need is:

**3 V source → edge interpreter / pre-driver → high-current level-shifting driver → slew-control network → CCD clock load**

The important bit is that you are **not** trying to “amplify a 12 ns edge into a 3 ns edge” with one ordinary gain block.  
You need a chain that does these jobs separately.

## 1. Input conditioning

Start with the 3 V signal and clean it up into something the next stage can switch decisively from.

This block can include:

- source termination if needed
- thresholding / buffering
- optional comparator / Schmitt behavior
- logic inversion if required

Purpose:

- present a **clean timing edge**
- remove ambiguity around slow-ish threshold crossing
- ensure the next stage sees a clear digital event, not a vague analog ramp

This is especially important if your incoming 12 ns edge is too soft for the rest of the chain.

---

## 2. Pre-driver / edge regenerator

This is the first truly important block.

If you need the output edge to be faster than the incoming edge, something in the chain must behave more like a **switching decision element** than a plain linear amplifier.

So this block should:

- detect the input crossing
- switch hard
- provide enough current to drive the main output stage input capacitance quickly

Typical role:

- logic buffer
- comparator-type stage
- dedicated gate/pre-driver
- fast differential receiver / translator, depending on architecture

Purpose:

- convert the incoming 3 V / 12 ns edge into a **sharper internal control edge**

Without this stage, a linear gain stage tends to inherit the slow input edge.

---

## 3. Level shift / amplitude translation

Now you need to move from the low-voltage control domain into the output swing domain.

If your final clock is 12 V swing, this block establishes that swing reference.

This may be:

- single-ended 0 to 12 V
- bipolar, for example −6 V to +6 V
- referenced around a CCD bias point

Purpose:

- translate logic-domain timing into the voltage domain the CCD clock actually needs

Sometimes this is integrated into the output driver. Sometimes it is separate.

---

## 4. Main output driver

This is the muscle stage.

This block must provide:

- voltage swing
- peak current
- capacitive load drive
- fast transition capability

This is where the ADA part sits if you are using it as the output stage.

But conceptually, this block is not “the whole answer.” It is just the **power edge delivery block**.

Purpose:

- charge and discharge the total clock load fast enough

At this point, the core equation is:

\[
I = C \cdot \frac{dV}{dt}
\]

So this block must supply the current needed for the total effective capacitance.

---

## 5. Slew-control block

This is where your ASG-selected network belongs.

This block is usually placed either:

- around the output driver feedback/compensation path, or
- directly at the output as a selectable shaping network

Typical elements:

- switched resistor values
- switched capacitor values
- series damping resistor
- RC snubber-type shaping
- selectable gate/base drive shaping in a switching architecture

Purpose:

- tune the trade between:
  - edge speed
  - ringing
  - overshoot
  - EMI
  - driver stress

This block should **trim** the edge, not rescue a fundamentally underpowered architecture.

That is a key distinction.

---

## 6. Output isolation / damping

Before the CCD load, you often want a small output network to stop the driver fighting parasitics.

This may include:

- small series resistor
- ferrite in some cases
- damping resistor at source
- clamp/protection network if needed

Purpose:

- isolate the output amplifier from pure capacitive load
- reduce peaking and ringing
- improve stability

For a very fast clock driver, this is often essential.

---

## 7. CCD clock load

This is the real destination, and it is not just “a pin.”

The load includes:

- CCD clock input capacitance
- package parasitics
- PCB trace capacitance/inductance
- connector/flex capacitance
- any probe loading during test

Purpose:

- define the real current demand and the real waveform shape

If you do not model this correctly, the rest of the design can look better on paper than it is.

---

# So the full conceptual flow is:

### Option A — if using a digital-style edge regeneration approach
**3 V input → fast threshold/buffer stage → level shift → main high-current output driver → selectable slew network → damping resistor → CCD clock**

### Option B — if using a more analog amplifier-led approach
**3 V input → conditioning/buffer → gain/level-shift stage → ADA output stage → selectable RC shaping → damping/isolation → CCD clock**

But for your requirement, I would lean more toward **Option A thinking**, even if the final power stage is analog.

Because the real need is:

- **timing event detection**
- then **fast energy delivery**

not just analog gain.

---

# What each block must achieve in your case

## Input conditioning
Take 3 V signal and make it robust.

## Pre-driver
Create a decisive internal control edge from the 12 ns input transition.

## Level shift
Move into the required clock voltage domain.

## Output driver
Provide the current to move the CCD clock node quickly.

## Slew network
Select how aggressive or damped the edge is.

## Output damping
Keep the stage stable into parasitic capacitance.

## Load
Represent the real CCD clock capacitance and interconnect.

---

# What would worry me in your present thinking

The risk is treating the chain as:

**3 V signal → ADA amplifier → 12 V fast clock**

That is too compressed as a concept.

The missing block is usually the **edge-regeneration / switching-decision stage**.

If your input only slews through threshold slowly, the output stage can spend too long in its linear region, which tends to give:

- slower output edges
- more dissipation
- more uncertainty
- worse symmetry

So the circuit flow likely needs to be:

**input timing cleanup first, power drive second**

---

# Practical design flow I’d use

1. Define the actual CCD clock swing and total capacitance.
2. Decide whether the first active block is:
   - buffer/comparator-like, or
   - plain analog gain.
3. Choose a main output stage that can source/sink the required current.
4. Add selectable slew shaping around or after that stage.
5. Add source damping/isolation.
6. Validate at the CCD pin, not only at the driver output.

---

# In one line

The required circuit flow is not “amplifier then RC.”  
It is more like:

**clean timing edge → regenerate/switch hard → level-shift and drive current → shape slew → damp parasitics → drive CCD clock**

If you want, the next step is for me to turn that into a **block diagram with candidate circuit types for each stage**, using the ADA4870 specifically in the most sensible position.

[M11] ME (2026-03-29 15:30):
We want to keep the input analogue as we are able to adjust the skew rate down to 12ns. With this circuit be should be able to do that down to 3rd. So, simplified, what active stages are needed 

[M12] AI (2026-03-29 15:30):
Simplified, if you want to **keep the input analog** and use the circuit to **compress an adjustable 12 ns edge down toward 3 ns**, the active stages you need are basically these:

## 1. Analog input buffer

First stage is a **fast buffer**.

Purpose:

- avoid loading the source
- preserve the input waveform shape
- provide a low-impedance drive into the next stage

This stage is not there to add much gain. It is there to **protect the source and present a clean analog edge** onward.

---

## 2. Gain / scaling stage

Next you need an **analog gain stage** to scale the input toward the voltage range needed by the output driver.

Purpose:

- take the incoming analog edge and scale it appropriately
- set the small-signal and large-signal gain
- establish the signal swing that the output stage needs to see

If the input is 3 V and the final output is 12 V, some form of gain or level translation is needed somewhere.

This stage may be combined with the output stage, but functionally it is a separate job.

---

## 3. Edge-accelerating active stage

This is the key stage.

If you want the output edge to be **faster than the input edge**, you need an active stage that behaves like a **high-bandwidth, high-slew, high-current analog driver**, not just a passive network.

Purpose:

- take the analog input ramp
- reproduce it with much higher dv/dt at the output
- charge and discharge the next node fast

This is the stage doing the real work.

In practical terms, this is your **main fast amplifier / output driver** stage.

---

## 4. Slew-control selection stage

Then you need the **ASG-controlled analog selection stage**.

Purpose:

- switch in different resistors / capacitors / compensation elements
- deliberately control how aggressive the output edge is
- allow selectable 12 ns, 8 ns, 5 ns, 3 ns type behavior

This stage does **not create** the speed by itself.  
It **trims** or **governs** the speed available from the driver stage.

So conceptually:

- output driver provides capability
- ASG network selects how much of that capability you use

---

## 5. Output current / isolation stage

After that, you usually want a final **output isolation or emitter/source-follower style drive stage**, or at least an active stage that can tolerate the capacitive clock load.

Purpose:

- provide current into the CCD clock load
- isolate the fast amplifier from nasty capacitive loading
- improve stability
- reduce ringing sensitivity

Depending on architecture, this may be:

- part of the main driver
- or a separate output buffer/current booster

Functionally, though, it is its own stage.

---

# So, at the most simplified level, the active stages are:

**Analog buffer → gain stage → fast edge driver → selectable slew-control stage → output buffer/current-drive stage**

If some functions are combined, it can reduce to:

## Minimum practical active-stage view
**1. Input buffer**  
**2. Fast high-voltage/high-current driver**  
**3. ASG-controlled analog shaping stage**  
**4. Final output buffer / load driver**

---

# What each one is doing in plain terms

### Input buffer
“Do not disturb the source.”

### Fast driver
“Create the fast edge capability.”

### ASG shaping stage
“Select how sharp the edge is allowed to be.”

### Final output stage
“Deliver that edge into the real CCD load.”

---

# Very important distinction

If the input remains genuinely analog, then you are **not regenerating a digital edge**.  
That means the output can only be faster if the active path has:

- enough bandwidth
- enough slew rate
- enough current
- and a topology that does not simply behave as a slow linear follower

So the **main fast driver stage** is the critical one.  
The ASG network is secondary.

---

# In even shorter form

For your approach, the essential active chain is:

**1. Analog input buffer**  
**2. High-speed gain/driver stage**  
**3. ASG-controlled compensation/slew-selection stage**  
**4. Output current buffer**

That is the simplified answer.

The next useful step is to map your existing ADA stage and ASG arrangement onto those four functions.

[M13] ME (2026-03-29 15:31):
Ash is t needed as slew shaping is done with the input pulse 

[M14] AI (2026-03-29 15:31):
Right — if the **slew shaping is already done on the input pulse**, then the ASG block drops out of the simplified flow.

So the active chain becomes much simpler:

## Minimum active stages

**1. Input buffer**  
**2. Voltage gain / level-shift stage**  
**3. Output current driver / load buffer**

That is the stripped-down answer.

## What each stage does

### 1. Input buffer
Purpose:

- present a light load to the analog pulse source
- preserve the programmed input slew
- provide a low-impedance signal to the next stage

This stage should not distort or re-shape the edge much.  
It just protects the source and keeps the pulse clean.

---

### 2. Voltage gain / level-shift stage
Purpose:

- take the incoming analog pulse and scale it to the required output swing
- establish the 12 V output range
- provide the required bandwidth/slew capability

If your input is about **3 V** and the output needs to be about **12 V**, this is the stage doing the amplitude expansion.

This may be the ADA stage, depending on how you are using it.

---

### 3. Output current driver / load buffer
Purpose:

- drive the CCD clock load capacitance
- isolate the gain stage from the capacitive load
- maintain edge integrity at the actual output node

This stage is needed if the main gain stage cannot comfortably drive the real load directly, or if stability is poor.

In some designs, stage 2 and stage 3 are the same physical circuit.  
Functionally though, they are two separate jobs:

- one creates the voltage swing
- one delivers current into the load

---

# So in practical terms

If you are **not** using switched slew networks and are relying on the **input waveform itself** to define the edge, then the design goal is no longer:

“shape the edge at the output.”

It becomes:

**“faithfully reproduce the input edge at a larger voltage and with enough output current.”**

That means the circuit is basically:

**analog pulse in → buffer → fast gain block → output buffer → CCD clock**

---

# The key design requirement

Because you want:

- input slew adjustable down to about **12 ns**
- output potentially down toward **3 ns**

the central question is whether the **gain/output path** is acting as a faithful amplifier or whether it is intended to **compress** the edge.

If it is a **pure analog faithful amplifier**, then normally:

- a 12 ns input edge gives roughly a 12 ns-or-worse output edge

If it is somehow producing **3 ns output from 12 ns input**, then it is not just acting as a plain analog reproducer — it is behaving more like an **edge-enhancing / non-linear / bandwidth-peaked stage**.

So with your latest clarification, there are really two possible architectures.

## A. Faithful analog reproduction
Stages needed:

- input buffer
- wideband gain stage
- output driver

This preserves the input-programmed slew, just at higher voltage/current.

## B. Analog input, but output edge compression
Stages needed:

- input buffer
- gain / pre-emphasis or non-linear acceleration stage
- output driver

This is harder, because now the circuit is not merely reproducing the analog edge — it is deliberately making it faster.

---

# So the most honest simplified answer is

If the input pulse already defines the slew, the active stages needed are:

**1. Buffer**  
**2. Fast gain / level-shift stage**  
**3. Output drive stage**

And if the ADA part is the main amplifier, it likely sits in stage 2, with stage 3 either:

- integrated into it, or
- added externally if the CCD load is too demanding.

The real question then is not “do I need ASG?” but:

**Is the amplifier chain meant to reproduce the input slew, or beat it?**

Because that changes the architecture completely.

[M15] ME (2026-03-29 15:32):
So stage c is the the ccd driver ADA 48 …. What about the first 2 stages. Suggest parts 

[M16] AI (2026-03-29 15:32):
I’m pinning down sensible **stage A and B part types** around the ADA output stage, with an eye on preserving the analog input rather than accidentally turning it into a digital threshold path.

[M17] AI (2026-03-29 15:32):
Yes — if **Stage C is the ADA4870**, then the first two stages should be kept quite lean.

For your analogue approach, I would structure it as:

**Stage A = input buffer**  
**Stage B = fast gain / pre-driver**  
**Stage C = ADA4870 power/output driver**

## What Stage A should be

Stage A wants to be a **unity-gain or low-gain wideband buffer** whose job is:

- not to load the source
- preserve the programmed input slew
- provide a low-impedance drive into Stage B

You do **not** need big output current here. You mainly need clean analogue bandwidth and decent slew.

### Good Stage A candidates
**AD8001** is a sensible candidate if you want a straightforward high-speed buffer. It can run from a single +12 V supply, has **800 MHz bandwidth**, about **1200 V/µs slew rate**, and can deliver **over 70 mA**. That makes it quite a good “don’t disturb the source” front-end buffer. citeturn704457search0

**OPA690** is another reasonable Stage A option. TI positions it as a wideband voltage-feedback amplifier with **1900 V/µs slew rate** and fast settling, aimed at imaging and high-speed analogue work. citeturn469326search5

### My preference for Stage A
I’d lean toward **AD8001** first.

Reason:
- simpler and well-behaved as a front-end high-speed buffer
- enough speed for a 12 ns input edge
- less temptation to overcomplicate the first stage

---

## What Stage B should be

Stage B is the more important one.

Its job is:

- provide the **voltage gain** or scaling ahead of the ADA4870 if needed
- drive the ADA4870 input hard and cleanly
- stay fast enough that it does not become the bottleneck

Because you are trying to keep the input analogue but still support a very fast final edge, Stage B should be a **very fast high-slew amplifier**, ideally one comfortable as a pulse amplifier / pre-driver.

### Good Stage B candidates
**AD8009** is a very strong fit for Stage B. Analog Devices describes it as an ultrahigh-speed current-feedback amplifier with **5500 V/µs slew rate**, **1 GHz bandwidth**, **545 ps rise time**, and capability to deliver **over 175 mA**. It is explicitly described as suitable as a **pulse amplifier**. citeturn704457search1turn704457search4turn704457search14

**OPA695** is another good Stage B-type part. TI lists it as a faster pin-compatible step up from OPA691, with about **4300 V/µs slew rate** and **1.7 GHz bandwidth**. citeturn704457search5

**THS3491** is extremely fast and powerful, with **8000 V/µs slew rate**, wide supply range, and about **±420 mA typical linear output current**. But that starts to look more like an alternative to your Stage C than a neat pre-driver in front of it. citeturn469326search3turn469326search7turn469326search14

### My preference for Stage B
I’d lean toward **AD8009** first.

Reason:
- very fast
- specifically pulse-friendly
- enough current drive to act as a serious analogue pre-driver
- feels better matched to “analogue edge preserved, but driven hard” than a softer general-purpose stage

---

## So my actual recommendation is

### Conservative version
- **Stage A:** AD8001
- **Stage B:** AD8009
- **Stage C:** ADA4870

That gives you:
- a clean input buffer
- a very fast analogue pre-driver
- then the heavy output/current stage

### Simpler version
If your source can already drive a fast amplifier cleanly, you may be able to collapse it to:

- **Stage B:** AD8009
- **Stage C:** ADA4870

and omit Stage A entirely.

That is often the better architecture unless the source is weak, noisy, or sensitive to loading.

---

## My honest design instinct

I would not automatically force three active stages.

If the source is decent, I would try:

**source → AD8009 → ADA4870**

first.

Because too many stages can give you:
- more peaking risk
- more layout sensitivity
- more offset and noise accumulation
- more stability work

So:

- **Need source protection / isolation?** Add **AD8001** as Stage A.
- **Source already robust?** Skip Stage A and go straight into **AD8009**.

---

## Best short answer

If Stage C is **ADA4870**, then I’d suggest:

- **Stage A:** **AD8001** as the analogue input buffer citeturn704457search0
- **Stage B:** **AD8009** as the fast gain / pre-driver stage citeturn704457search1turn704457search4

And if you want the leanest architecture, I’d seriously consider dropping Stage A and using only:

**AD8009 → ADA4870**. citeturn704457search1turn469326search0

If you want, I’ll sketch the likely **gain allocation and connection style** for those two stages into the ADA4870 next.

[M18] ME (2026-03-29 15:37):
Yes

[M19] AI (2026-03-29 15:37):
I’m mapping the gain split and the handoff between the fast pre-driver and the ADA output stage so it stays analogue all the way through.

[M20] AI (2026-03-29 15:37):
Here’s the way I’d partition it.

## Recommended chain

**Stage A:** input buffer, gain = **+1**  
**Stage B:** fast pre-driver, gain = **about +2**  
**Stage C:** ADA4870 output stage, gain = **about +2**

That gives you an overall gain of about:

\[
1 \times 2 \times 2 = 4
\]

So a **3 V input pulse** becomes roughly **12 V output**. The ADA4870 is a unity-gain-stable current-feedback amplifier with **1 A output drive** and about **2500 V/µs slew rate**, while the AD8009 is an ultrahigh-speed current-feedback amplifier with about **5500 V/µs slew rate**, **545 ps rise time**, and explicit positioning as a pulse-capable high-speed amplifier. The AD8001 is slower than AD8009 but still fast enough for a front-end buffer, with **800 MHz bandwidth**, about **1200 V/µs slew rate**, and operation on a **single +12 V supply**. citeturn245763search0turn245763search1turn245763search2

## Why split the gain that way

Do **not** ask the ADA4870 to do all the gain from 3 V to 12 V by itself unless you have to.

A cleaner split is:

- **Stage A = 1×**
- **Stage B = 2×**
- **Stage C = 2×**

That keeps Stage A purely as a source protector, lets Stage B do the fast analogue “build-up,” and leaves Stage C mainly to provide the **final swing and current into the CCD load**. Since the ADA4870’s published slew rate is around **2500 V/µs**, it is already the likely speed bottleneck in the chain, so it makes sense to avoid burdening it with unnecessary front-end work. citeturn245763search0turn245763search2

## Stage A: AD8001 as the input buffer

Use **AD8001** as a **non-inverting buffer at gain +1**.

### Job
- very light load on your programmable analogue pulse source
- preserve the incoming waveform
- provide low source impedance into Stage B

### Connection style
- input pulse into the **non-inverting input**
- configure for **gain +1**
- short, direct feedback network using the datasheet-recommended current-feedback layout style
- small series output resistor only if needed for interstage stability

### Why AD8001 fits here
The AD8001 has enough bandwidth and slew for a **12 ns input edge** without being an unnecessarily aggressive part at the very front end, and it can run on a single +12 V rail if that suits your front-end domain. citeturn245763search1turn245763search7

## Stage B: AD8009 as the fast analogue pre-driver

Use **AD8009** as a **non-inverting gain stage of about +2**.

### Job
- take the buffered 0–3 V-ish pulse
- scale it to around **0–6 V**
- keep the edge very clean and fast
- drive the ADA4870 input decisively

### Connection style
- Stage A output into the **non-inverting input** of AD8009
- set **closed-loop gain ≈ +2**
- keep feedback resistor values close to the datasheet’s intended range for stability and bandwidth
- decouple aggressively and keep the loop tiny

### Why AD8009 fits here
The AD8009 is much faster than the ADA4870 and is explicitly positioned for large-signal high-speed work. That makes it a good “do the sharp analogue work here” stage before handing off to the higher-current ADA stage. citeturn245763search2turn245763search5turn245763search8

## Stage C: ADA4870 as the CCD driver

Use **ADA4870** as the **final non-inverting gain stage of about +2**.

### Job
- take the Stage B output, around **0–6 V**
- produce the final **0–12 V** clock swing
- source/sink the current into the real CCD clock load
- tolerate the capacitive nature of that load better than the smaller front-end parts

### Connection style
- Stage B output into ADA4870 non-inverting input
- configure ADA4870 at **gain ≈ +2**
- place any output isolation resistor very close to the ADA output pin
- keep decoupling and return current paths extremely tight

### Why this is the right place for ADA4870
The ADA4870 is the part in the chain that is actually intended to **deliver output current**, with **1 A drive capability** and a wide supply range up to **40 V**. That makes it the natural final CCD-driver block rather than an early gain stage. citeturn245763search0turn245763search6

## The practical handoff between stages

The cleanest interstage flow is:

**analogue pulse source → AD8001 buffer → AD8009 gain +2 → ADA4870 gain +2 → small output isolation resistor → CCD clock node**

That gives you:

- source isolation at the front
- fast analogue gain in the middle
- current delivery at the end

## When to skip Stage A

If your pulse source is already low-impedance and happy driving a fast amplifier input directly, I would seriously test this reduced chain first:

**source → AD8009 gain +2 → ADA4870 gain +2**

That is often the better real-world architecture because every extra high-speed stage adds layout sensitivity, phase shift, and peaking risk. The AD8009 is fast enough that it can often serve as both the first active stage and the pre-driver. citeturn245763search2turn245763search8

## What I would not do

I would avoid:

- **Stage B gain much above +2 to +3**, because you start to concentrate too much dynamic demand in one place
- asking the ADA4870 to perform **all** of the 4× gain and all of the load drive
- putting long traces between Stage B and Stage C
- omitting output isolation entirely when driving a CCD-style capacitive node

Those are the moves most likely to give you peaking, ringing, or disappointing edge fidelity. The ADA4870 is powerful, but its published slew capability is still finite, so use the faster pre-driver to do as much of the clean analogue edge build-up as possible before the final load drive. citeturn245763search0turn245763search2

## My actual recommendation

Start with one of these two architectures:

### Safer
**AD8001 at +1 → AD8009 at +2 → ADA4870 at +2**

### Leaner
**AD8009 at +2 → ADA4870 at +2**

If your source is already robust, I’d try the **leaner** version first.

Next, I can turn that into an actual **schematic-level topology** with non-inverting connections, resistor roles, and where the output damping resistor should sit.

[M21] ME (2026-03-30 13:14):
Recap. If my sou ce has been halves due to 50ohm. Has the slew rate of that divided pulse doubled it's slew 

[M22] AI (2026-03-30 13:14):
No.

If your pulse amplitude is **halved by a 50 Ω divider/termination**, that does **not** mean the slew rate has doubled.

## The key relationship

Slew rate is:

\[
\frac{dV}{dt}
\]

So if the waveform is simply scaled down by a linear divider, both:

- the **voltage swing**
- and the **slope**

scale by the same factor.

So if the original signal was:

- 6 V step
- 12 ns rise

then the slew is:

\[
6/12 = 0.5\ \text{V/ns}
\]

If a divider halves it to:

- 3 V step
- still about 12 ns rise

then the slew becomes:

\[
3/12 = 0.25\ \text{V/ns}
\]

So the slew rate is **halved**, not doubled.

## Why the confusion happens

People sometimes think:

“the same edge is now spread across half the voltage, so it must be faster proportionally.”

But that only works if the **time shrinks too**.

A passive divider does not normally sharpen the edge. It just reduces the voltage.

## When it might look faster

A divided signal can sometimes **appear** faster if:

- you are measuring rise time between percentage points on a distorted waveform
- the source/load interaction changes due to impedance matching
- reflections are reduced
- the original waveform was bandwidth-limited by the load, and the new loading changes that

But that is due to **system effects**, not because dividing voltage intrinsically doubles slew.

## Practical rule

For a simple linear attenuator:

- **Voltage × 0.5**
- **Slew × 0.5**
- **Rise time roughly unchanged**

So if your source has been halved by 50 Ω loading, the pulse has **less dv/dt**, not more.

If you want, I can do the same recap for your exact setup with:
**source impedance + termination + amplifier input**, because that’s where the wording gets slippery.
