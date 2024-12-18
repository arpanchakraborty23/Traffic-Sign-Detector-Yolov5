import logging
import os
import base64

logging.basicConfig(level=logging.INFO)

def decodeImage(imgstring, fileName):
    try:
        directory = "./data"
        os.makedirs(directory, exist_ok=True)
        file_path = os.path.join(directory, fileName)

        imgdata = base64.b64decode(imgstring)
        with open(file_path, 'wb') as f:
            f.write(imgdata)
        logging.info(f"Image successfully decoded and saved to {file_path}")
    except Exception as e:
        logging.error(f"Error decoding image: {e}")
        raise e

def encodeImageIntoBase64(croppedImagePath):
    try:
        if not os.path.exists(croppedImagePath):
            raise FileNotFoundError(f"File does not exist: {croppedImagePath}")

        with open(croppedImagePath, "rb") as f:
            encoded = base64.b64encode(f.read())
        logging.info(f"Image successfully encoded to base64: {croppedImagePath}")
        return encoded
    except Exception as e:
        logging.error(f"Error encoding image: {e}")
        raise e 
