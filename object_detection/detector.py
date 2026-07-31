from object_detection.yolo_model import model

def detect_objects(image_path):

    results = model(image_path, verbose=False)

    detected_objects = []

    for result in results:

        for box in result.boxes:

            class_id = int(box.cls[0])

            object_name = model.names[class_id]

            detected_objects.append(object_name)

    return list(set(detected_objects))