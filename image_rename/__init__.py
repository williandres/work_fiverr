import os
from PIL import Image
from exif import Image as loco
import pandas as pd

# Define the source and output directories
source_dir = "sources/img/test"
output_dir = "sources/output"

def main():
    for filename in os.listdir(source_dir):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png") or filename.endswith(".webp"):
            # Open the image and add the "x" metadata field with value "y"
            filepath = os.path.join(source_dir, filename)
            image = Image.open(filepath)


            #Add the metadata field to the image
            image.info["Software"] = "x=y" 

            # Save the image with the new metadata field to the output directory
            output_path = os.path.join(output_dir, "filename.png")
            image.save(output_path)

            print(f"Metadata del objeto:")
            print(image.info)



if __name__ == '__main__':
    main()
    print(f"Metadata de sources/output/filename.png:")
    image = Image.open("sources/output/filename.png")
    print(image.info)
