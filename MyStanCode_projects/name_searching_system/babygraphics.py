"""
File: babygraphics.py
Name: Kevin
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    dist = (width - GRAPH_MARGIN_SIZE * 2) / len(YEARS)  # 依據年份數量算出垂直線間的間隔距離
    x_coordinate = GRAPH_MARGIN_SIZE + year_index * dist  # 考量間隔距離算出每個年份的Ｘ座標
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(0+GRAPH_MARGIN_SIZE, 0+GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, 0+GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)  # 在底端畫一條水平線
    canvas.create_line(0+GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)  # 在頂端畫一條水平線
    cnt = 0
    for year in YEARS:
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, cnt), 0, get_x_coordinate(CANVAS_WIDTH, cnt), CANVAS_HEIGHT,
                           width=LINE_WIDTH)  # 依據年份數量畫出垂直線
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, cnt), CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=year,
                           anchor=tkinter.NW)  # 在每條垂直線旁邊加上年份文字
        cnt += 1


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    cc = 0  # 判斷用到哪一個COLOR
    for name in lookup_names:
        if cc >= len(COLORS):  # 若繪製數目大於COLOR長度，則重新回到第一個COLOR
            cc = 0
        color = COLORS[cc]
        info = name_data[name]  # 將name_data的值取出放到info中
        print(name, info)
        cnt = 0  # 記錄算到第幾個年份
        y0 = 0  # y座標值
        for year in YEARS:  # 把year從list取出
            year = str(year)  # 轉換成文字型態，配合name_data的year型態
            if year in info:  # 若找得到年份代表有rank
                # 找出文字的座標，用get_x_coordinate()取的該年份的Ｘ值，並將rank轉換成符合Ｙ軸長度
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, cnt)+TEXT_DX, (int(info[year])/1000*600) +
                                   GRAPH_MARGIN_SIZE, text=(name, info[year]), anchor=tkinter.SW, fill=color)
            else:  # 若找不到年份rank用'*'代替
                # 用(CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)*1000//600當作'*'的rank值
                info[year] = str((CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)*1000//600)
                # 找出文字的座標，用get_x_coordinate()取的該年份的Ｘ值，並將rank轉換成符合Ｙ軸長度
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, cnt)+TEXT_DX, (int(info[year]) / 1000 * 600)
                                   + GRAPH_MARGIN_SIZE, text=(name, '*'), anchor=tkinter.SW, fill=color)
            if cnt >= 1:  # 第二點往回找第一點連成線條
                canvas.create_line(get_x_coordinate(CANVAS_WIDTH, cnt-1), y0, get_x_coordinate(CANVAS_WIDTH, cnt),
                                   (int(info[year]) / 1000 * 600)+GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill=color)
            y0 = (int(info[year]) / 1000 * 600) + GRAPH_MARGIN_SIZE  # 將rank轉換成符合Ｙ軸長度，找出Ｙ值
            cnt += 1  # 記錄算到第幾個年份
        print(cc, len(COLORS))
        cc += 1


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
