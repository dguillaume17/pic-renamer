from os import listdir

class DirectoryExtractor:
    
    def getFilesWithin(self, pahtToDirectory: str) -> list[str] :
        return listdir(pahtToDirectory)