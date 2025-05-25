import sys
from cmdgen.ollama_client import query_ollama

def main():
    if len(sys.argv) < 2:
        print("Usage: cmdgen 'describe your task'")
        sys.exit(1)

    user_prompt = sys.argv[1]
    system_prompt = (
        "You are a helpful Linux command-line assistant. "
        "Only return the appropriate command without explanation or formatting. "
        f"Task: {user_prompt}"
    )

    response = query_ollama(system_prompt)
    print("\nSuggested Command:\n", response.strip())
