import PIL
from PIL import Image
import pathlib
import argparse

parser = argparse.ArgumentParser(description="Modifies images and stores them in a new folder")

parser.add_argument("OriginalPath", metavar="originalpath", type=str, help="The path to the images that need to be modified.")
parser.add_argument("NewPath", metavar="newpath", type=str, help="The path where the new images are stored.")


args = parser.parse_args()

original_path = args.OriginalPath
new_path = args.NewPath

old_images = pathlib.Path(original_path).resolve()
new_images = pathlib.Path(new_path).mkdir(parents=True, exist_ok=True)

for path in old_images.iterdir():
    with Image.open(path) as old_img:
        new_img = old_img.rotate(90).resize((100, 100))
        new_img.save(pathlib.Path(new_path).resolve().joinpath(path.name))
        
        

