from PIL import Image
import io
import os

# Program Goals


# Create a function that will write out a uint8_t array (with binary values) from a single .bmp file
# Overload the function to write out an arry of uint8_t arrays from either several .bmp files or a folder than contains several .bmp files
# Push the contents of said function to an output file that can be copy-pasted into a Source C++ file


# Define Filepath Constants (Edit these to select which file to convert)

inputPath = "Input/HeartBMP.bmp"
fileName = os.path.basename(inputPath)
outputPath = "Output/" + str(fileName)[0:len(fileName) - 4] + "Binary.h"
# outputPath = "Output/testFileBinary.h"


def BMPtoBinary(arrayName, file):
    image = Image.open(file)
    imageConverted1 = image.convert("L")
    width, height = image.size
    totalPixels = 0
    imageList = list(image.getdata())
    # Define a string to hold the bitmap array as text
    # COL_SIZE is a constant I have defined in my TMP Github Repository
    bitmapData = "#pragma once\n"
    bitmapData += "#include \"Arduino.h\""
    bitmapData += "\n\nclass BinaryArrays {\n"
    bitmapData += "public:\n"
    bitmapData += " uint8_t " + str(arrayName) + " [COL_SIZE] = \n"
    bitmapData += " {\n"


    # Start writing out code to write out uint8_t binary
    # Note the the zero-indexing will make the loops end at height - 1 and width - 1
    for a in range (height):
        # Iterating through height will show how many binary values will be in the array
        bitmapData += "  0b"
        for b in range (width):
            # Iterating through the .BMP width will actually determine the values of each bit
            # bitmapData += "0"
            if (imageList[b] == 255):
                bitmapData += "0"
            else:
                bitmapData += "1"  
        # Once the width has been determined, add a "," to end the element value and start on a newline
        if (a == (height - 1)):
            bitmapData += "\n };"
        else:
            bitmapData += ",\n"
    bitmapData += "\n};"

    return bitmapData


output = BMPtoBinary("testFrames", inputPath)
# print(outputPath)
outputFile = open(outputPath, "w")
outputFile.write(output)
outputFile.close()