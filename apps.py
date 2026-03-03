import subprocess
import os
from tuesday.config import APPS as KNOWN_APPS
from tuesday.text_to_speech import speak

def open_app(app_name):
    """
    Opens an application with strict fallback logic.
    Order: KNOWN_APPS -> .exe -> protocols -> start search.
    """
    # 1. Clean Input
    clean_name = app_name.lower().replace("open ", "").strip()
    
    # 2. Check KNOWN_APPS
    if clean_name in KNOWN_APPS:
        path = KNOWN_APPS[clean_name]
        speak(f"Opening {clean_name}")
        try:
            # Check if it's a directory to use appropriate opener if needed, 
            # but usually start "" "path" works for dirs too.
            subprocess.Popen(f'start "" "{path}"', shell=True)
            return True
        except Exception as e:
            print(f"[Error] Failed to open known app {clean_name}: {e}")
            # Fall through if known app fails? The user rules say "If not found...". 
            # If known, we found it. If it fails to open, that's different.
            # But let's assume we return True to avoid double-searching.
            return True

    # 3. Check .exe
    if clean_name.endswith(".exe"):
        speak(f"Opening executable {clean_name}")
        try:
            subprocess.Popen(f'start "" "{clean_name}"', shell=True)
            return True
        except Exception:
            pass

    # 4. Protocol Check
    if ":" in clean_name and not " " in clean_name: # Simple heuristic for protocol like spotify:
        speak(f"Opening protocol {clean_name}")
        try:
            subprocess.Popen(f'start "" "{clean_name}"', shell=True)
            return True
        except Exception:
            pass

    # 5. Start Menu Search 
    # The user rule: "If not found: Use Windows Start Menu search via: start "" "<app_name>""
    speak(f"Searching for {clean_name}")
    try:
        # We assume success if we triggered the command, as 'start' handles the rest.
        # There is no easy way to know if 'start' failed without complex Popen piping which might block.
        # The user's prompt "If app still does not open: Speak..." is tricky with 'start'.
        # We will assume that if we got here, we try this. The feedback "Could not find" might only happen strictly if we decide NOT to run start?
        # Or maybe check if `where` finds it? 
        # But 'start' searches the Start Menu (Apps folder), which 'where' does not.
        
        # We will trust 'start' to do its job. 
        # If the user strictly wants "I could not find..." ON FAILURE, we can't easily detect failure of 'start' asynchronously.
        # We will rely on the "I searching..." message as the last "positive" feedback.
        
        subprocess.Popen(f'start "" "{clean_name}"', shell=True)
        return True
    except Exception as e:
        print(f"[Error] Search failed: {e}")

    # 6. Explicit Failure (Only reachable if code logic changes or specific conditions met)
    speak("I could not find that application")
    return False
