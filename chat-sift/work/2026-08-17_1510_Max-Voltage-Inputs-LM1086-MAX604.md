# Max Voltage Inputs LM1086 MAX604
Date (UTC): 2026-08-17 15:10
Conversation ID: 6a83241b-0544-83eb-8162-7ab1dd01abcd
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-008.json

[M1] ME (2026-08-17 15:10):
What’s the maximum voltage inputs for the following 
Lm1086is-(3.3/5.0/adj)
Max604

[M2] AI (2026-08-17 15:10):
I’ll check the actual datasheet limits, because these two are specified differently: the LM1086 is mainly limited by **input-to-output differential**, whereas the MAX604 has a direct **VIN absolute maximum**.

[M3] AI (2026-08-17 15:10):
For the **LM1086IS family** and **MAX604**, there’s an important distinction between the **guaranteed operating input range** and the **absolute maximum**.

| Device | Normal/guaranteed max input | Absolute maximum |
|---|---:|---:|
| **LM1086IS-3.3** | **18 V** | **27 V input-to-output differential** |
| **LM1086IS-5.0** | **20 V** | **25 V input-to-output differential** |
| **LM1086IS-ADJ** | **15 V max differential for specified regulation** | **29 V input-to-output differential** |
| **MAX604** | **11.5 V VIN** | **12 V VIN** |

TI specifies the LM1086-3.3 over **4.75–18 V input** and the LM1086-5.0 over **6.5–20 V input**. The absolute limits are stated as \(V_{IN}-V_{OUT}\): 27 V for the 3.3 V version, 25 V for the 5 V version, and 29 V for the adjustable version. citeturn715755view0

So for actual circuit design, I'd treat **18 V and 20 V as the useful maximums** for the fixed LM1086 versions rather than designing anywhere close to the absolute differential ratings. Also remember that **thermal dissipation normally becomes the limiting factor long before voltage does**; e.g. dropping 20 V to 5 V at 1 A means the regulator has to dissipate about **15 W**. citeturn715755view0

For the **MAX604**, it's much simpler: Analog Devices/Maxim gives an operating supply range of **2.7–11.5 V**, with **12 V absolute maximum** from IN to ground. citeturn126763view1

If you're looking at these for your **15 V rail circuitry**, the distinction matters a lot: **15 V is comfortable for an LM1086, but already beyond the MAX604's absolute maximum.**
