import os
import sys
import cv2

IMAGE_FORMATS = [".jpg", ".jpeg", ".bmp", ".png"]

class Image:
    def __init__(self, image, name):
        self.image = image
        self.name = name
        self.height = self.image.shape[0]
        self.width = self.image.shape[1]
        self.center_x = self.width // 2
        self.center_y = self.height // 2

    def get_image(self):
        return self.image

    def get_name(self):
        return self.name

    def show_image(self):
        cv2.imshow("Image", self.image)
        cv2.waitKey(0)

    def split(self):
        new_images = []

        top_left = Image(self.image[0:self.center_y, 0:self.center_x], self.name + "_1")
        new_images.append(top_left)

        top_right = Image(self.image[0:self.center_y, self.center_x:self.width], self.name + "_2")
        new_images.append(top_right)

        bottom_left = Image(self.image[self.center_y:self.height, 0:self.center_x], self.name + "_3")
        new_images.append(bottom_left)

        bottom_right = Image(self.image[self.center_y:self.height, self.center_x:self.width], self.name + "_4")
        new_images.append(bottom_right)

        return new_images


class ImageSplitter:
    def __init__(self, input_file, output_number):
        self.file_name, self.file_extension = os.path.splitext(input_file)
        self.output_number = output_number
        self.original_image = Image(cv2.imread(input_file), self.file_name)
        self.output_images = []

    def split_image(self):
        new_images = self.original_image.split()

        while True:
            if len(new_images) >= self.output_number:
                break

            images = []

            for image in new_images:
                images += image.split()

            new_images = images

        self.output_images = new_images

    def save_images(self):
        for image in self.output_images:
            name = image.get_name() 
            
            while True:
                if os.path.isfile(name + self.file_extension): 
                    name += "_I"
                
                else:
                    break

            output_file = name + self.file_extension
            cv2.imwrite(output_file, image.get_image())

        print("Saved", self.output_number, "new images in location:", os.getcwd())


def valid_file(file_path):
    if not os.path.isfile(file_path):
        print("File not found. Make sure you are in the right directory.")
        return False

    _, extension = os.path.splitext(file_path)

    if extension not in IMAGE_FORMATS:
        print("File must be of one of the following types: jpg/jpeg, bmp, or png.")
        return False

    return True


def valid_output_number(number):
    if number > 64:
        print("Output image number must not exceed 64.")
        return False
    
    if number % 4 == 0:
        return True

    print("Output image number must be divisible by 4 (e.g., 4, 16, 32, 64).")
    return False


def main():
    args = sys.argv
    image_path = args[1]
    output_number = int(args[2])

    if valid_file(image_path) and valid_output_number(output_number):
        splitter = ImageSplitter(image_path, output_number)
        splitter.split_image()
        splitter.save_images()

    
if __name__ == '__main__':
    main()