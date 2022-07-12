"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: img, background
    :param figure_img: img, figure
    :return:  new_img
    """
    new_img = SimpleImage.blank(background_img.width, background_img.height)
    for x in range(new_img.width):
        for y in range(new_img.height):
            b_p = background_img.get_pixel(x, y)
            f_p = figure_img.get_pixel(x, y)
            n_p = new_img.get_pixel(x, y)
            if f_p.green > max(f_p.red, f_p.blue)*2:
                n_p.red = b_p.red
                n_p.green = b_p.green
                n_p.blue = b_p.blue
            else:
                n_p.red = f_p.red
                n_p.green = f_p.green
                n_p.blue = f_p.blue

    return new_img


def main():
    """
    Check whether the figure pixel is green; if so, the corresponding position will be
    Pixels are replaced by MillenniumFalcon images
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
