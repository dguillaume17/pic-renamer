from services.recognition_service import RecognitionService

class Picture:
    def __init__(self, file_name, file_path):
        self.file_name = file_name
        self.file_path = file_path
        
    def setup_face_encoding(self, recognition_service):
        return RecognitionService.load_recognition(recognition_service, self.file_path + self.file_name)