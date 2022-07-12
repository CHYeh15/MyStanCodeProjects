"""
File: blur.py
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    Change the original pixel value to the average value of this pixel and its adjacent pixels.
    :param img: img, The image input by the user
    :return: new_img, blurred img
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(new_img.width):
        for y in range(new_img.height):
            n_p = new_img.get_pixel(x, y)
            if x == 0:  # Handle possible situations on X=0
                if y == 0:  # corner(0,0)
                    n_p.red, n_p.green, n_p.blue = avg_c(n_p, img, x, y, 0, 2, 0, 2)
                elif y == new_img.height-1:  # corner(0,y.height-1)
                    n_p.red, n_p.green, n_p.blue = avg_c(n_p, img, x, y, 0, 2, -1, 1)
                else:  # board(0,y)
                    n_p.red, n_p.green, n_p.blue = avg_b(n_p, img, x, y, 0, 2, -1, 2)
            elif x == new_img.width-1:  # # Handle possible situations on X=width
                if y == 0:  # corner(width-1,0)
                    n_p.red, n_p.green, n_p.blue = avg_c(n_p, img, x, y, -1, 1, 0, 2)
                elif y == new_img.height-1:  # (width-1,height-1)
                    n_p.red, n_p.green, n_p.blue = avg_c(n_p, img, x, y, -1, 1, -1, 1)
                else:  # board(width-1,y)
                    n_p.red, n_p.green, n_p.blue = avg_b(n_p, img, x, y, -1, 1, -1, 2)
            elif 0 < x < new_img.width - 1:
                if y == 0:  # board(x,0)
                    n_p.red, n_p.green, n_p.blue = avg_b(n_p, img, x, y, -1, 2, 0, 2)
                elif y == new_img.height-1:  # board(x,height-1)
                    n_p.red, n_p.green, n_p.blue = avg_b(n_p, img, x, y, -1, 2, -1, 1)
                else:  # inner
                    n_p.red, n_p.green, n_p.blue = avg_n(n_p, img, x, y, -1, 2)
    return new_img


def avg_c(new, img, x, y, si, ei, sj, ej):
    """
    Calculate corner value
    :param new: pixel of img, new img pixel
    :param img: img, The image input by the user
    :param x: int, the x-axis value of new img
    :param y: int, the y-axis value of new img
    :param si: int, the lower limit of the movement of the x-axis
    :param ei: int, The upper limit of the movement of the x-axis
    :param sj: int, the lower limit of the movement of the y-axis
    :param ej: int, The upper limit of the movement of the y-axis
    :return: new.red
    :return: new.green
    :return: new.blue
    """
    red = 0
    green = 0
    blue = 0
    for i in range(si, ei):
        for j in range(sj, ej):
            img_p = img.get_pixel(x + i, y + j)
            red = red + int(img_p.red)
            green = green + int(img_p.green)
            blue = blue + int(img_p.blue)
    new.red = red / 4
    new.green = green / 4
    new.blue = blue / 4
    return new.red, new.green, new.blue


def avg_b(new, img, x, y, si, ei, sj, ej):
    """
    Calculate boundary values
    :param new: pixel of img, new img pixel
    :param img: img, The image input by the user
    :param x: int, the x-axis value of new img
    :param y: int, the y-axis value of new img
    :param si: int, the lower limit of the movement of the x-axis
    :param ei: int, The upper limit of the movement of the x-axis
    :param sj: int, the lower limit of the movement of the y-axis
    :param ej: int, The upper limit of the movement of the y-axis
    :return: new.red
    :return: new.green
    :return: new.blue
    """
    red = 0
    green = 0
    blue = 0
    for i in range(si, ei):
        for j in range(sj, ej):
            img_p = img.get_pixel(x + i, y + j)
            red = red + int(img_p.red)
            green = green + int(img_p.green)
            blue = blue + int(img_p.blue)
    new.red = red / 6
    new.green = green / 6
    new.blue = blue / 6
    return new.red, new.green, new.blue


def avg_n(new, img, x, y, s, e):
    """
    Calculate the inner value of the coordinates
    :param new: pixel of img, new img pixel
    :param img: img, The image input by the user
    :param x: int, the x-axis value of new img
    :param y: int, the y-axis value of new img
    :param s: int, the movement of the x-axis
    :param e: int, the movement of the y-axis
    :return: new.red
    :return: new.green
    :return: new.blue
    """
    red = 0
    green = 0
    blue = 0
    for i in range(s, e):
        for j in range(s, e):
            img_p = img.get_pixel(x + i, y + j)
            red = red + int(img_p.red)
            green = green + int(img_p.green)
            blue = blue + int(img_p.blue)
    new.red = red / 9
    new.green = green / 9
    new.blue = blue / 9
    return new.red, new.green, new.blue


def main():
    """
    Use for loop in def main( ) to call blur function to achieve multiple blur effects.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
