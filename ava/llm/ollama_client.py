"""Ollama LLM client for AVA."""
import requests
from typing import Optional, Dict, Any
from ..utils.logger import setup_logger

logger = setup_logger(__name__)


class OllamaClient:
    """Client for interacting with Ollama API."""
    
    def __init__(
        self,
        endpoint: str,
        model: str,
        temperature: float = 0.0,
        max_tokens: int = 20
    ):
        """
        Initialize the Ollama client.
        
        Args:
            endpoint: Ollama API endpoint URL
            model: Model name to use
            temperature: Sampling temperature
            max_tokens: Maximum tokens in response
        """
        self.endpoint = endpoint
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        logger.info(f"OllamaClient initialized with model: {model}")
    
    def generate(self, prompt: str) -> Optional[str]:
        """
        Generate a response from the LLM.
        
        Args:
            prompt: Input prompt
            
        Returns:
            Generated text or None if request failed
        """
        payload: Dict[str, Any] = {
            "prompt": prompt,
            "model": self.model,
            "stream": False,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens
        }
        
        try:
            response = requests.post(self.endpoint, json=payload, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                text_response = result.get("response", "")
                logger.info(f"LLM response: {text_response[:50]}...")
                return text_response
            else:
                logger.error(f"LLM error {response.status_code}: {response.text}")
                return f"Error {response.status_code}"
                
        except requests.exceptions.Timeout:
            logger.error("LLM request timed out")
            return "Request timed out"
        except requests.exceptions.RequestException as e:
            logger.error(f"LLM request failed: {e}")
            return "Connection error"
        except Exception as e:
            logger.error(f"Unexpected error during LLM generation: {e}")
            return "Unexpected error"