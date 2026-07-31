import json
import queue
from pathlib import Path

import sounddevice as sd
from vosk import Model, KaldiRecognizer


class SpeechToText:

    def __init__(self):

        model_path = (
            Path(__file__).resolve().parent.parent
            / "models"
            / "vosk-model-small-en-in-0.4"
        )

        self.model = Model(str(model_path))
        self.q = queue.Queue()

    def callback(self, indata, frames, time, status):

        if status:
            print(status)

        self.q.put(bytes(indata))

    def listen(self):

        recognizer = KaldiRecognizer(self.model, 16000)

        print("\n🎤 Listening...")

        with sd.RawInputStream(
                samplerate=16000,
                blocksize=8000,
                dtype="int16",
                channels=1,
                callback=self.callback):

            while True:

                data = self.q.get()

                if recognizer.AcceptWaveform(data):

                    result = json.loads(recognizer.Result())

                    text = result.get("text", "")

                    if text:

                        print(f"\nYou : {text}")

                        return text


if __name__ == "__main__":

    stt = SpeechToText()

    while True:

        command = stt.listen()

        if command == "exit":
            break