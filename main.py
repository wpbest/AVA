"""Entry point for AVA application."""
from ava.core.assistant import AVA
from ava.llm.ollama_client import OllamaClient
from config import Config


def main():
    """Initialize and run AVA."""
    # Initialize LLM client (only thing separated from original)
    ollama_client = OllamaClient(
        endpoint=Config.OLLAMA_ENDPOINT,
        model=Config.OLLAMA_MODEL,
        temperature=Config.OLLAMA_TEMPERATURE,
        max_tokens=Config.OLLAMA_MAX_TOKENS
    )
    
    # Create and run assistant
    assistant = AVA(
        ollama_client=ollama_client,
        prompt_template=Config.PROMPT_TEMPLATE
    )
    
    assistant.run()


if __name__ == "__main__":
    main()