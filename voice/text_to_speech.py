import pyttsx3


class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()

        self.engine.setProperty("rate", 170)
        self.engine.setProperty("volume", 1)

        voices = self.engine.getProperty("voices")
        if voices:
            self.engine.setProperty("voice", voices[0].id)

    def speak(self, text):
        """Speak any text passed from other modules."""
        print(f"\nSAKSHAM AI : {text}")

        self.engine.say(text)
        self.engine.runAndWait()


tts = TextToSpeech()


if __name__ == "__main__":
    tts.speak("Welcome to Saksham AI.")