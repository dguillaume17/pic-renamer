import io
from PIL import Image
from PIL.ExifTags import TAGS

class ExifExtractor:
    def getCaptureDateTime(self, pathToMediaFile: str) -> Image:
        print(f'getCaptureDateTime("{pathToMediaFile}"")')
        
        
        mediaFile = Image.open(pathToMediaFile)
        
        b = io.BytesIO()
        mediaFile.rotate(180).save(b, mediaFile.format)
        b.seek(0)
        #mediaFile.rotate(180)
        #mediaFile.save("test.jpg")
        exifData = mediaFile.getexif()
        
        for tagId in exifData:
            tagName = TAGS.get(tagId, tagId)
            tagValue = exifData.get(tagId)
            
            if isinstance(tagValue, bytes):
                tagValue = tagValue.decode()
                
            print(f'{tagName} : {tagValue}')
        
        return b