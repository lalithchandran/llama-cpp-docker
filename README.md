# Llama.cpp CUDA Docker Server

A production-ready Docker configuration for running the `llama.cpp` server with NVIDIA CUDA acceleration using GGUF models.

This repository provides a clean and extensible setup for GPU-based local LLM inference, suitable for backend integration, experimentation, and AI system development.

---

## Overview

This project enables:

- GPU-accelerated inference using llama.cpp
- Dockerized deployment
- Support for GGUF quantized models
- Easy integration with API-based systems

It serves as a foundation for building local LLM applications such as:

- AI backends
- Multimodal pipelines
- OCR + LLM systems
- Research and experimentation environments

---

## Tech Stack

- Docker
- llama.cpp (server build)
- NVIDIA CUDA
- GGUF models

---

## Project Structure

llama-cpp-docker/

│

├── Dockerfile

├── docker-compose.yml

├── download_model.py

├── models/                # Model files (excluded from Git)

└── README.md

> Note: Model files are not included in this repository due to size constraints.

---

## Requirements

- Docker
- NVIDIA GPU
- NVIDIA Container Toolkit
- Compatible NVIDIA drivers

Verify GPU support:

```bash
docker run --rm --gpus all nvidia/cuda:12.2.0-base nvidia-smi
```

## Model Setup

Download your preferred GGUF model and place it inside the `models/` directory.

Example:

models/Qwen3VL-2B-Instruct-Q4_K_M.gguf
models/mmproj-Qwen3VL-2B-Instruct-Q8_0.gguf

Ensure model paths match your Docker configuration.

---

## Build the Image

From the project root:

<pre class="overflow-visible! px-0!" data-start="1808" data-end="1854"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="pointer-events-none absolute inset-x-px top-6 bottom-6"><div class="sticky z-1!"><div class="bg-token-bg-elevated-secondary sticky"></div></div></div><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>docker build </span><span class="ͼu">-t</span><span> llama-cpp-server .</span></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

## Run the Server (GPU Enabled)

<pre class="overflow-visible! px-0!" data-start="1894" data-end="1957"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="pointer-events-none absolute inset-x-px top-6 bottom-6"><div class="sticky z-1!"><div class="bg-token-bg-elevated-secondary sticky"></div></div></div><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>docker run </span><span class="ͼu">--gpus</span><span> all </span><span class="ͼu">-p</span><span></span><span class="ͼq">8080</span><span>:8080 llama-cpp-server</span></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

Modify port mappings and runtime flags as needed.

---

## API Access

Default endpoint:

<pre class="overflow-visible! px-0!" data-start="2049" data-end="2078"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="pointer-events-none absolute inset-x-px top-6 bottom-6"><div class="sticky z-1!"><div class="bg-token-bg-elevated-secondary sticky"></div></div></div><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>http://localhost:8080</span></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

Example request:

curl http://localhost:8080/v1/chat/completions 
  -H "Content-Type: application/json" 
  -d '{
    "model": "your-model-name",
    "messages": [
      {"role": "user", "content": "Hello"}
    ]
  }'

<pre class="overflow-visible! px-0!" data-start="2098" data-end="2310"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span class="ͼr">}'</span></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

## Customization

You can extend this setup by:

* Adding a FastAPI proxy layer
* Implementing authentication
* Configuring logging
* Creating a multi-service Docker Compose setup
* Integrating with OCR or vision pipelines

---

## Use Cases

* Local LLM experimentation
* GPU benchmarking
* Backend AI integration
* Multimodal model serving
* Research projects

---

## Python Environment Setup

Create a virtual environment:

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows
```

Install dependencies:

```
pip install -r requirements.txt
```


---
Now let me ask something important:

Is this repo:
- Pure Docker (no Python runtime needed inside)?
- Or are you planning to combine this with your FastAPI + OCR pipeline?


---
Because if you're building toward AI backend roles, we should structure this like a **real AI microservice project**, not just a container wrapper.

---

## Author

U. Lalith Chandran

M.Sc Computer Science

Software Developer | AI  Enthusiast
