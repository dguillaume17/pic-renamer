from PIL import Image
from PIL.ExifTags import TAGS

class ExifExtractor:
    def getCaptureDateTime(self, pathToMediaFile: str) -> str:
        print(f'getCaptureDateTime("{pathToMediaFile}"")')
        
        
        mediaFile = Image.open(pathToMediaFile)
        #mediaFile.rotate(180).save("test.jpg")
        mediaFile.save("test.jpg")
        exifData = mediaFile.getexif()
        
        for tagId in exifData:
            tagName = TAGS.get(tagId, tagId)
            tagValue = exifData.get(tagId)
            
            if isinstance(tagValue, bytes):
                tagValue = tagValue.decode()
                
            print(f'{tagName} : {tagValue}')
        
        return 'test'