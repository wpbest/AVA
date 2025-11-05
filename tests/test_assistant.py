"""Unit tests for AVA assistant."""
import unittest
from unittest.mock import Mock, patch
from ava.core.assistant import AVA
from ava.audio.listener import AudioListener
from ava.audio.speaker import AudioSpeaker
from ava.llm.ollama_client import OllamaClient


class TestAVA(unittest.TestCase):
    """Test cases for AVA assistant."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.mock_ollama = Mock(spec=OllamaClient)
        self.mock_listener = Mock(spec=AudioListener)
        self.mock_speaker = Mock(spec=AudioSpeaker)
        self.prompt_template = "Test: {text}"
        
        self.ava = AVA(
            ollama_client=self.mock_ollama,
            listener=self.mock_listener,
            speaker=self.mock_speaker,
            prompt_template=self.prompt_template
        )
    
    def test_initialization(self):
        """Test AVA initialization."""
        self.assertIsNotNone(self.ava)
        self.assertEqual(self.ava.prompt_template, self.prompt_template)
    
    def test_process_input_success(self):
        """Test successful input processing."""
        self.mock_ollama.generate.return_value = "Test response"
        
        result = self.ava.process_input("Hello")
        
        self.assertEqual(result, "Test response")
        self.mock_ollama.generate.assert_called_once_with("Test: Hello")
    
    def test_process_input_none_response(self):
        """Test input processing when LLM returns None."""
        self.mock_ollama.generate.return_value = None
        
        result = self.ava.process_input("Hello")
        
        self.assertEqual(result, "Sorry, there was an error from the model.")


class TestAudioListener(unittest.TestCase):
    """Test cases for AudioListener."""
    
    def test_initialization(self):
        """Test AudioListener initialization."""
        listener = AudioListener(ambient_noise_duration=1.0)
        self.assertIsNotNone(listener.recognizer)
        self.assertEqual(listener.ambient_noise_duration, 1.0)


class TestAudioSpeaker(unittest.TestCase):
    """Test cases for AudioSpeaker."""
    
    def test_initialization(self):
        """Test AudioSpeaker initialization."""
        speaker = AudioSpeaker(volume=0.8)
        self.assertEqual(speaker.volume, 0.8)


class TestOllamaClient(unittest.TestCase):
    """Test cases for OllamaClient."""
    
    def test_initialization(self):
        """Test OllamaClient initialization."""
        client = OllamaClient(
            endpoint="http://test:11434/api/generate",
            model="test-model",
            temperature=0.5,
            max_tokens=50
        )
        self.assertEqual(client.endpoint, "http://test:11434/api/generate")
        self.assertEqual(client.model, "test-model")
        self.assertEqual(client.temperature, 0.5)
        self.assertEqual(client.max_tokens, 50)
    
    @patch('ava.llm.ollama_client.requests.post')
    def test_generate_success(self, mock_post):
        """Test successful generation."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"response": "Generated text"}
        mock_post.return_value = mock_response
        
        client = OllamaClient(
            endpoint="http://test:11434/api/generate",
            model="test-model"
        )
        
        result = client.generate("Test prompt")
        
        self.assertEqual(result, "Generated text")
        mock_post.assert_called_once()
    
    @patch('ava.llm.ollama_client.requests.post')
    def test_generate_error(self, mock_post):
        """Test generation with error response."""
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.text = "Internal error"
        mock_post.return_value = mock_response
        
        client = OllamaClient(
            endpoint="http://test:11434/api/generate",
            model="test-model"
        )
        
        result = client.generate("Test prompt")
        
        self.assertEqual(result, "Error 500")


if __name__ == '__main__':
    unittest.main()