from enum import Enum, auto
from os import listdir

from models.picture_model import Picture

class PictureLocation(Enum):
    TEMPLATE = auto()
    WORKLOAD = auto()
    
    def get_directory_path(self) -> str:
        match self:
            case PictureLocation.TEMPLATE:
                return "src/assets/pictures/template/"
            case PictureLocation.WORKLOAD:
                return "src/assets/pictures/workload/"
            
    def get_pictures(self):
        directory_path = PictureLocation.get_directory_path(self)
        file_names = listdir(
            PictureLocation.get_directory_path(self)
        )
        
        pictures = []

        for file_name in file_names:
            picture = Picture(file_name, directory_path)
            pictures.append(picture)
            
        return pictures
