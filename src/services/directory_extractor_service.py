from os import listdir

class DirectoryExtractor:
    
    def getFilesWithin(self, pahtToDirectory: str) -> list[str] :
        return [pahtToDirectory + fileName for fileName in listdir(pahtToDirectory) if fileName != '.DS_Store' and fileName != 'OLD']