import cv2

def preprocess_image(image_path):

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Image not found.")

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Remove noise while preserving text edges
    gray = cv2.bilateralFilter(gray, 11, 17, 17)

    # Improve contrast
    gray = cv2.equalizeHist(gray)

    # Adaptive threshold
    thresh = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        11
    )

    return thresh