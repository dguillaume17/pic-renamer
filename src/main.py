from constants.constants import Constants
from factories.service_factory import ServiceFactory
from services.directory_extractor_service import DirectoryExtractor
from services.face_comparator_service import FaceComparator

serviceFactory = ServiceFactory(
    DirectoryExtractor(),
    FaceComparator()
)

directoryExtractor = serviceFactory.getDirectoryExtractor()
baseImagePathes = directoryExtractor.getFilesWithin(Constants.PATH_DIRECTORY_WITH_IMAGES_TO_BE_BASED_ON)
processImagePathes = directoryExtractor.getFilesWithin(Constants.PATH_DIRECTORY_WITH_IMAGES_TO_PROCESS)

faceComparator = serviceFactory.getFaceComparator()


for processImagePath in processImagePathes:
    for baseImagePath in baseImagePathes:
        if faceComparator.compareImages(baseImagePath, processImagePath):
            print('OK', baseImagePath, processImagePath)
        else:
            print('NOK', baseImagePath, processImagePath)

print(baseImagePathes, processImagePathes)
