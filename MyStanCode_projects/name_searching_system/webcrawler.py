"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")
        # tags = soup.find_all('tbody')
        tags = soup.tbody.text  # 取出tbody裡的所有文字
        info = tags.split()  # 將文字切開
        # 只取出Source以前的文字
        while True:
            delete = info.pop()
            if delete == 'Source:':
                break
        # print(info)
        cnt_male = 0  # 設定計算男生名字數量的變數
        cnt_female = 0  # 設定計算女生名字數量的變數
        for i in range(2, len(info)):
            # 觀察資料發現男生名字數量從'2' index開始，且會隔5個字串
            if (i - 2) % 5 == 0:
                cnt_male += str_2_num(info[i])
            # 觀察資料發現女生名字數量從'4' index開始，且會隔5個字串
            elif (i - 4) % 5 == 0:
                cnt_female += str_2_num(info[i])
        print('Male Number: ', str(cnt_male))
        print('Female Number: ', str(cnt_female))


        # ----- Write your code below this line ----- #


def str_2_num(s):
    """
    轉換會計格式成數值型態

    Input:
        s (str): 以會計格式呈現的數值

    Returns:
        n (int): 去掉逗點的數值
    """
    l = s.split(',')
    n = int(l[0])*1000+int(l[1])
    return n


if __name__ == '__main__':
    main()
