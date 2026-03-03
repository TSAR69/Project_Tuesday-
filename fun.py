import random
from tuesday.config import JOKES
from tuesday.text_to_speech import speak

def tell_joke():
    """Tells a random joke from the config."""
    joke = random.choice(JOKES)
    speak(joke)
