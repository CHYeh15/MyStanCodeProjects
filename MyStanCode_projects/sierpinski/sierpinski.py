"""
File: sierpinski.py
Name: Kevin
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 3                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow
DELAY = 1000

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	依據參數，畫出不同 order 的 Sierpinski Triangle
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: int, order of Sierpinski Triangle
	:param length: int, The length of Sierpinski Triangle
	:param upper_left_x: int, The upper left x coordinate of Sierpinski Triangle
	:param upper_left_y: int, The upper left y coordinate of Sierpinski Triangle
	"""
	if order == 0:  # base case!
		pass
	else:
		# 先點出倒三角形頂點(X,Y)座標
		upper_right_x = upper_left_x + length  # 點出倒三角形右上頂點X座標
		upper_right_y = upper_left_y  # 點出倒三角形右上頂點Y座標
		bottom_middle_x = upper_left_x + length * 0.5  # 點出倒三角形下方頂點X座標
		bottom_middle_y = upper_left_y + length * 0.866  # 點出倒三角形下方頂點Y座標

		# 將倒三角形頂點(X,Y)座標連線
		line_upper = GLine(upper_left_x, upper_left_y, upper_right_x, upper_right_y)  # 倒三角形上方邊線
		line_left = GLine(upper_left_x, upper_left_y, bottom_middle_x, bottom_middle_y)  # 倒三角形左方邊線
		line_right = GLine(upper_right_x, upper_right_y, bottom_middle_x, bottom_middle_y)  # 倒三角形右方邊線
		window.add(line_upper)
		window.add(line_left)
		window.add(line_right)
		pause(DELAY)

		sierpinski_triangle(order - 1, length / 2, upper_left_x, upper_left_y)  # 畫左邊倒三角形
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 2, upper_right_y)  # 畫右邊倒三角形
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 2 * 0.5, upper_left_y + length / 2 * 0.866)  # 畫下方倒三角形


if __name__ == '__main__':
	main()