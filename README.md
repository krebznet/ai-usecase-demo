# AI Usecase Demo — Personal Project by Duncan Krebs

**AI-powered document analysis demo** that showcases:
- 📄 **PDF text extraction**
- 🤖 **Local LLM analysis** using [Ollama](https://ollama.ai/) (no API keys needed)
- 🛠 **FastAPI backend** for easy integration into apps or frontends
- 💡 Example use case: Contract deviation detection, but easily adaptable to other document AI tasks.

---

## 🚀 Features
- **PDF Parsing** — extracts raw text for analysis
- **Deviation Detection** — detects clauses or terms deviating from a baseline
- **Local AI Inference** — works fully offline with `llama3` or any Ollama model
- **REST API** — ready to plug into a UI or automation pipeline
- **Extensible** — replace prompt templates, add embeddings, or hook into Hugging Face models

---

## 🛠 Installation

**Requirements**
- macOS (Apple Silicon M1/M2/M3/M4 recommended)
- Python 3.12+
- [Homebrew](https://brew.sh/) installed

**Setup**
```bash
# Clone repo
git clone https://github.com/YOURUSERNAME/ai-usecase-demo.git
cd ai-usecase-demo

# Install Python deps
pip install -r requirements.txt

# Install Ollama (one-time)
brew install ollama

# Pull a model (llama3 recommended)
ollama pull llama3
