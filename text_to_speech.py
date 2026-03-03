import pyttsx3
import sys

# Initialize engine once globally
try:
    ENGINE = pyttsx3.init('sapi5')
    ENGINE.setProperty('rate', 170)
    ENGINE.setProperty('volume', 1.0)
    
    # Optional: Select a specific voice if desired, but default is usually fine.
    # voices = ENGINE.getProperty('voices')
    # if voices:
    #    ENGINE.setProperty('voice', voices[0].id)
    
except Exception as e:
    print(f"[Error] Failed to initialize TTS engine: {e}")
    sys.exit(1)

def speak(text: str):
    """
    Convert text to speech synchronously using the global engine.
    This function blocks until speech is finished.
    """
    if not text:
        return

    print(f"[Tuesday]: {text}")
    try:
        # Queue the speech
        ENGINE.say(text)
        # Block until spoken
        ENGINE.runAndWait()
    except RuntimeError:
        # This catches "run loop already started" errors if called recursively
        pass
    except Exception as e:
        print(f"[Error] TTS failed: {e}")
