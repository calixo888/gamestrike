from PIL import Image
import os

def crop_images():
    for file in os.listdir(os.path.abspath("media/profile_pictures")):
        try:
            filepath = os.path.abspath("media/profile_pictures") + "/" + file
            img = Image.open(filepath)
            width, height = img.size
            crop_size = min(img.size)
            left = (width - crop_size)/2
            top = (height - crop_size)/2
            right = (width + crop_size)/2
            bottom = (height + crop_size)/2

            img = img.crop((left, top, right, bottom))
            img.save(filepath)
        except Exception as e:
            print(e)
