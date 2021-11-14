from enum import Enum, auto
from os import listdir

from models.picture_model import Picture

class PictureLocation(Enum):
    TEMPLATE = auto()
    WORKLOAD = auto()
    
    def getDirectoryPath(self):
        match self:
            case PictureLocation.TEMPLATE:
                return "assets/pictures/template/"
            case PictureLocation.WORKLOAD:
                return "assets/pictures/workload/"
            
    def getPictures(self):
        directory_path = PictureLocation.getDirectoryPath(self)
        file_names = listdir(
            PictureLocation.getDirectoryPath(self)
        )
        
        pictures = []

        for file_name in file_names:
            picture = Picture(file_name, directory_path)
            pictures.append(picture)
            
        return pictures
