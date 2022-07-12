"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str,
    :return img: SimpleImage,
    """
    img = SimpleImage(filename)
    r_img = SimpleImage.blank(img.width // 2, img.height // 2)

    r_img.show()
    for x in range(r_img.width):
        for y in range(r_img.height):
            # 彩色 pixel
                x1 = x * 2
                y1 = y * 2

                img_p = img.get_pixel(x1, y1)
                # 空白 pixel
                r_p = r_img.get_pixel(x, y)
                r_p.red = img_p.red
                r_p.green = img_p.green
                r_p.blue = img_p.blue
    return r_img


def main():
    """
    Reduce the width and height of the original image by 1/2 to generate a new image.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
