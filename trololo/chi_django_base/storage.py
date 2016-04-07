from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os


# http://stackoverflow.com/questions/9522759/imagefield-overwrite-image-file-with-same-name
class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name):
    # If the filename already exists, remove it as if it was a true file system
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name