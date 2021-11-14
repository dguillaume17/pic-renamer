
import face_recognition

class RecognitionService:
    def load_recognition(self, file_path):
        recognition_image = face_recognition.load_image_file(file_path)
    
        face_encoding = face_recognition.face_encodings(recognition_image)
    
        return face_encoding[0]