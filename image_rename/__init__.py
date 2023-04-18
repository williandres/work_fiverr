import os
from PIL import Image

# loop to open images and add an add metadata to each image
def main():
    for file in os.listdir("sources/img/"):
        if file.endswith(".jpg") or file.endswith(".webp") or file.endswith(".jpeg") or file.endswith(".gif") or file.endswith(".svg") or file.endswith(".bmp") or file.endswith(".tif") or file.endswith(".tiff") or file.endswith(".jfif") or file.endswith(".pjpeg") or file.endswith(".pjp") or file.endswith(".png"):
            path_file = os.path.join("sources/img/", file)
            img = Image.open(path_file)
            img.info["x"] = "y"
            img.info["m"] = "z"
            img.save(f"sources/output/{file}")

if __name__ == '__main__':
    main()