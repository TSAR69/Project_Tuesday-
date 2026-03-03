# Tuesday Voice Assistant

Tuesday is a lightweight, offline CLI-based voice assistant designed for Windows. It provides hands-free control over your system, applications, and media playback using strict wake-word detection.

## Features

- **Wake Word detection**: Listens efficiently for "noxr" to activate.
- **Offline Speech Recognition**: Powered by **Vosk** for privacy and speed.
- **System Control**: Manage volume, brightness, and power options (shutdown, restart, sleep).
- **App Launching**: Open common applications (Chrome, VS Code, Calculator, etc.) by voice.
- **Media Control**: Play, pause, skip tracks, and control volume.
- **Utilities**: Check the time, date, or hear a joke.

## Requirements

- **OS**: Windows
- **Python**: 3.11+
- **Microphone**: Standard input device.

## Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd Tuesday
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    *(Ensure `vosk`, `pyttsx3`, `pyaudio`, and other dependencies are listed in requirements.txt)*

3.  **Download Vosk Model**:
    - Download a small English model from [Vosk Models](https://alphacephei.com/vosk/models).
    - Extract it to `d:\Jarvis\jarvis\models\` (or update the path in `speech_to_text.py`).

## Usage

1.  Run the main script:
    ```bash
    python tuesday/main.py
    ```

2.  **Wait for initialization**:
    - The console will show: `[TUESDAY Online] Say 'tuesday' to wake me up.`

3.  **Speak Commands**:
    - **Wake up**: "tuesday"
    - **Commands**:
        - "Open Chrome"
        - "Set volume to 50"
        - "What time is it?"
        - "Play music"
        - "Go to sleep" (Returns to low-power listening mode)

## Configuration

- **Wake Word**: predefined as `"tuesday"` (strict match).
- **Settings**: Modify `tuesday/config.py` to add new apps or adjust defaults.

## License

MIT License

