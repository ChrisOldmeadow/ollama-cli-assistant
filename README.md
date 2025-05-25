# cmdgen — Local CLI Assistant Powered by Ollama

`cmdgen` is a local command-line tool that uses a locally hosted LLM (via [Ollama](https://ollama.com)) to translate natural language instructions into Linux terminal commands.

---

## 🚀 Features

- Converts English prompts into shell commands
- Runs locally — no API keys or cloud access required
- Uses models like `llama3`, `mistral`, or any supported by Ollama
- Extensible and hackable Python codebase

---

## 🛠️ Installation

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/ollama-cli-assistant.git
cd ollama-cli-assistant

2. Set up virtual environment

python3 -m venv venv
source venv/bin/activate

3. Install dependencies and tool

pip install -e .

🧠 Requirements

    Python 3.8+

    Ollama installed locally

    A model (e.g. llama3) downloaded:

    ollama run llama3

🧪 Usage

cmdgen "Find all PDF files in the current directory modified in the last 2 days"

Example output:

find . -name '*.pdf' -mtime -2

🧰 Development
Run tests:

pytest

Project structure:

cmdgen/
├── cli.py              # CLI entry point
├── ollama_client.py    # Handles Ollama interaction
├── utils.py            # (Optional) Utility helpers
tests/

📄 License

MIT License
💡 Future Ideas

    Interactive mode (cmdgen --interactive)

    Confirm-and-execute mode (cmdgen --run)

    Command history and logging

    Support multiple models via config

🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.
