from services.directory_extractor_service import DirectoryExtractor
from services.face_comparator_compliant import FaceComparatorCompliant


class ServiceFactory:
    
    def __init__(
        self,
        directoryExtractor: DirectoryExtractor,
        faceComparator: FaceComparatorCompliant
    ):
        self._directoryExtractor = directoryExtractor
        self._faceComparator = faceComparator
        
    def getDirectoryExtractor(self) -> DirectoryExtractor:
        return self._directoryExtractor
    
    def getFaceComparator(self) -> FaceComparatorCompliant:
        return self._faceComparator