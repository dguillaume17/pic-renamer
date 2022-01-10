from constants.constants import Constants
from factories.service_factory import ServiceFactory
from services.directory_extractor_service import DirectoryExtractor
from services.exif_extractor_service import ExifExtractor
from services.face_comparator_service import FaceComparator

serviceFactory = ServiceFactory(
    DirectoryExtractor(),
    ExifExtractor(),
    FaceComparator()
)

directoryExtractor = serviceFactory.getDirectoryExtractor()
exifExtractor = serviceFactory.getExifExtractor()
baseImagePathes = directoryExtractor.getFilesWithin(Constants.PATH_DIRECTORY_WITH_IMAGES_TO_BE_BASED_ON)
processImagePathes = directoryExtractor.getFilesWithin(Constants.PATH_DIRECTORY_WITH_IMAGES_TO_PROCESS)

faceComparator = serviceFactory.getFaceComparator()


for processImagePath in processImagePathes:
    for baseImagePath in baseImagePathes:
        newPath = exifExtractor.getCaptureDateTime(processImagePath)
        
        if faceComparator.compareImages(baseImagePath, newPath):
            print('OK', baseImagePath, processImagePath)
        else:
            print('NOK', baseImagePath, processImagePath)

#print(baseImagePathes, processImagePathes)
