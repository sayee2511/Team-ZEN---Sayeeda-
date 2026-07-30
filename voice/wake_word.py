class WakeWord:

    def __init__(self):

        self.wake_word = "hey saksham"

    def detected(self, text):

        return self.wake_word in text.lower()


if __name__ == "__main__":

    wake = WakeWord()

    while True:

        sentence = input("Say : ")

        if wake.detected(sentence):

            print("Wake Word Detected!")

        else:

            print("Waiting...")