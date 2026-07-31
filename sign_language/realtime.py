import cv2

from utils.mediapipe_detector import detect_hand_landmarks
from utils.classifier import SignClassifier
from utils.predictor import PredictionSmoother
from utils.sentence import SentenceBuilder
from utils.speech import TextToSpeech

# Initialize components
classifier = SignClassifier()
smoother = PredictionSmoother(history_size=10)
sentence = SentenceBuilder()
speaker = TextToSpeech()

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open webcam.")
    exit()

print("========== CONTROLS ==========")
print("SPACE  -> Add current letter")
print("ENTER  -> Speak sentence")
print("BACKSPACE -> Delete last letter")
print("C -> Clear sentence")
print("Q -> Quit")
print("==============================")

current_prediction = ""

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    frame, landmarks = detect_hand_landmarks(frame)

    confidence = 0

    if len(landmarks) == 63:

        prediction, confidence = classifier.predict(landmarks)

        prediction = smoother.update(prediction)

        if prediction is not None:
            current_prediction = prediction

    # Show prediction
    cv2.putText(
        frame,
        f"Prediction: {current_prediction}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Show confidence
    cv2.putText(
        frame,
        f"Confidence: {confidence:.1f}%",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 0, 0),
        2
    )

    # Show current sentence
    cv2.putText(
        frame,
        f"Sentence: {sentence.get_text()}",
        (20, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    cv2.imshow("SAKSHAM AI - Sign Language", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord(' '):
        sentence.add_character(current_prediction)

    elif key == 13:      # Enter
        speaker.speak(sentence.get_text())

    elif key == 8:       # Backspace
        sentence.backspace()

    elif key == ord('c'):
        sentence.clear()

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()