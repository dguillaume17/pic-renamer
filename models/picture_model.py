from services.recognition_service import RecognitionService

class Picture:
    def __init__(self, file_path, file_name):
        self.file_path = file_path
        self.file_name = file_name
        
    def setup_face_encoding(self, recognition_service):
        RecognitionService.load_recognition(recognition_service, self.file_path + "/" + self.file_name)