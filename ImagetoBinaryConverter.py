from PIL import Image
import io
import os

# Program Goals


# Create a function that will write out a uint8_t array (with binary values) from a single .bmp file
# Overload the function to write out an arry of uint8_t arrays from either several .bmp files or a folder than contains several .bmp files
# Push the contents of said function to an output file that can be copy-pasted into a Source C++ file


# Define Filepath Constants (Edit these to select which file to convert)

# inputPath = "Input/HeartBMP.bmp"
inputPath = "Input/testPNG.png"
fileName = os.path.basename(inputPath)
outputPath = "Output/" + str(fileName)[0:len(fileName) - 4] + "Binary.h"
# outputPath = "Output/testFileBinary.h"


def ImagetoBinary(file, arrayName):
    image = Image.open(file)
    width, height = image.size
    totalPixels = 0
    
    # Implement a switch statement to handle several file formats

    imageList = list(image.getdata())
    # Define a string to hold the image binary array as text (to be written as a header file)
    # COL_SIZE is a constant I have defined in my TMP Github Repository
    headerData = "#pragma once\n"
    headerData += "#include \"Arduino.h\""
    headerData += "\n\nclass BinaryArrays {\n"
    headerData += "public:\n"
    headerData += " uint8_t " + str(arrayName) + " [COL_SIZE] = \n"
    headerData += " {\n"


    # Start writing out code to write out uint8_t binary
    # Note the the zero-indexing will make the loops end at height - 1 and width - 1
    match (image.format):
        case "BMP":
            print("Converting BMP...")
            for a in range (height):
            # Iterating through height will show how many binary values will be in the array
                headerData += "  0b"
            for b in range (width):
                # Iterating through the .BMP width will actually determine the values of each bit
                # bitmapData += "0"
                if (imageList[b] == 255):
                    headerData += "0"
                else:
                    headerData += "1"  
            # Once the width has been determined, add a "," to end the element value and start on a newline
            if (a == (height - 1)):
                headerData += "\n };"
            else:
                headerData += ",\n"
        case "PNG":
            print("Converting PNG...")
        case _:
            # Throw an error for this part of the function (remind user to use an image file format)
            print("Error: File Format Unsupported. Are you sure you're using a PNG, JPEG or BMP file?")
        
    headerData += "\n};"
    return headerData


output = ImagetoBinary(inputPath, "testFrames")
# print(outputPath)
outputFile = open(outputPath, "w")
outputFile.write(output)
outputFile.close()