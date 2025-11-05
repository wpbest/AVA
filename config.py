"""Configuration settings for AVA."""
import os

class Config:
    """Application configuration."""
    
    # Ollama Settings
    OLLAMA_ENDPOINT = os.getenv("OLLAMA_ENDPOINT", "http://localhost:11434/api/generate")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gemma3:1b")
    OLLAMA_TEMPERATURE = float(os.getenv("OLLAMA_TEMPERATURE", "0.0"))
    OLLAMA_MAX_TOKENS = int(os.getenv("OLLAMA_MAX_TOKENS", "20"))
    
    # Audio Settings
    AMBIENT_NOISE_DURATION = 0.5
    TTS_VOLUME = 1.0
    
    # Prompt Template
    PROMPT_TEMPLATE = (
        "Create the ultimate minimal response to the following prompt: {text}\n"
        "Respond with as fewest words as possible, ideally in a complete sentence."
    )
    
    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")