import os
from PIL import Image
import pandas as pd
import piexif
from PIL import PngImagePlugin

# Define the source and output directories
source_dir = "sources/img/11k Collection/"
output_dir = "sources/output/11k Collection/"

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


def read_excel():
    #['Nr.' 'Prompts' 'image nr. 1' 'image nr. 2' 'image nr. 3' 'image nr. 14' 'directory' 'info' 'Animal' 'Plant' 'Landscape' 'Weather' 'Time' 'Features']
    df = pd.read_excel('sources/11k_metadata.xlsx', header=1, nrows=2763, usecols="A:N")

    return df

def write_file(df):
    slg_files = os.listdir("sources/img/11k Collection/SLJ/")
    n = 0
    for i in range(0, 2761):
            image_numbers = df.loc[i, ['image nr. 1', 'image nr. 2', 'image nr. 3', 'image nr. 14']]
            folder = evaluate_folder(df.loc[i, 'directory'])
            if not folder == 'SLJ/':
                for j in image_numbers:
                    try:
                        filepath = os.path.join(source_dir + folder, f'image ({round(j)}).webp')
                        image = Image.open(filepath)
                    except FileNotFoundError:
                        filepath = os.path.join(source_dir + folder, f'Image ({round(j)}).webp')
                        image = Image.open(filepath)
                    # Add the metadata field to the image
                    metadata = PngImagePlugin.PngInfo()
                    metadata.add_text("Nr.", str(df.loc[i, 'Nr.']) )
                    metadata.add_text("Prompts", df.loc[i, 'Prompts'] )
                    metadata.add_text("Animal", df.loc[i, 'Animal'] )
                    metadata.add_text("Plant", df.loc[i, 'Plant'] )
                    metadata.add_text("Landscape", df.loc[i, 'Landscape'] )
                    metadata.add_text("Weather", df.loc[i, 'Weather'] )
                    metadata.add_text("Time", df.loc[i, 'Time'] )
                    metadata.add_text("Features", df.loc[i, 'Features'] )


                    #Image save
                    image.save(f"{output_dir}{folder}{round(j):05}.png", pnginfo=metadata)
            else :
                t = 0
                while t < 4:
                    try:
                        filepath = os.path.join(source_dir + folder, slg_files[n])
                        image = Image.open(filepath)

                        # Add the metadata field to the image
                        metadata = PngImagePlugin.PngInfo()
                        metadata.add_text("Nr.", str(df.loc[i, 'Nr.']))
                        metadata.add_text("Prompts", df.loc[i, 'Prompts'] )
                        metadata.add_text("Animal", df.loc[i, 'Animal'] )
                        metadata.add_text("Plant", df.loc[i, 'Plant'] )
                        metadata.add_text("Landscape", df.loc[i, 'Landscape'] )
                        metadata.add_text("Weather", df.loc[i, 'Weather'] )
                        metadata.add_text("Time", df.loc[i, 'Time'] )
                        metadata.add_text("Features", df.loc[i, 'Features'] )


                        #Image save
                        image.save(f"{output_dir}{folder}{(n+1):05}.png", pnginfo=metadata)
                    except IndexError:
                        pass
                    n += 1                    
                    t += 1

    
def evaluate_folder(name):
    true_name = ''
    if name[0] == 'c':
        true_name = 'cg11 (0-4000)/'
    elif name[0] == 'd':
        true_name = 'dawi (1-6000)/'
    elif name[1] == 'L':
        true_name = name + '/' 
    elif name[0] == 's':
        true_name = "sweggers/" + name + '/'  
    return true_name

def check(filename):
    image = Image.open(filename)
    print(image.info)

if __name__ == '__main__':
    #test()
    #read_excel()
    #write_file(read_excel())
    check("sources/img/00065.png")