# Active Low with -5V
Date (UTC): 2026-04-02 13:05
Conversation ID: 69ce69a9-f59c-838d-9342-3945fa8d91b1
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-007.json

[M1] ME (2026-04-02 13:05):
So what does active low referenced to negative 5v means?

[M2] AI (2026-04-02 13:05):
It means the signal is considered **“asserted” when it goes low relative to the -5 V rail**, not relative to 0 V ground.

So in practice:

- If the logic reference is **-5 V**
- then **“low” = near -5 V**
- and **“high” = some voltage above -5 V**

Example:

- **-5 V** → logic low / active state
- **0 V** → logic high / inactive state

Why this matters:
A lot of circuits assume logic is referenced to **0 V ground**, where low is near 0 V and high is +3.3 V or +5 V. But if something is **referenced to -5 V**, the whole logic swing is shifted.

So a signal swinging from:

- **-5 V to 0 V**

could be treated like a normal logic signal, just offset downward by 5 V.

“Active low” specifically means:

- the function happens when the signal is at its **low level**
- and in this case that low level is **near -5 V**

So an **enable** pin described that way would mean:

- **-5 V = enabled**
- **0 V = disabled**

unless the datasheet defines a different threshold window.

If you’ve got the exact pin description or datasheet wording, send it over and I’ll decode exactly what voltage range it expects.

[M3] ME (2026-04-02 13:07):
And I can take that to -15v right?

[M4] ME (2026-04-02 13:07):
4870

[M5] AI (2026-04-02 13:07):
I’m checking the ADA4870 threshold wording so I can answer against the actual pin spec rather than guess from memory.

[M6] AI (2026-04-02 13:07):
Not on that pin, no.

For the **ADA4870 ON pin**, the datasheet defines the logic relative to **VEE**, not as an arbitrary negative input you can keep extending downward. The valid ranges are:

- **Low / enabled:** **VEE to VEE + 1.3 V**
- **High / power-down:** **VEE + 1.8 V to VEE + 5 V** citeturn351391search1turn351391search0

So if your negative rail **VEE = -5 V**, then:

- **enabled low** = about **-5 V to -3.7 V**
- **power-down high** = about **-3.2 V to 0 V** citeturn351391search1turn351391search0

That means **taking it to -15 V would be 10 V below VEE**, which is **not** what “active low referenced to -5 V” means. It means the pin’s low state sits **near the negative rail**, not “any more negative voltage is fine.” The ADA4870 supply range itself is **10 V to 40 V total**, so with a ±5 V setup the negative rail is already at **-5 V**. citeturn351391search0turn351391search1

So the practical answer is:

- **If VEE = -5 V, drive the ON pin to about -5 V for low/enabled**
- **Do not drive it to -15 V** citeturn351391search1turn351391search0

If you want, I can also decode the **SD pin** and the difference between **ON**, **SD**, and **TFL** on the 4870, because those three are easy to mix up.

[M7] ME (2026-04-02 13:08):
My ever is 15v

[M8] AI (2026-04-02 13:08):
I’m mapping it to your actual rails now. With VEE at -15 V, the logic window shifts down with it.

[M9] AI (2026-04-02 13:08):
Then **“active low referenced to VEE” means referenced to -15 V in your case**.

So for the **ADA4870 ON pin**:

- **logic low / enabled** = **VEE to VEE + 1.3 V**
- **logic high / shutdown** = **VEE + 1.8 V to VEE + 5 V** citeturn840926search0turn840926search1

With **VEE = -15 V**, that becomes:

- **enabled low:** about **-15 V to -13.7 V**
- **shutdown high:** about **-13.2 V to -10 V** citeturn840926search0turn840926search1

So in that setup:

- **-15 V is a valid low**
- **0 V is not the intended logic high for that pin**
- and the control signal should live in that **window above VEE**, not ground-referenced logic. citeturn840926search0turn840926search1

The other important limit is that the device’s **common-mode/input-related voltages are specified between VEE and VCC**, so you should not treat the control pin as tolerant of arbitrary voltages outside the rails. citeturn840926search0turn840926search1

So yes: **if your negative rail is -15 V, pulling ON to -15 V is the “active low” state.**

If you tell me what your **VCC** is and what logic source is driving it, I’ll map out a clean interface circuit.

=== ALTERNATE BRANCHES (edited/regenerated messages not on the final thread) ===

[A1] AI (2026-04-02 13:07):
Usually **no** — not unless the datasheet explicitly allows it.

If a pin is described as:

- **active low**
- **referenced to -5 V**

that does **not** mean “pull it as negative as you like.”

It normally means the logic thresholds are defined around a signal range such as:

- low near **-5 V**
- high near **0 V**

So taking it to **-15 V** may:

- exceed the pin’s **absolute maximum rating**
- forward-bias protection structures
- damage the input
- cause latch-up or strange behaviour

The key thing to check is:

1. **Absolute input voltage range**
2. **Logic threshold spec**
3. Whether the input is **clamped** to internal rails

A common situation is:
- valid logic swing = **-5 V to 0 V**
- absolute max maybe a bit beyond that, for example **V- - 0.3 V** or similar
- but **not** down to **-15 V**

So the safe assumption is:

- **active low referenced to -5 V = drive it low to about -5 V**
- **do not take it to -15 V unless the datasheet clearly says that is allowed**

If you paste the exact part number or the input spec line, I’ll tell you whether -
