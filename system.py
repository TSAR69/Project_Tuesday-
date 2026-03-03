import os
import pyautogui
import screen_brightness_control as sbc
from tuesday.text_to_speech import speak

def set_volume(action):
    """Adjusts system volume."""
    if "up" in action:
        speak("Turning volume up")
        pyautogui.press("volumeup", presses=5)
    elif "down" in action:
        speak("Turning volume down")
        pyautogui.press("volumedown", presses=5)
    elif "mute" in action:
        speak("Muting volume")
        pyautogui.press("volumemute")

def set_brightness(action):
    """Adjusts screen brightness."""
    try:
        current = sbc.get_brightness()
        level = current[0] if current else 50
        
        if "up" in action:
            new_level = min(level + 10, 100)
            speak("Increasing brightness")
            sbc.set_brightness(new_level)
        elif "down" in action:
            new_level = max(level - 10, 0)
            speak("Decreasing brightness")
            sbc.set_brightness(new_level)
    except Exception as e:
        speak("Could not adjust brightness")
        print(f"[Error]: {e}")

def power_control(action):
    """Handles power operations."""
    if "shutdown" in action:
        speak("Shutting down the system in 5 seconds")
        os.system("shutdown /s /t 5")
    elif "restart" in action:
        speak("Restarting the system")
        os.system("shutdown /r /t 5")
    elif "sleep" in action:
        speak("Putting system to sleep")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
