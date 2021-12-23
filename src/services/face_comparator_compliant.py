import abc

class FaceComparatorCompliant(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def compareImages(self, pathToImage1: str, pathToImage2: str) -> bool:
        pass