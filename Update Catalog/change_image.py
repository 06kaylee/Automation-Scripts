import PIL
from PIL import Image
import pathlib

images_path = pathlib.Path.home().joinpath('supplier-data/images')

# modifies each image in the directory: resizes them to 600 x 400 resolution and converts them to jpeg 
for path in images_path.rglob('*.tiff'):
        with Image.open(path) as old_img:
                new_img = old_img.resize((600, 400)).convert('RGB')
                new_img_path = "{}.jpeg".format(images_path.joinpath(path.stem))
                new_img.save(new_img_path)