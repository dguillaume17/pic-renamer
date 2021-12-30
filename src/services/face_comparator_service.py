import face_recognition
from services.face_comparator_compliant import FaceComparatorCompliant


class FaceComparator(FaceComparatorCompliant):
    
    def compareImages(self, pathToImage1: str, pathToImage2: str) -> bool:
        image1 = face_recognition.load_image_file(pathToImage1)
        image2 = face_recognition.load_image_file(pathToImage2)
        
        print('ICI', pathToImage2)
        print(face_recognition.face_encodings(image2))
    
        encoding1 = face_recognition.face_encodings(image1)[0]
        encoding2 = face_recognition.face_encodings(image2)[0]

        results = face_recognition.compare_faces([encoding1], encoding2)
        
        return results[0]
