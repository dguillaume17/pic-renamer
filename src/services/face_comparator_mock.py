from services.face_comparator_compliant import FaceComparatorCompliant

class FaceComparatorMock(FaceComparatorCompliant):
    
    def compareImages(self, pathToImage1: str, pathToImage2: str) -> bool:
        if pathToImage1 == 'cauet.jpg':
            if pathToImage2 == 'img1.jpg':
                return True
            if pathToImage2 == 'img4.jpeg':
                return True

        
        if pathToImage1 == 'david guetta.jpeg':
            if pathToImage2 == 'img2.jpeg':
                return True
            if pathToImage2 == 'img3.jpeg':
                return True

        return False
