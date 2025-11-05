"""AVA - Agentic Voice Assistant."""
from .core import AVA
from .audio import AudioListener, AudioSpeaker
from .llm import OllamaClient

__version__ = "1.0.0"
__all__ = ['AVA', 'AudioListener', 'AudioSpeaker', 'OllamaClient']