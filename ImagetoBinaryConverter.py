from PIL import Image
import numpy
import io
import os

# Program Goals


# Create a function that will write out a uint8_t array (with binary values) from a single .bmp file
# Overload the function to write out an arry of uint8_t arrays from either several .bmp files or a folder than contains several .bmp files
# Push the contents of said function to an output file that can be copy-pasted into a Source C++ file


# Testing different types of BMP files from Microsoft Paint
bmpPath = "Input/SquareBMP16Color.bmp" # Mode = P
bmpPathTwo = "Input/SquareBMP256Color.bmp" # Mode = P
bmpPathThree = "Input/SquareBMP24Bit.bmp" # Mode = RGB
bmpPathFour = "Input/SquareBMPMonochrome.bmp" # Mode = 1
pngPath = "Input/SquarePNG.png" # Mode = RGBA
jpgPath = "Input/SquareJPG.jpg" # Mode = RGB

inputPath = bmpPathThree




# inputPath = "Input/testFile.bmp"
# inputPath = "Input/testPNG.png"
fileName = os.path.basename(inputPath)
outputPath = "Output/" + str(fileName)[0:len(fileName) - 4] + "Binary.h"
numpy.set_printoptions(threshold=numpy.inf)

# Later Tasks:
# Work on testing different cases of BMP files

def ImagetoBinary(file, arrayName):
    image = Image.open(file)
    width, height = image.size
    totalPixels = 0
    
    # Implement a switch statement to handle several file formats

    imageList = list(image.getdata())
    # Note: Write out a test function in a different file to check if the selected image is valid
    # Examples of things to test:
    # "Does the image have any dimension with a size of 0?"

    imageNumpyArray = numpy.array(imageList).reshape(height, width*len(imageList[0])) 

    # Define a string to hold the image binary array as text (to be written as a header file)
    # COL_SIZE is a constant I have defined in my TMP Github Repository
    headerData = "#pragma once\n"
    headerData += "#include \"Arduino.h\""
    headerData += "\n\nclass BinaryArrays {\n"
    headerData += "public:\n"
    headerData += " uint8_t " + str(arrayName) + " [COL_SIZE] = \n"
    headerData += " {\n"
    # print("The current image format is: " + image.format)
    # print("The mode of the image is: " + str(image.mode))
    

    # Start writing out code to write out uint8_t binary
    # Note the the zero-indexing will make the loops end at height - 1 and width - 1
    match (image.format):
        case "BMP":
            # print("The mode of the image is: " + str(image.mode))

            # Define another switch statement for the different kinds of supported BMP files
            match(image.mode):
                # Note: Make a seperate if-else statement for each image mode depending on if the image has the edge case of being 1px by 1px
                # ** This is so that an image having one pixel will only return either a 1 or a 0
                case "1":
                    print("Converting Monochromatic BMP...")
                    # The value below is that of the white pixels in a BMP image of this mode
                    whitePixelValue = 255 
                    # I check the first pixel's width here at the 0th index because previous conditionals prove it exists
                    for a in range (height):
                    # Iterating through height will show how many binary values will be in the array
                        headerData += "  0b"
                        for b in range (width):
                            # Iterating through the .BMP width will actually determine the values of each bit
                            if (imageNumpyArray[a][b] == whitePixelValue):
                                headerData += "0"
                            else:
                                # headerData += str(imageList[b])
                                headerData += "1"  
                        # Once the width has been determined, add a "," to end the element value and start on a newline
                        if (a == (height - 1)):
                            headerData += "\n };"
                        else:
                            headerData += ",\n"
                case "RGB":
                    print("Converting 24-Bit BMP")
                    # Tuple of what a white pixel is in this BMP mode
                    whitePixelValue = (255,255,255)  
                    for a in range (height):
                        headerData += "  0b"
                        for b in range (width):
                            if (imageList[(a*width) + b]== whitePixelValue):
                                headerData += "0"
                            else:
                                headerData += "1"  
                        if (a == (height - 1)):
                            headerData += "\n };"
                        else:
                            headerData += ",\n"
                # Look into how to discern between 16 Color and 256 Color BMPs
                # Write both cases accordingly below
                case _:
                    print("Invalid BMP File Detected")
        case "PNG":
            print("Converting PNG...")
        case "JPEG":
            print("Converting JPG...")
        case _:
            # Throw an error for this part of the function (remind user to use an image file format)
            print("Error: File Format Unsupported. Are you sure you're using a PNG, JPEG or BMP file?")
        
    headerData += "\n};"
    return headerData
    # return imageList
    # return imageNumpyArray

output = ImagetoBinary(inputPath,"testFrames")
print(output)

# Write contents to the file
# outputFile = open(outputPath, "w")
# outputFile.write(output)
# outputFile.close()