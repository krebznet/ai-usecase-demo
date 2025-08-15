#!/bin/bash
set -e

echo "=== AI Usecase Demo Setup & Run Script ==="

# 1. Install Ollama (only if missing)
if ! command -v ollama &>/dev/null; then
    echo "Installing Ollama..."
    brew install ollama
else
    echo "Ollama already installed ✅"
fi

# 2. Pull model (default llama3)
MODEL="llama3"
echo "Pulling model: $MODEL..."
ollama pull "$MODEL"

# 3. Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# 4. Run demo CLI
echo "Running CLI demo..."
python ollama_prompt_demo.py --text-file samples/sample_text.txt

# 5. Start API
echo "Starting FastAPI server..."
echo ">>> Open a new terminal and run the curl command below to test <<<"
echo 'curl -X POST http://127.0.0.1:8000/explain -H "Content-Type: application/json" -d '\''{"text":"Termination 15 days. Governing law NY. PHI without BAA."}'\'''

uvicorn app:app --reload --port 8000