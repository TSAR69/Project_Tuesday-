import os
import sys
from tuesday.speech_to_text import listen
from tuesday.text_to_speech import speak
from tuesday.config import WAKE_WORD
from tuesday.commands import apps, system, media, fun

def main():
    """Main loop for the Tuesday Voice Assistant."""
    speak(f"Hello! I am ready. Say '{WAKE_WORD}' to wake me up.")
    
    try:
        while True:
            text = listen().lower()
            if not text:
                continue
            
            if WAKE_WORD in text:
                speak("How can I help you?")
                command = listen().lower()
                
                if not command:
                    continue
                
                # Routing logic
                if "open" in command:
                    apps.open_app(command)
                elif "volume" in command or "mute" in command:
                    system.set_volume(command)
                elif "brightness" in command:
                    system.set_brightness(command)
                elif "shutdown" in command or "restart" in command or "sleep" in command:
                    system.power_control(command)
                elif any(word in command for word in ["play", "pause", "next", "previous", "back"]):
                    media.control_media(command)
                elif "joke" in command:
                    fun.tell_joke()
                elif "exit" in command or "stop" in command:
                    speak("Goodbye!")
                    break
                else:
                    speak("I am not sure how to do that yet.")
            
    except KeyboardInterrupt:
        speak("Shutting down.")
    except Exception as e:
        print(f"[Error] Main loop crashed: {e}")
        speak("I encountered an error and must restart.")

if __name__ == "__main__":
    main()
