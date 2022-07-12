"""
File: babynames.py
Name: Kevin
--------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any value.
    """

    baby = name_data
    baby_info = {}
    if name in baby:  # 若名字存在字典的KEY值中
        if year in baby[name]:  # 拆解巢狀字典，若年份已存在
            value = baby[name][year]  # 取出原本名字下那個年份排名
            if int(value) < int(rank):  # 若新排名比較後面
                baby[name][year] = value  # 取舊排名
            else:  # 反之亦然
                baby[name][year] = rank
        else:  # 若年份未存在，新增一筆資料
            baby[name][year] = rank
    else:  # 若名字未存在。新增一筆資料
        baby_info[year] = rank
        baby[name] = baby_info


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.
    """
    row = 0
    with open(filename, 'r') as f:
        for line in f:
            if row == 0:  # 若在第0行，先把年份取出來
                year = line[0:4]
            else:
                info = line.split(',')  # 以逗點當token
                rank = info[0].strip()
                name1 = info[1].strip()
                name2 = info[2].strip()
                add_data_for_name(name_data, year, rank, name1)  # 新增一筆男生資料
                add_data_for_name(name_data, year, rank, name2)  # 新增一筆女生資料
            row += 1


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}
    for file in filenames:
        add_file(name_data, file)
    return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string
    """
    matching_names = []
    for name in name_data:  # 取出name_data的KEY值
        if name.upper().find(target.upper()) != -1:  # 將名字轉換成大寫且有搜尋到名字
            matching_names.append(name)  # 放到matching_name裡
    return matching_names


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
