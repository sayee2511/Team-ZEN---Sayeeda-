import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)


def detect_hand_landmarks(image):
    """
    Detect hand landmarks from an image.

    Args:
        image: Input BGR image

    Returns:
        image: Image with landmarks drawn
        landmarks: List of 63 values (21 landmarks × x, y, z)
    """

    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_image)

    landmarks = []

    if results.multi_hand_landmarks:
        hand = results.multi_hand_landmarks[0]

        # Draw landmarks
        mp_drawing.draw_landmarks(
            image,
            hand,
            mp_hands.HAND_CONNECTIONS
        )

        # Store x, y, z coordinates
        for lm in hand.landmark:
            landmarks.extend([lm.x, lm.y, lm.z])

    return image, landmarks