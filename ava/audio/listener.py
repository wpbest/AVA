"""Audio input handling for AVA."""
import speech_recognition as sr
from typing import Optional


class AudioListener:
    """Handles audio input and speech recognition."""
    
    def __init__(self, ambient_noise_duration: float = 0.5):
        """
        Initialize the audio listener.
        
        Args:
            ambient_noise_duration: Duration to adjust for ambient noise
        """
        # Initialize the Recognizer ONCE
        self.recognizer = sr.Recognizer()
        self.ambient_noise_duration = ambient_noise_duration
    
    def listen(self) -> Optional[str]:
        """
        Listen to microphone input and convert to text.
        EXACT ORIGINAL PATTERN - microphone context manager ensures cleanup.
        
        Returns:
            Recognized text or None if recognition failed
        """
        # 1. LISTEN TO AUDIO - with statement ensures microphone cleanup
        with sr.Microphone() as source:
            print("Listening...")
            
            # Adjust for ambient noise for better accuracy
            self.recognizer.adjust_for_ambient_noise(
                source, 
                duration=self.ambient_noise_duration
            )
            
            # Listen for audio
            audio = self.recognizer.listen(source)
        # Microphone is automatically closed here by context manager
        
        # 2. RECOGNIZE (after microphone is closed)
        try:
            text = self.recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            return None
        except Exception:
            return None