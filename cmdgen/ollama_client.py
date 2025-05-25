import subprocess

def query_ollama(prompt: str) -> str:
    """Send a prompt to the Ollama model and return its response."""
    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL
    )
    return result.stdout.decode("utf-8")
