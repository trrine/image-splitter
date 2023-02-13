# Image Splitter
Python program that can split an image into multiple new images.

## Description
This program splits a given image or each image in a given directory into a given number of new images and saves them. The user provides the name/path of a file or a directory as input. If the path is a file, and if the file can be found and if it is and image file (jpg/jpeg, png, or bmp), the image will be split into a number of new images. This number is also specified by the user and must be a number that is a 4th power. If the path is a directory, each image in the directory will be split into the specified number of new images. The new images are saved in the original location. When saving the new images, the program takes measures to prevent overwriting existing files of the same names. 

## Getting Started

### Dependencies
- Python 3
- OpenCV

### Executing the Program
The program runs from the command line where the user provides the filename/path of the image to be split or a path to a directory with images and the number of new output images from the split as arguments. At the moment, it is only possible for the user to choose a number that is a 4th power, such as 4, 16, 64. To split a given image into four new images, type the following command:
- image_splitter.py imagefile 4
- E.g. image_splitter.py image1.jpg 4
