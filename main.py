import face_recognition
from enums.picture_location_enum import PictureLocation
from models.picture_model import Picture
from services.recognition_service import RecognitionService

def main(recognition_service: RecognitionService):
    template = Picture("cauet.jpg", PictureLocation.get_directory_path(PictureLocation.TEMPLATE))
    face_encoding1 = Picture.setup_face_encoding(template, recognition_service)

    pictures = PictureLocation.get_pictures(PictureLocation.WORKLOAD)
    for picture in pictures:
        face_encoding2 = Picture.setup_face_encoding(picture, recognition_service)
        
        results = face_recognition.compare_faces([face_encoding1], face_encoding2)
        
        print(results)
        if results == True:
            print("ok : " + picture.file_name)
        else:
            print("NOK : " + picture.file_name)


main(
    RecognitionService()
)
