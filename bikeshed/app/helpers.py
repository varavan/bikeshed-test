# coding=utf-8
import os
import uuid


def sanitaze_image_upload_path(instance, filename):
    path = 'image-upload'

    filename = filename.split('.')
    extension = str(filename.pop())

    id_ = str(uuid.uuid4())

    new_file_name = '%s.%s' % (
        id_,
        extension
    )
    return os.path.join(path, new_file_name)


