
import random
from mpmath import mp
from PIL import Image


def get_pi_list():
    return [i for i in str(mp.pi)]

def get_pixel_data(current_digit):
    for k, v in colors_of_digits.items():
        if current_digit == k:
            return v

        elif current_digit == ".":
            return (255, 255, 255)

        else:
            pass

def set_pixels_data():
    pixels = [get_pixel_data(digit) for digit in pi]

    img.putdata(pixels)

def main_run():
    set_pixels_data()


colors_of_digits = {
    "0": (255, 255, 255), # white
    "1": (255, 0, 0), # red
    "2": (255, 135, 5), # orange
    "3": (255, 255, 5), # yellow
    "4": (110, 235, 60), # green
    "5": (5, 75, 5), # dark green
    "6": (45, 160, 255), # blue
    "7": (15, 40, 75), # dark blue
    "8": (125, 25, 215), # purple
    "9": (255, 75, 255), # pink
}

img_size = 128
img_res = (img_size, img_size)

# Number of pi numbers
mp.dps = (img_size * img_size) - 1

pi = get_pi_list()


# main
if __name__ == "__main__":
    img = Image.new("RGB", img_res)

    # Run
    main_run()

    # Show the image
    img.show()

    # Save the image
    # If you want to save this image, just uncomment "#img.save("PI.png")"
    #img.save("PI.png")
