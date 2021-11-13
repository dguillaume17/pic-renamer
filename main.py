import face_recognition
from face_recognition.api import face_encodings
from os import listdir

def get_templates_path(filename):
    return "assets/img/templates/" + filename

def get_pictures_path(filename):
    return "assets/img/pictures/" + filename

def load_recognition_image(filepath):
    return face_recognition.load_image_file(filepath)

def setupFaceEncoding(filepath):
    recognition_image = load_recognition_image(filepath);
    
    return face_recognition.face_encodings(recognition_image)[0];

face_encoding1 = setupFaceEncoding(get_templates_path("cauet.jpg"))

filenames = listdir(get_pictures_path("."))
for filename in filenames:
    filepath = get_pictures_path(filename)
    
    face_encoding2 = setupFaceEncoding(filepath)
    
    results = face_recognition.compare_faces([face_encoding1], face_encoding2)
    
    print(results)
    if results == True:
        print("ok : " + filename)
    else:
        print("NOK : " + filename)



