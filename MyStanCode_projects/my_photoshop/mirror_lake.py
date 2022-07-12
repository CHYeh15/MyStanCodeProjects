"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, The address input by the user
    :return: r_img
    """
    img = SimpleImage(filename)
    r_img = SimpleImage.blank(img.width, img.height*2)
    r_img.show()
    for x in range(img.width):
        for y in range(img.height):
            # 彩色 pixel
            img_p = img.get_pixel(x, y)
            # 空白 pixel
            r_p = r_img.get_pixel(x, y)
            r_p.red = img_p.red
            r_p.green = img_p.green
            r_p.blue = img_p.blue
            r_p = r_img.get_pixel(x, r_img.height-1-y)
            r_p.red = img_p.red
            r_p.green = img_p.green
            r_p.blue = img_p.blue
    return r_img


def main():
    """
    Place an image side-by-side with its upside-down image to create the illusion of a mirror image.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
