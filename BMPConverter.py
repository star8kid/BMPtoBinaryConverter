from PIL import Image
import io


# Program Goals


# Create a function that will write out a uint8_t array (with binary values) from a single .bmp file
# Overload the function to write out an arry of uint8_t arrays from either several .bmp files or a folder than contains several .bmp files
# Push the contents of said function to an output file that can be copy-pasted into a Source C++ file


# Define Filepath Constants (Edit these to select which file to convert)

inputPath = "Input/testFile.bmp"
outputPath = "Output/testFileBinary.h"


def BMPtoBinary(arrayName, file):
    image = Image.open(file)
    imageConverted1 = image.convert("L")
    imageConverted1.show()
    # imageConverted2 = image.convert("1")
    # imageConverted2.show()

    # Start writing out code to write out uint8_t binary
    width, height = image.size
    for a in range (height):
        for b in range (width):

            print("Filler Text!")
    pass
    # print(width)
    # print(height)

    return arrayName


# BMPtoBinary("testFrames", inputPath)

image = Image.open(r"./Input/testFile.bmp")
imageConverted1 = image.convert("L")
imageConverted1.show()





# index = image.getpixel((5,0))
# testString = str(index)
# print(testString)

