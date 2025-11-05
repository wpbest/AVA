"""Audio output handling for AVA."""
import pyttsx3
from ..utils.logger import setup_logger

logger = setup_logger(__name__)


class AudioSpeaker:
    """Handles text-to-speech output."""
    
    def __init__(self, volume: float = 1.0):
        """
        Initialize the audio speaker.
        
        Args:
            volume: TTS volume (0.0 to 1.0)
        """
        self.volume = volume
        logger.info("AudioSpeaker initialized")
    
    def speak(self, text: str) -> bool:
        """
        Convert text to speech and play it.
        IMPORTANT: Creates a NEW engine instance each time (original working pattern)
        
        Args:
            text: Text to speak
            
        Returns:
            True if successful, False otherwise
        """
        tts_engine = None
        try:
            # 1. Initialize a NEW engine instance (ORIGINAL PATTERN)
            tts_engine = pyttsx3.init()
            tts_engine.setProperty('volume', self.volume)
            
            # 2. Say the text response
            tts_engine.say(text)
            tts_engine.runAndWait()
            
            # 3. Explicitly delete the engine (ORIGINAL PATTERN)
            del tts_engine
            
            logger.info(f"Spoke: {text[:50]}...")
            return True
            
        except Exception as e:
            logger.error(f"TTS error: {e}")
            # Ensure a broken engine is cleaned up (ORIGINAL PATTERN)
            try:
                del tts_engine
            except:
                pass
            return False