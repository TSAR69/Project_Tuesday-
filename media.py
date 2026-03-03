import pyautogui
from tuesday.text_to_speech import speak

def control_media(action):
    """Controls media playback."""
    if "play" in action or "pause" in action:
        speak("Play pause")
        pyautogui.press("playpause")
    elif "next" in action:
        speak("Next track")
        pyautogui.press("nexttrack")
    elif "previous" in action or "back" in action:
        speak("Previous track")
        pyautogui.press("prevtrack")
