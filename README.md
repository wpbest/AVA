# AVA (Agentic Voice Assistant)

A modular voice assistant powered by Ollama and speech recognition.

## Features

- 🎤 Speech-to-text using Google Speech Recognition
- 🤖 LLM integration with Ollama (local)
- 🔊 Text-to-speech output
- 📦 Modular, maintainable architecture
- 🔧 Configurable via environment variables
- 📝 Comprehensive logging

## Installation

1. **Clone or download this repository**

2. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

3. **Install and start Ollama:**
```bash
# Install Ollama from https://ollama.ai

# Pull your desired model
ollama pull gemma3:1b

# Start Ollama server
ollama serve
```

## Project Structure

```
ava/
├── README.md
├── requirements.txt
├── config.py
├── main.py
├── ava/
│   ├── __init__.py
│   ├── audio/
│   │   ├── __init__.py
│   │   ├── listener.py
│   │   └── speaker.py
│   ├── llm/
│   │   ├── __init__.py
│   │   └── ollama_client.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── assistant.py
│   └── utils/
│       ├── __init__.py
│       └── logger.py
└── tests/
    ├── __init__.py
    └── test_assistant.py
```

## Usage

Run the assistant:
```bash
python main.py
```

The assistant will:
1. Listen for your voice input
2. Convert speech to text
3. Send to Ollama for processing
4. Speak the response back to you

Press `Ctrl+C` to exit.

## Configuration

Edit `config.py` or set environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `OLLAMA_ENDPOINT` | Ollama API URL | `http://localhost:11434/api/generate` |
| `OLLAMA_MODEL` | Model name | `gemma3:1b` |
| `OLLAMA_TEMPERATURE` | Sampling temperature | `0.0` |
| `OLLAMA_MAX_TOKENS` | Max response length | `20` |
| `LOG_LEVEL` | Logging verbosity | `INFO` |

Example:
```bash
export OLLAMA_MODEL="llama2"
export LOG_LEVEL="DEBUG"
python main.py
```

## Architecture

- **`ava/audio/`**: Audio input/output handling
  - `listener.py`: Speech recognition
  - `speaker.py`: Text-to-speech
- **`ava/llm/`**: LLM client implementation
  - `ollama_client.py`: Ollama API integration
- **`ava/core/`**: Main assistant logic
  - `assistant.py`: Orchestrates all components
- **`ava/utils/`**: Utility functions
  - `logger.py`: Logging setup
- **`config.py`**: Configuration settings
- **`main.py`**: Application entry point

## Development

### Adding New Features

1. Create new modules in appropriate directories
2. Follow the existing naming conventions
3. Add proper docstrings and type hints
4. Update `__init__.py` files to export new classes

### Testing

Create tests in the `tests/` directory:
```python
# tests/test_assistant.py
import unittest
from ava.core.assistant import AVA

class TestAVA(unittest.TestCase):
    def test_initialization(self):
        # Your tests here
        pass
```

Run tests:
```bash
python -m unittest discover tests
```

## Troubleshooting

**Microphone not working:**
- Check microphone permissions
- Ensure PyAudio is installed correctly
- Test with: `python -c "import speech_recognition as sr; print(sr.Microphone.list_microphone_names())"`

**Ollama connection failed:**
- Ensure Ollama is running: `ollama serve`
- Check endpoint configuration
- Verify model is downloaded: `ollama list`

**TTS not working:**
- On Linux, install espeak: `sudo apt-get install espeak`
- On macOS/Windows, pyttsx3 should work out of the box

## License

MIT License - feel free to use and modify!

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Credits

Built with:
- [SpeechRecognition](https://github.com/Uberi/speech_recognition)
- [pyttsx3](https://github.com/nateshmbhat/pyttsx3)
- [Ollama](https://ollama.ai)

# AVA
AVA (Agentic Voice Assistant)

In VSCode hit Ctrl-Shift-P to open up the command palette.

Type: Python Create Environment
