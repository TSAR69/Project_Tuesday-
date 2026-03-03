import os
import json
import pyaudio
from vosk import Model, KaldiRecognizer

# Initialize Model (Path is relative to this file)
MODEL_PATH = os.path.join(os.path.dirname(__file__), "models", "vosk-model-en-in-0.5")

if not os.path.exists(MODEL_PATH):
    print(f"[Error] Vosk model not found at: {MODEL_PATH}")
    print("Please ensure the 'vosk-en' model is in the 'models' directory.")
    MODEL = None
else:
    print(f"[Init] Loading Vosk Model from {MODEL_PATH}...")
    try:
        MODEL = Model(MODEL_PATH)
    except Exception as e:
        print(f"[Error] Failed to load model: {e}")
        MODEL = None

# Audio Configuration
SAMPLE_RATE = 16000
CHUNK_SIZE = 4096

def listen() -> str:
    """
    Listens using Vosk (Offline).
    Blocks until a complete phrase is recognized.
    Returns the recognized text string (lowercase).
    """
    if not MODEL:
        print("[Error] Model not loaded.")
        return ""

    rec = KaldiRecognizer(MODEL, SAMPLE_RATE)
    p = pyaudio.PyAudio()

    try:
        stream = p.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=SAMPLE_RATE,
                        input=True,
                        frames_per_buffer=CHUNK_SIZE)
        
        stream.start_stream()
        print("[Listening...]")

        while True:
            data = stream.read(CHUNK_SIZE, exception_on_overflow=False)
            if len(data) == 0:
                continue

            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "").strip()
                if text:
                    print(f"[Heard]: {text}")
                    return text
    
    except KeyboardInterrupt:
        print("\n[Stopped]")
        raise
    except Exception as e:
        print(f"[Error]: {e}")
        return ""
    finally:
        # cleanup
        try:
            if 'stream' in locals():
                stream.stop_stream()
                stream.close()
            if 'p' in locals():
                p.terminate()
        except:
            pass
