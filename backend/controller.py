from voice.text_to_speech import tts


class Controller:

    def speak(self, message):
        tts.speak(message)

    def handle_ocr(self, text):

        self.speak(text)

    def handle_sign_language(self, text):

        self.speak(text)

    def handle_object_detection(self, text):

        self.speak(text)