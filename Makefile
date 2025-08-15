# Makefile for ai-usecase-demo
PYTHON=python3.12
VENV=.venv
ACTIVATE=source $(VENV)/bin/activate

.PHONY: setup run api ollama-install pull-model clean

setup:
	@echo "🔹 Setting up Python venv..."
	$(PYTHON) -m venv $(VENV)
	@$(ACTIVATE) && pip install --upgrade pip && pip install -r requirements.txt
	@echo "✅ Setup complete."

run:
	@echo "🚀 Running Ollama prompt demo..."
	@$(ACTIVATE) && python ollama_prompt_demo.py --text-file samples/sample_text.txt

api:
	@echo "🌐 Starting FastAPI server..."
	@$(ACTIVATE) && uvicorn app:app --reload --port 8000

ollama-install:
	@echo "📦 Installing Ollama via Homebrew..."
	brew install ollama

pull-model:
	@echo "⬇️ Pulling Llama 3 model..."
	ollama pull llama3

clean:
	@echo "🧹 Cleaning venv..."
	rm -rf $(VENV)