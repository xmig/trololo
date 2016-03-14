from PIL import Image

MAX_THUMBNAIL_SIZE = 200

def resize_logo(instance):
    """
    Resize model logo to needed sizes.
    """
    width = instance.logo.width
    height = instance.logo.height

    filename = instance.logo.path

    max_size = max(width, height)

    if max_size > MAX_THUMBNAIL_SIZE:  
        image = Image.open(filename)
        image = image.resize(
            (round(width / max_size * MAX_THUMBNAIL_SIZE),
             round(height / max_size * MAX_THUMBNAIL_SIZE)),
            Image.ANTIALIAS
        )
        image.save(filename)