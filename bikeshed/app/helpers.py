import os
import uuid


def sanitaze_image_upload_path(instance, filename):
    path = "image-upload"
    filename = filename.split('.')
    extension = str(filename.pop())
    id = str(uuid.uuid4())
    format = id + '.' + extension
    return os.path.join(path, format)
