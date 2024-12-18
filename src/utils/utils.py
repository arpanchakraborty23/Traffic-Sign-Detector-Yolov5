
import os
import base64


def decodeImage(image_data, file_path):
    try:
        with open(file_path, "wb") as file:
            file.write(base64.b64decode(image_data))
    except Exception as e:
        print(f"Error decoding image: {e}")

def encodeImageIntoBase64(file_path):
    try:
        with open(file_path, "rb") as file:
            return base64.b64encode(file.read())
    except Exception as e:
        print(f"Error encoding image: {e}")
