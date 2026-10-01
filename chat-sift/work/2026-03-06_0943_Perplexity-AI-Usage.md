# Perplexity AI Usage
Date (UTC): 2026-03-06 09:43
Conversation ID: 69aaa19b-dcfc-838b-a0aa-06a9f9c2deab
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-03-06 09:43):
What is perplexity so used for?

[M2] AI (2026-03-06 09:43):
**entity["software","Perplexity AI","AI search engine"]** is primarily used as an **AI-powered research and answer engine**. Think of it as a hybrid between **a search engine (like entity["software","Google Search","web search engine"])** and **a conversational AI assistant (like entity["software","ChatGPT","OpenAI conversational AI"])**.

Instead of returning a list of links, it **reads sources across the web and synthesizes an answer**, while **citing the sources it used**.

Below are the main ways people actually use it.

---

## 1. Research With Source Citations
This is the **core use case**.

You ask a question, and it:
1. Searches the web in real time  
2. Reads multiple sources  
3. Produces a summarized answer  
4. Shows the citations

Example query:
- *“What are the limitations of LVDS at 200 MHz over cable?”*

Perplexity will return:
- a synthesized explanation
- links to datasheets / papers / forum posts

This is why it’s popular for:
- academic research  
- technical investigation  
- verifying claims

It behaves more like **an intelligent research assistant** than a chatbot.

---

## 2. Fast Technical Investigation
Engineers use it heavily because it can quickly scan:

- datasheets
- forums
- papers
- application notes
- documentation

Example engineering queries:
- “Maximum LVDS cable length at 400 Mbps”
- “Difference between MSOP and TSSOP packages”
- “SPI timing constraints for 74HC595”

Instead of manually opening **10 search results**, it extracts the key information.

---

## 3. Current / Real-Time Information
Unlike many AI chat models that rely on training data, Perplexity is **live-search driven**.

So it works well for:
- latest news
- new products
- current pricing
- company information
- software updates

---

## 4. Deep Web Summaries
It can ingest long content like:

- research papers
- blog posts
- documentation
- PDFs

and produce **short explanations or bullet summaries**.

Example:
> “Summarize this 40-page FPGA whitepaper.”

---

## 5. Follow-Up Research Conversations
You can refine questions interactively.

Example chain:

1. “What is LVDS?”  
2. “What limits its cable length?”  
3. “What cable type works best at 1 Gbps?”  

It keeps the **context of the investigation**.

---

## 6. Focused Search Modes
Perplexity has modes like:

- **Academic** – prioritizes papers
- **Writing** – helps produce text
- **Coding** – focuses on developer sources
- **Web** – general search

---

## The Key Difference vs Normal Search

| Tool | What it returns |
|---|---|
| Google | List of links |
| ChatGPT | Synthesized answer (not always live web) |
| **Perplexity** | Synthesized answer **with live citations** |

---

## The Name “Perplexity”
The name comes from the **AI metric “perplexity”** used in language models.

In machine learning:

**Perplexity = how well a model predicts text.**

Lower perplexity → better prediction.

They used the term as a brand for an **AI that resolves confusion in information**.

---

💡 **In practice:**  
Many people now use Perplexity as a **replacement for Google when researching something**, especially technical topics.

---

If you're curious, I can also explain something interesting:

**Why a lot of engineers now use Perplexity *alongside* ChatGPT rather than instead of it.**  
They actually serve quite different roles.

[M3] ME (2026-03-06 09:44):
Is it safe for sensitive info 

[M4] AI (2026-03-06 09:44):
Short answer: **No — you should assume it is *not safe* for sensitive or proprietary information.**

**entity["software","Perplexity AI","AI search engine"]**, like most cloud AI services, processes your prompts on **remote servers**. Unless you are running a **self-hosted AI model**, anything you type may be:

- stored temporarily or logged  
- used for service improvement or model training (depending on settings)  
- visible to administrators or support staff under some conditions  
- potentially exposed if accounts or systems were compromised

So the safe engineering rule is:

> **Treat any public AI service the same as sending an email to an external company.**

---

## What you should **NOT** put into Perplexity
For someone in your kind of engineering environment (imaging sensors, FPGA test systems, etc.), avoid sharing:

**Company confidential material**
- schematics
- PCB layouts
- FPGA code
- internal specifications
- customer data
- unreleased products

**Sensitive technical details**
- internal architectures
- proprietary algorithms
- security mechanisms
- internal network details

**Anything under NDA**

---

## Why it’s risky
AI services work by sending your prompt to a **cloud inference system**. That means:

1. Your text leaves your device  
2. It is processed on their infrastructure  
3. It may be logged for debugging or improvement  

Even if the company says **“we don’t train on it”**, the data still **exists on their systems**.

---

## Typical company policy
Many engineering companies (especially defence, aerospace, or semiconductor) restrict AI usage to:

- **public information only**
- **sanitized technical questions**

For example you could ask:

✅ Safe:
- “What limits LVDS cable length at 200 MHz?”  
- “Typical ADC anti-alias filter design”

❌ Not safe:
- “Here is our sensor readout schematic — why is this node oscillating?”

---

## Safer ways engineers use AI
A common pattern is:

**Generalize the problem.**

Instead of:

> “In our CIS125 burn-in board the OS node sits at 28 V…”

You might ask:

> “How would you measure current on a 28 V bias line with 5 mA nominal current?”

That removes proprietary context.

---

## If you want a **really safe AI workflow**
There are three levels:

| Level | Safety |
|---|---|
Public AI (ChatGPT, Perplexity) | lowest |
Enterprise AI with data controls | medium |
Self-hosted LLM (local GPU/server) | highest |

Large companies sometimes deploy **internal GPT systems** where data never leaves the company network.

---

💡 **My advice for your work context (Teledyne / sensor electronics):**

Use AI for:
- **conceptual design thinking**
- **component suggestions**
- **general theory**

But **never paste real schematics, internal docs, or code**.

---

If you want, I can also explain something many engineers don’t realise:

**Why Perplexity can actually be *riskier than ChatGPT* for sensitive information.**  
(It comes down to how it pulls live web sources.)
