# 🎙️ Tuesday — Offline Voice Assistant for Windows

> A lightweight, offline CLI-based voice assistant for Windows. Hands-free control over your system, apps, and media — powered by strict wake-word detection. No internet. No cloud. No telemetry.

---

## ✨ Features

| Feature | Details |
|---|---|
| 🎤 Wake Word Detection | Listens for `"tuesday"` — strict match, no false triggers |
| 🧠 Offline Speech Recognition | Powered by Vosk — fully local, no API calls |
| 🖥️ System Control | Volume, brightness, shutdown, restart, sleep |
| 🚀 App Launching | Open Chrome, VS Code, Calculator, and more by voice |
| 🎵 Media Playback | Play, pause, skip tracks, control volume |
| 🕐 Utilities | Get the time, date, or hear a joke |

---

## 🖥️ Requirements

- **OS:** Windows 10 / 11
- **Python:** 3.11+
- **Microphone:** Any standard input device

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/TSAR69/Project_Tuesday-.git
cd Project_Tuesday-
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> Core dependencies include `vosk`, `pyaudio`, `pynput`, and others listed in `requirements.txt`

**If `pyaudio` fails on install:**
```bash
pip install pipwin
pipwin install pyaudio
```

### 3. Download the Vosk Model

1. Go to [https://alphacephei.com/vosk/models](https://alphacephei.com/vosk/models)
2. Download a **small English model** (e.g. `vosk-model-small-en-us-0.15`)
3. Extract it and update the model path inside `speech_to_text.py`

```python
# In speech_to_text.py — update this line to match your path:
model = Model("path/to/your/vosk-model-folder")
```

### 4. (Optional) Run Setup

```bash
python setup.py
```

---

## 🚀 Usage

### Start Tuesday

```bash
python main.py
```

You'll see:
```
[TUESDAY Online] Say 'tuesday' to wake me up.
```

### How to Use

1. Say **"tuesday"** — this activates the assistant
2. Wait for the confirmation tone / prompt
3. Speak your command

### Example Commands

```
"Open Chrome"         → Launches Google Chrome
"Set volume to 50"    → Sets system volume to 50%
"What time is it"     → Reads out the current time
"Play music"          → Starts media playback
"Shutdown"            → Initiates system shutdown
"Go to sleep"         → Returns to low-power listening mode
```

---

## 📁 Project Structure

```
Project_Tuesday-/
├── main.py              # Entry point — run this to start Tuesday
├── app.py               # Core app logic and command routing
├── speech_to_text.py    # Vosk-based offline speech recognition
├── system.py            # System control (volume, brightness, power)
├── config.py            # Wake word config and app settings
├── fa.py                # Feature/action handlers
├── setup.py             # First-time setup helper
├── __init__.py
├── test_open.py         # App launch tests
├── test_libary.py       # Library/dependency tests
├── test_to_speech.py    # Speech recognition tests
└── requirements.txt
```

---

## ⚙️ Configuration

Edit `config.py` to customize:

- **Wake word** — default is `"tuesday"` (strict match)
- **Registered apps** — add new apps Tuesday can open
- **Default behaviors** — adjust volume steps, default apps, etc.

---

## 🛠️ Troubleshooting

**Microphone not detected**
- Set your mic as the default recording device in Windows Sound Settings
- Test with: `python test_to_speech.py`

**Vosk model not found / crashes on start**
- Verify the model path in `speech_to_text.py` is correct
- The model folder should contain `am/`, `conf/`, and `graph/` subdirectories

**Wake word never triggers**
- Speak clearly at a normal pace
- Check mic input levels in Windows — should be at 70%+
- Run `python test_libary.py` to verify all dependencies loaded correctly

**App won't open via voice**
- Make sure the app is registered in `config.py`
- Run `python test_open.py` to debug app launch issues

**`pip install` errors**
- Run terminal as Administrator
- Confirm Python version: `python --version` (needs 3.11+)

---

## 📬 Contact & Issues

Found a bug? Something's broken? Want to suggest a feature?

- **Open an issue:** [github.com/TSAR69/Project_Tuesday-/issues](https://github.com/TSAR69/Project_Tuesday-/issues) ← best way to reach me
- **GitHub Profile:** [@TSAR69](https://github.com/TSAR69)

PRs are welcome. If it helped you, drop a ⭐

---

## 📄 License

MIT License — free to use, modify, and distribute.
