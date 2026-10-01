# Over-volting a PC fan
Date (UTC): 2025-11-12 17:47
Conversation ID: 6914c81c-2568-8329-adf7-517b2e244b00
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-001.json

[M1] ME (2025-11-12 17:47):
Can you briefly over volt a pc
Fan

[M2] AI (2025-11-12 17:47):
Yes — **you can briefly over-volt a PC fan**, but only **within a small and carefully controlled margin**, and **only for a short duration**. Here’s the key detail:  

- **Typical voltage range:**  
  - Standard PC fans are rated for **12 V DC** (some smaller ones for 5 V).  
  - They often tolerate **up to about 13.2–13.8 V** safely (≈ 10–15 % over-voltage).  

- **Effects:**  
  - **Slightly higher speed** → more airflow and noise.  
  - **Much higher voltage (>14 V)** → current and heat rise quickly, possibly damaging the motor driver IC or bearings.  
  - **Brief spikes** (e.g., 13 V for a few seconds) usually fine; **sustained over-voltage** shortens life dramatically.  

- **Safe practice:**  
  - If testing, use a **bench supply** with current limit set.  
  - Increase voltage slowly while monitoring current and fan noise/temperature.  
  - Never exceed **+15 % of rated voltage** even briefly if you care about the fan.  

Would you like me to estimate what happens (current draw, RPM increase, and risk) for a specific fan model and voltage, e.g., 12 V → 15 V?
