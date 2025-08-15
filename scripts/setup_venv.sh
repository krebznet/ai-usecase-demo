#!/usr/bin/env bash
# scripts/setup_venv.sh
# One-time + recurring venv setup for ai-usecase-demo

# Save current flags so we can restore them on exit
_ORIGINAL_FLAGS="$-"
# Enable safer mode for the script’s own commands
set -e
set -o pipefail
# DO NOT set -u when sourcing, it leaks into parent shell and breaks prompts

cleanup() {
  # Restore -e
  case "$_ORIGINAL_FLAGS" in
    *e*) set -e ;;
    *) set +e ;;
  esac
  # Restore pipefail
  set +o pipefail
}
trap cleanup RETURN

PYTHON_VER="3.12"
PYTHON_BIN="python${PYTHON_VER}"
VENV_DIR=".venv"

# 1) Install Python if missing
if ! command -v "${PYTHON_BIN}" &> /dev/null; then
  echo "🔹 Installing Python ${PYTHON_VER} via Homebrew..."
  brew install "python@${PYTHON_VER}"
else
  echo "✅ Python ${PYTHON_VER} already installed."
fi

# 2) Create venv if missing
if [ ! -d "${VENV_DIR}" ]; then
  echo "🔹 Creating virtual environment..."
  "${PYTHON_BIN}" -m venv "${VENV_DIR}"
else
  echo "✅ Virtual environment already exists."
fi

# 3) Activate (must be sourced to persist)
# shellcheck disable=SC1090
source "${VENV_DIR}/bin/activate"

python -V
echo "✅ venv active. To deactivate: 'deactivate'"