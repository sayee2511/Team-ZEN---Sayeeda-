import easyocr
import re
from ocr.preprocess import preprocess_image

reader = easyocr.Reader(['en'])

def extract_text(image_path):

    processed_image = preprocess_image(image_path)

    results = reader.readtext(
        processed_image,
        paragraph=False,
        detail=1,
        decoder="beamsearch",
        batch_size=1
    )

    text = ""
    for box, word, confidence in results:
        print(f"{word} --> {confidence:.2f}")

        if confidence > 0.60:
            text += word + " "
    

    # Remove unwanted OCR symbols
    text = re.sub(r'[^A-Za-z0-9\s.,!?():/-]', '', text)

    # Remove extra spaces
    text = " ".join(text.split())
    

    return text