# Radiation Effects on Sensors
Date (UTC): 2026-06-25 11:28
Conversation ID: 6a3d1094-a3ec-83ed-9dfc-d37567525676
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-008.json

[M1] ME (2026-06-25 11:28):
When powering a sensor for radiation testing from our own source is the potential for fast voltage spikes and droops happening due to radiation. X rays, neutron. Someone has mentioned that they don’t know why this is being requested, but may be thinking of it from a heavy ion only perspective 

[M2] AI (2026-06-25 11:28):
I’ll frame this technically rather than as a generic “power quality” concern: the key distinction is whether the source is being specified for **SEE/transient capture**, **TID/displacement testing**, or simply **safe biased operation during irradiation**.

[M3] AI (2026-06-25 11:28):
Yes — the request is technically defensible, but it needs wording carefully so it does not sound like you are claiming the **external PSU itself** will be hit by radiation and produce spikes. The real concern is usually this:

> Radiation can cause **the powered sensor or its nearby electronics** to draw sudden transient current, latch up, leak more, reset, or disturb internal nodes. If the supply path is not well controlled, those current events can appear as **fast local voltage droops, overshoots, rail ringing, or supply-borne disturbances** at the DUT.

So the request is not just “heavy ion test thinking”. It is broader than that.

For **heavy ions**, the concern is obvious: single-event effects can cause transient currents, single-event transients, latch-up, burnout mechanisms, or sudden leakage changes. ESA/ECSS guidance explicitly treats single-event effects as arising from particles such as protons, neutrons and heavy ions, with transient and potentially destructive effects included. citeturn692616search4

For **neutrons**, it is also valid. Neutrons are commonly considered in SEE/soft-error testing, particularly for terrestrial/atmospheric or avionics-type environments. JESD89-related literature refers to neutron and proton testing for SEE cross-section measurement, and neutron-induced effects have been demonstrated in complex digital devices and sensors. citeturn692616search11turn692616academia29

For **X-rays**, the mechanism is usually less about single-particle SEE and more about **ionising dose effects**, photocurrent, leakage change, threshold shift, upset/reset sensitivity, or analogue performance drift. During irradiation, a biased sensor can show changing current demand or functional disturbance. That may not create nanosecond-level rail spikes in the same way as a heavy-ion SET/SEL event, but it can still cause **bias rail movement, droop, recovery artefacts, or false test conclusions** if the supply is not stable and monitored.

A good way to respond to the objection would be:

> The request is not based solely on a heavy-ion SEE perspective. When the DUT is powered from our own source during irradiation, radiation-induced changes in DUT current demand, leakage, latch-up, transient charge collection, resets, or functional state changes can couple into the local supply rails. Depending on the source impedance, cable length, decoupling, current limiting and measurement bandwidth, these events may appear as fast voltage droops, overshoots or rail disturbances at the sensor. This is relevant for heavy-ion SEE testing, but also for neutron-induced single-event effects and X-ray/TID-biased operation where leakage, photocurrent or functional disturbance may change the rail loading.

I would separate the requirement into three parts:

**1. Supply quality requirement**  
The DUT supply should be low-noise, low-impedance and appropriately decoupled at the sensor, with current limit behaviour understood. Long supply leads, remote PSU sense instability, poor local capacitance, or aggressive current limiting can turn a DUT transient into a rail transient.

**2. Monitoring requirement**  
Monitor both **voltage at the DUT** and **current from the source**. Voltage at the DUT tells you what the sensor actually experienced; current tells you whether the DUT drew an abnormal transient or latch-up-like current. For radiation testing, this distinction is important because a recorded failure could be caused by the DUT response, the power delivery network response, or both.

**3. Event correlation requirement**  
If possible, time-correlate voltage/current anomalies with irradiation events, shutter state, fluence count, mode changes, resets, and sensor data errors. Otherwise, you may see a sensor upset and not know whether it was a radiation-induced internal fault, a supply droop, a latch-up event, or a test-system artefact.

The strongest technical wording is probably:

> We are not assuming the PSU will generate radiation-induced spikes. The concern is that radiation-induced activity in the biased DUT may create fast load-current transients or leakage changes, and the power-distribution network may convert those into local voltage droops, overshoot or ringing at the sensor. Therefore the supply path should be characterised, locally decoupled, and monitored at the DUT during X-ray, neutron and heavy-ion exposure.

That should address the “why is this being requested?” point without overstating the physics.

[M4] ME (2026-06-25 11:32):
So there could be a case where finite transient voltage doesn’t produce a fine current draw. They are keen see voltage in GHz but ok with current being 50khz

[M5] AI (2026-06-25 11:32):
Yes — that can absolutely happen.

A **fast transient voltage event** at the DUT rail does **not necessarily imply a correspondingly measurable fast current event** in the PSU/current monitor, especially if the current measurement bandwidth is only **50 kHz** while the voltage measurement is being observed into the **GHz range**.

The important distinction is:

> A GHz-bandwidth voltage measurement can see local rail behaviour at the DUT.  
> A 50 kHz current measurement mostly sees the averaged or envelope current drawn from the source.

So the two measurements are not equivalent.

A fast voltage spike or droop can be caused by:

**Local charge redistribution**  
Radiation can disturb charge inside the sensor or nearby electronics. That can create a fast voltage movement locally without immediately appearing as a large current change at the remote supply.

**Decoupling capacitors supplying the event**  
A transient load may be supplied by local capacitance near the DUT. The PSU only replenishes that charge later, so the PSU current monitor sees a slower recovery current rather than the original fast pulse.

**Power-distribution-network impedance**  
Cable inductance, plane inductance, connector impedance and decoupling ESR/ESL can convert a very short current impulse into a voltage disturbance. The voltage transient may be visible locally even when the source-current monitor averages it away.

**Common-mode or pickup artefacts**  
A GHz voltage probe can also see radiated pickup, ground bounce, cable resonance, probe-loop artefacts or local electromagnetic coupling. That does not always represent a true conducted current transient from the PSU.

**Bandwidth mismatch**  
A 50 kHz current monitor has a timescale of roughly microseconds to tens of microseconds. It will not resolve nanosecond-scale current impulses. It may show only a small blip, a delayed recovery, or nothing obvious at all.

So the position I would take is:

> It is reasonable to monitor voltage with very high bandwidth if the aim is to detect fast local rail disturbances at the sensor. However, a 50 kHz current measurement cannot be used to prove that no fast current transient occurred. It only proves that no large low-frequency or sustained current change was observed.

That is probably the key technical rebuttal.

A good way to phrase it to them:

> The voltage and current measurements are answering different questions. GHz-bandwidth voltage probing can detect fast local rail disturbances at the DUT, including droop, overshoot, ringing or pickup caused by radiation-induced events or PDN response. A 50 kHz current monitor is still useful for detecting sustained leakage increase, latch-up, current-limit behaviour or slower recovery effects, but it will not capture nanosecond-scale transient current. Therefore, absence of a fast current signature at 50 kHz does not rule out a fast voltage transient at the DUT.

In practical terms, I would define the measurement intent like this:

| Measurement | Bandwidth | What it can prove |
|---|---:|---|
| DUT rail voltage probe | MHz–GHz | Fast droop, overshoot, ringing, reset-level disturbances, local rail integrity |
| Source current monitor | ~50 kHz | Sustained current rise, latch-up, leakage increase, slow transients, average load change |
| Fast current probe / shunt | MHz–GHz if needed | Actual fast transient current signature |

So if they are “keen to see voltage in GHz but okay with current being 50 kHz”, that is defensible **only if they understand the limitation**:

> It is fine for the current channel to be slower if its purpose is latch-up/leakage/fault monitoring. It is not fine if they intend to correlate every GHz voltage spike with a measured fast current pulse, because the current channel will be blind to those events.

The strongest recommendation would be:

> Keep the GHz voltage monitoring for local rail disturbance detection. Keep the 50 kHz current monitoring for protection and slower fault classification. Add a fast local current-sense option only if the test objective requires proving whether a specific voltage transient was caused by a conducted current impulse rather than pickup, PDN resonance or local charge effects.

That gives you a clean technical compromise: high-speed voltage is justified, slower current is still useful, but they are not interchangeable.
