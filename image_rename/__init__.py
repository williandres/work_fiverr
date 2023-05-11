import os
from PIL import Image
import pandas as pd
import piexif
from PIL import PngImagePlugin

# Define the source and output directories
source_dir = 'sources/img/GEN-2/'
output_dir = 'sources/output/GEN-2/'
excel_file = 'sources/Gen2_metadata.xlsx'
"""
def test():
    for filename in os.listdir(source_dir):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png") or filename.endswith(".webp"):
            # Open the image and add the "x" metadata field with value "y"
            filepath = os.path.join(source_dir, filename)
            image = Image.open(filepath)

            # Add the metadata field to the image
            metadata = PngImagePlugin.PngInfo()
            metadata.add_text("Software", "x=y")
            metadata.add_text("Softsdfgsdfgware", "x=ydfgsd")
            image.save("sources/output/image (5).png", pnginfo=metadata)
"""

def read_excel():
    df = pd.read_excel(excel_file, header=0, nrows=76, usecols="A:L")
    return df

def write_file(df):
    for i in range(0, 75):
            image_numbers = df.loc[i, ['image nr.', 'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11']]
            folder = df.loc[i, 'Folder']
            for j in image_numbers:
                filepath = os.path.join(source_dir + str(folder), f'image ({round(j)}).webp')
                image = Image.open(filepath)
                # Add the metadata field to the image
                metadata = PngImagePlugin.PngInfo()
                metadata.add_text("Prompt", df.loc[i, 'Prompt'] )
                metadata.add_text("Animal", df.loc[i, 'Animal'] )
                metadata.add_text("Plant", df.loc[i, 'Plant'] )
                metadata.add_text("Landscape", df.loc[i, 'Landscape'] )
                metadata.add_text("Weather", df.loc[i, 'Weather'] )
                metadata.add_text("Time", df.loc[i, 'Time'] )
                metadata.add_text("Features", df.loc[i, 'Features'] )


                #Image save
                image.save(f"{output_dir}{folder}/{round(j):03}.png", pnginfo=metadata)

def evaluate_folder(name):
    pass


def check(filename):
    image = Image.open(filename)
    print(image.info)

if __name__ == '__main__':
    #test()
    #read_excel()
    #write_file(read_excel())
    #check("sources/img/016.png")
