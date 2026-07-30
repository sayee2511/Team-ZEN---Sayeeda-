from collections import Counter


class PredictionSmoother:
    def __init__(self, history_size=10):
        self.history = []
        self.history_size = history_size

    def update(self, prediction):
        """
        Add a prediction and return the most frequent
        prediction from the recent history.
        """

        if prediction is None:
            return None

        self.history.append(prediction)

        if len(self.history) > self.history_size:
            self.history.pop(0)

        return Counter(self.history).most_common(1)[0][0]

    def clear(self):
        self.history.clear()