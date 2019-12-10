import dlib
import cv2
from flask import current_app


def same_person(photo1, photo2):
    detector = dlib.get_frontal_face_detector()
    sp = dlib.shape_predictor(f"{current_app.config['MODEL_DIR']}/sp.dat")
    facerec = dlib.face_recognition_model_v1(
        f"{current_app.config['MODEL_DIR']}/fr.dat")

    p1 = dlib.load_rgb_image(photo1)
    p2 = dlib.load_rgb_image(photo2)

    face1 = detector(p1, 1)
    face2 = detector(p2, 1)

    if not face1 or not face2:
        return False

    for k, d in enumerate(face1):
        shape = sp(p1, d)
        desc1 = facerec.compute_face_descriptor(p1, shape)

    for k, d in enumerate(face2):
        shape = sp(p2, d)
        desc2 = facerec.compute_face_descriptor(p2, shape)

    cv2.rectangle(p1, (face1[0].left(), face1[0].top()),
                  (face1[0].right(), face1[0].bottom()), (0, 255, 0), 3)
    cv2.rectangle(p2, (face2[0].left(), face2[0].top()),
                  (face2[0].right(), face2[0].bottom()), (0, 255, 0), 3)

    p1 = cv2.cvtColor(p1, cv2.COLOR_BGR2RGB)
    p2 = cv2.cvtColor(p2, cv2.COLOR_BGR2RGB)

    cv2.imwrite(photo1, p1)
    cv2.imwrite(photo2, p2)

    cluster = dlib.chinese_whispers_clustering([desc1, desc2], 0.5)
    if len(set(cluster)) == 1:
        return True
    return False
