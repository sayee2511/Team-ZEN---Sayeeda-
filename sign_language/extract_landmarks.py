import os
import cv2
import pandas as pd
from tqdm import tqdm

from utils.mediapipe_detector import detect_hand_landmarks

DATASET_PATH = "sign_language/dataset"
OUTPUT_PATH = "sign_language/data/landmarks.csv"

os.makedirs("sign_language/data", exist_ok=True)

data = []

for label in sorted(os.listdir(DATASET_PATH)):
    class_path = os.path.join(DATASET_PATH, label)

    if not os.path.isdir(class_path):
        continue

    print(f"Processing {label}...")

    for image_name in tqdm(os.listdir(class_path)):
        image_path = os.path.join(class_path, image_name)

        image = cv2.imread(image_path)

        if image is None:
            continue

        _, landmarks = detect_hand_landmarks(image)

        if len(landmarks) != 63:
            continue

        row = [label] + landmarks
        data.append(row)

columns = ["label"]

for i in range(21):
    columns.extend([f"x{i}", f"y{i}", f"z{i}"])

df = pd.DataFrame(data, columns=columns)

df.to_csv(OUTPUT_PATH, index=False)

print("✅ Landmark extraction completed!")
print(df.head())
print(f"Saved to {OUTPUT_PATH}")