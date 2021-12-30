from services.directory_extractor_service import DirectoryExtractor
from services.exif_extractor_service import ExifExtractor
from services.face_comparator_compliant import FaceComparatorCompliant


class ServiceFactory:
    
    def __init__(
        self,
        directoryExtractor: DirectoryExtractor,
        exifExtractor: ExifExtractor,
        faceComparator: FaceComparatorCompliant
    ):
        self._directoryExtractor = directoryExtractor
        self._exifExtractor = exifExtractor
        self._faceComparator = faceComparator
        
    def getDirectoryExtractor(self) -> DirectoryExtractor:
        return self._directoryExtractor
    
    def getExifExtractor(self) -> ExifExtractor:
        return self._exifExtractor
    
    def getFaceComparator(self) -> FaceComparatorCompliant:
        return self._faceComparator