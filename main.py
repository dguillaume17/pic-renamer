import face_recognition
from face_recognition.api import face_encodings
from os import listdir

from models.picture_model import Picture
from services.recognition_service import RecognitionService


def get_templates_path(filename):
    return "assets/pictures/template/" + filename

def get_pictures_path(filename):
    return "assets/pictures/workload/" + filename

def load_recognition_image(filepath):
    return face_recognition.load_image_file(filepath)

def setupFaceEncoding(filepath):
    recognition_image = load_recognition_image(filepath)
    
    face_encoding = face_recognition.face_encodings(recognition_image)
    
    return face_encoding[0]

face_encoding1 = setupFaceEncoding(get_templates_path("cauet.jpg"))

filenames = listdir(get_pictures_path("."))
for filename in filenames:
    filepath = get_pictures_path(filename)
    
    recognition_service = RecognitionService()
    picture = Picture(get_pictures_path(""), filename)
    picture.setup_face_encoding(recognition_service)
    
    face_encoding2 = setupFaceEncoding(filepath)
    
    results = face_recognition.compare_faces([face_encoding1], face_encoding2)
    
    print(results)
    if results == True:
        print("ok : " + filename)
    else:
        print("NOK : " + filename)



