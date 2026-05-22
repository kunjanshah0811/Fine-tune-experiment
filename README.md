# Fine-tune-experiment

Models and Datasets are available here: [Hugging Face](https://huggingface.co/kunjanshah)

---

## What is this project about?

Large language models (LLMs) like GPT, Mistral, Llama, and Qwen can do a lot more than just answer questions. When connected to external tools and APIs, they can take real actions, like checking a database, booking a calendar event, or running a workflow. This ability is called **function calling**.

But here is the problem: models often get it wrong. They misread the prompt, generate incomplete parameters, use the wrong data types, or call a function when they should not. This project investigates how **fine-tuning** and **hyperparameter optimization** can fix that and by how much.

The short answer from the experiments: fine-tuning improved accuracy and completeness by roughly **40-50%** over the baseline. Hyperparameter tuning added another **3-5%** on top, and in multi-turn conversations, success rates nearly doubled compared to the un-tuned versions.

---

## Who is this for?

- Researchers working on LLM reliability and structured output generation
- Developers building agentic systems, copilots, or automation pipelines
- Anyone curious about fine-tuning open-source models to compete with closed-source ones (spoiler: it works better than you might expect)

---

## What research questions does this answer?

**RQ1: Which models are actually good at function calling out of the box?**

This compares OpenAI, Mistral, Llama, and Qwen on single-turn function calling tasks. The goal is to see how well each model can read a natural language prompt and produce a structured function call with correct format, complete parameters, and valid types. It also tests whether models know when to call a tool versus when to just respond normally.

**RQ2: How much does fine-tuning actually help?**

This takes the same open-source models (Mistral, Llama, Qwen) and fine-tunes them using a dataset built specifically for API-style function calling tasks. The results are compared before and after fine-tuning to measure the exact improvement in schema compliance and call accuracy.

**RQ3: Does it hold up in a real conversation (multi-turn)?**

Single-turn is one thing. But real applications involve back-and-forth conversations, clarifications, and context that builds over multiple messages. This question tests whether the improvements from fine-tuning carry over into multi-turn scenarios, like a support agent or a workflow automation assistant.

---

## What does the code do?

This repo contains notebooks and scripts for:

- **QLoRA fine-tuning** using low-rank adapters (memory-efficient, runs on a single GPU)
- **Hyperparameter optimization (HPO)** using Optuna to squeeze out extra performance
- **AST-based evaluation** to check structural correctness of generated function calls, not just fuzzy text matching
- **Inference helpers** for calling models through Hugging Face, OpenAI, or OpenRouter

---

## Repo structure

```
Fine-tune-experiment/
├── 1.Single_turn_fc/      # Notebooks and scripts for single-turn function calling & evaluation
├── 2.Multi_turn_fc/       # Notebooks and scripts for multi-turn function calling & evaluation
└── README.md
```

---

## Requirements

- Python 3.8 or higher
- A CUDA-compatible GPU (strongly recommended for fine-tuning; CPU is too slow)
- API keys for Hugging Face, OpenAI, and OpenRouter

---

## Why does this matter?

Most LLM benchmarks focus on reasoning or general knowledge. Function calling is different. It requires the model to produce structured output that has to be exactly right, not approximately right. Wrong parameter name? The API call fails. Wrong data type? Runtime error. Missing required field? The whole pipeline breaks.

This work shows that smaller open-source models, when fine-tuned properly on targeted datasets, can reach or even surpass the performance of much larger closed-source models like GPT-5 on these specific tasks. That is a meaningful result for anyone who cares about cost, privacy, or deployment constraints.
