class SentenceBuilder:
    def __init__(self):
        self.text = ""

    def add_character(self, character):
        """Add a recognized character."""
        if character is not None:
            self.text += str(character)

    def add_space(self):
        """Add a space."""
        self.text += " "

    def backspace(self):
        """Remove the last character."""
        self.text = self.text[:-1]

    def clear(self):
        """Clear the sentence."""
        self.text = ""

    def get_text(self):
        """Return the current sentence."""
        return self.text