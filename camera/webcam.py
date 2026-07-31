import cv2
import os

def capture_image():

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Unable to access webcam.")
        return None

    print("Press SPACE to capture image")
    print("Press ESC to exit")

    while True:

        ret, frame = cap.read()

        if not ret:
            print("Failed to capture frame.")
            break

        cv2.imshow("Camera", frame)

        key = cv2.waitKey(1)

        if key == 27:   # ESC
            break

        elif key == 32:   # SPACE

            save_folder = "camera/images"

            os.makedirs(save_folder, exist_ok=True)

            image_path = os.path.join(save_folder, "captured.jpg")

            cv2.imwrite(image_path, frame)

            #print("Image Captured Successfully.")

            cap.release()
            cv2.destroyAllWindows()

            return image_path

    cap.release()
    cv2.destroyAllWindows()

    return None