# Fine-tune-experiment

Repository: kunjanshah0811/Fine-tune-experiment

Overview
--------
This repository contains code and scripts to perform QLoRA-based fine-tuning, hyperparameter optimization (HPO), and AST-based evaluation for language models. Datasets and inference can be accessed via Hugging Face, OpenAI, or OpenRouter APIs — you must supply your own API tokens/keys.

High-level capabilities
- QLoRA applied for low-rank adapter fine-tuning.
- Multiple pre-configured base model targets (listed below).
- Hyperparameter optimization workflow (Optuna / configurable).
- AST-based evaluation script to compute structural/programming-aware metrics.
- Inference helpers to call models via Hugging Face / OpenAI / OpenRouter APIs.

Requirements
- Python 3.8+
- CUDA-compatible GPU (recommended for fine-tuning)
- A Hugging Face token, an OpenAI API key, and an OpenRouter API key to access datasets and do inference via those services.

Environment variables
- HUGGINGFACE_TOKEN (or HF_TOKEN)
- OPENAI_API_KEY
- OPENROUTER_API_KEY
