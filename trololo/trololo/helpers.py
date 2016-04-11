from PIL import Image

MAX_THUMBNAIL_SIZE = 112.0


def resize_logo(instance):
    """
    Resize model logo to needed sizes.
    """
    width = instance.photo.width
    height = instance.photo.height

    filename = instance.photo.path
    max_size = max(width, height)

    if max_size > MAX_THUMBNAIL_SIZE:
        ratio = min(MAX_THUMBNAIL_SIZE/width, MAX_THUMBNAIL_SIZE/height)
        image = Image.open(filename)
        image = image.resize(
            (int(round(width * ratio)), int(round(height * ratio))),
            Image.ANTIALIAS
        )
        image.save(filename)