"""
File: boggle.py
Name: Kevin
----------------------------------------
此程式會先請玩家輸入一個 4 x 4 的方形字母拼盤，
接著玩家要去串連在字母盤上相連的字母，來找出所有
存在於這個拼盤上的英文單字。
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
word = []                     # 字典變數


def main():
	"""
	串連在字母盤上相連的字母，來找出所有存在於這個拼盤上的英文單字。
	"""

	####################
	boggle = {}  # 給定一個空字典存玩家輸入的字母
	player_input(boggle)  # 玩家輸入字母
	# print(boggle)
	read_dictionary()
	# boggle[0] = ['f', 'y', 'c', 'l']
	# boggle[1] = ['i', 'o', 'm', 'g']
	# boggle[2] = ['o', 'r', 'i', 'l']
	# boggle[3] = ['h', 'j', 'h', 'u']
	# print(boggle)
	start = time.time()
	find_anagrams(boggle)


	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def player_input(dict):
	"""
	請玩家依序且依規則輸入16個字母
	:param dict: dictionary, 要存入字母的變數，以字典結構存放
	"""
	for i in range(4):  # 共分4列
		while True:
			wording = str(i+1) + ' raw of letters: '
			s = list(input(wording).lower().split(" "))  # 請玩家輸入並且為case-insensitive
			check = [w for w in s if len(w) > 1]
			if len(s) != 4 or len(check) >= 1:  # 檢查輸入的字串長度是否有用空格隔開且整列長度不超過4
				print('Illegal input')  # 重新輸入
			else:
				break
		dict[i] = s  # 以每行行號當key值


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""

	with open(FILE, 'r') as f:
		for line in f:
			line = line.replace("\n", "")
			if len(line) >= 4:    # 只取長度大於4的數字進來
				word.append(line)


def find_anagrams(s):
	"""
	:param s: dictionary, 使用者輸入的字母
	:param current_list: list, 存已處理過字母的(x,y)
	:param s_list: list, 存已處理過字母
	:param ans_list: list, 存function找出來的答案
	:param x: int, 使用者輸入的字母的row number
	:param y: int, 使用者輸入的字母的column number
	"""
	ans_list = []  # 用來存最終答案
	# 把4x4的字母盤一一取出作為起點
	for i in range(4):
		for j in range(4):
			x = 0 + i
			y = 0 + j
			find_anagrams_helper(s, [], [], ans_list, x, y)
	print(f'There are {len(ans_list)} words in total.')


def find_anagrams_helper(s, current_list, s_list, ans_list, x, y):
	"""
	:param s: dictionary, 使用者輸入的字母
	:param current_list: list, 存已處理過字母的(x,y)
	:param s_list: list, 存已處理過字母
	:param ans_list: list, 存function找出來的答案
	:param x: int, 使用者輸入的字母的row number
	:param y: int, 使用者輸入的字母的column number
	"""
	s_word = ''.join(map(str, s_list))  # 將list轉換成str
	if s_word in word and s_word not in ans_list:  # 若找出來的結果存在字典裡且不在原本存答案的list中就是新發現的答案
		print(f'Found "{s_word}" ')
		ans_list.append(s_word)
		find_anagrams_helper(s, current_list, s_list, ans_list, x, y)

	else:
		if len(current_list) == 0:  # 若字串長度=0，代表是起點，取第一組(x,y)進來
			# choose
			current_list.append((x, y))
			s_list.append(s[x][y])
			find_anagrams_helper(s, current_list, s_list, ans_list, x, y)
		else:  # 若字串長度!=0，針對目標字母周圍字母做處理判斷
			# choose
			# 針對目標字母周圍字母做處理判斷是否往下走，共9個
			for i in range(-1, 2, 1):
				for j in range(-1, 2, 1):
					if x + i < 0 or y + j < 0 or x + i == 4 or y + j == 4 or (x+i, y+j) in current_list:  # 若x,y數值超出字母盤邊界，或已經找過的(x,y)則跳過
						# print('skip', (x, y),(x+i,y+j),  'i:', i, 'j:', j, s_list)  # 檢視跳過哪些座標
						pass
					elif x + i == x and y + j == y:  # 若遇到自己也跳過
						# print('skip', (x, y),(x+i,y+j), 'i:', i, 'j:', j, s_list)  # 檢視跳過哪些座標
						pass
					else:  # 針對目標座標進行判斷
						x1 = x + i
						y1 = y + j
						# print('exp', (x, y), (x1, y1), 'i:', i, 'j:', j, s_list)  # 檢視要處理的座標
						current_list.append((x1, y1))
						s_list.append(s[x1][y1])
						a = has_prefix(''.join(map(str, s_list)))  # 將目前找到的字母帶入字典比對
						if a:  # 若比對的到則繼續
							# print(''.join(map(str, s_list)),'True',x1,y1)  # 檢視比對到的座標和字母
							find_anagrams_helper(s, current_list, s_list, ans_list,x1,y1)
						else:  # 若比對不到則跳過
							# print(''.join(map(str, s_list)), 'False')  # 檢視跳過的字母
							pass
						# un-choose
						current_list.pop()
						s_list.pop()


def has_prefix(sub_s):
	"""
	將字串比對字典裡的相同長度開頭單字是否一樣
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for w in word:
		if w.startswith(sub_s):  # 若與字典裡相同長度開頭字母一樣則返回True
			return True
	return False


if __name__ == '__main__':
	main()
