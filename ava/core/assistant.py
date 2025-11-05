"""Core assistant logic for AVA."""
import speech_recognition as sr
import pyttsx3
import sys


class AVA:
    """Agentic Voice Assistant."""
    
    def __init__(self, ollama_client, prompt_template: str):
        """
        Initialize AVA.
        
        Args:
            ollama_client: LLM client instance
            prompt_template: Template for formatting prompts
        """
        self.ollama = ollama_client
        self.prompt_template = prompt_template
    
    def run(self):
        """Main conversation loop."""
        print(f"Hello, I'm running Python version {sys.version}")
        print("Say something...")
        
        # Initialize the Recognizer ONCE - but as LOCAL variable, not self
        recognizer = sr.Recognizer()
        
        while True:
            # 1. LISTEN TO AUDIO
            with sr.Microphone() as source:
                print("Listening...")
                
                # Adjust for ambient noise for better accuracy
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                
                # Listen for audio
                audio = recognizer.listen(source)
            
            # 2. PROCESS AND SPEAK
            try:
                # Recognize speech
                text = recognizer.recognize_google(audio)
                print(f"You said: {text}")
                
                # Create prompt
                constrained_prompt = self.prompt_template.format(text=text)
                
                # Get response from Ollama
                text_response = self.ollama.generate(constrained_prompt)
                
                if text_response is None:
                    text_response = "Sorry, there was an error from the model."
                
                print("Response from Ollama:", text_response)
                
                # 1. Initialize a NEW engine instance
                tts_engine = pyttsx3.init()
                tts_engine.setProperty('volume', 1.0)
                
                # 2. Say the text response
                tts_engine.say(text_response)
                tts_engine.runAndWait()
                
                # 3. Explicitly stop and delete the engine
                del tts_engine
                
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand what you said.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                try:
                    del tts_engine
                except:
                    pass