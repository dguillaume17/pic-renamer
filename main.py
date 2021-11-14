import face_recognition
from models.picture_location_enum import PictureLocation
from models.picture_model import Picture
from services.recognition_service import RecognitionService

recognition_service = RecognitionService()

template = Picture("cauet.jpg", PictureLocation.getDirectoryPath(PictureLocation.TEMPLATE))
face_encoding1 = Picture.setup_face_encoding(template, recognition_service)

pictures = PictureLocation.getPictures(PictureLocation.WORKLOAD)
for picture in pictures:
    face_encoding2 = Picture.setup_face_encoding(picture, recognition_service)
    
    results = face_recognition.compare_faces([face_encoding1], face_encoding2)
    
    print(results)
    if results == True:
        print("ok : " + picture.file_name)
    else:
        print("NOK : " + picture.file_name)



