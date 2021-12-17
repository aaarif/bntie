# Coding Test 1, 2 

def convertBinaryToDecimal(binary_number):
	# Quention 1.a
	binary_string = str(binary_number)
	b = {'0','1'}
	t = set(binary_string)
	if b != t and t != {'0'} and t != {'1'}:
		return "Cannot convert non binary to decimal"
	biggest_pow = len(binary_string) - 1
	dec_num = 0
	for num in binary_string:
		if num == '1':
			mult = pow(2, biggest_pow)
			dec_num += mult
		biggest_pow -=1
	return dec_num


def convertDecimalToBinary(decimal_number):
	# Question 1.b
	# return string_binary
	str_bin= ''
	import math
	while(decimal_number > 0):
		if decimal_number != 0:
			if decimal_number%2 == 0:
				str_bin += '0'
			else:
				str_bin += '1'
		else:
			str_bin += '1'
		decimal_number = math.floor(decimal_number/2)
	return str_bin[::-1]


def longestPalindrome(string):
  	#Question 2
	string_without_space = string.replace(" ", "")
	maxLength = 1
 
	start = 0
	length = len(string_without_space)
 
	low = 0
	high = 0
 
	for i in range(1, length):

		low = i - 1
		high = i
		while low >= 0 and high < length and string_without_space[low] == string_without_space[high]:
			low -= 1
			high += 1
		low += 1
		high -= 1
		if string_without_space[low] == string_without_space[high] and high - low + 1 > maxLength:
		  start = low
		  maxLength = high - low + 1
 

		low = i - 1
		high = i + 1
		while low >= 0 and high < length and string_without_space[low] == string_without_space[high]:
			low -= 1
			high += 1

		low += 1
		high -= 1
		if string_without_space[low] == string_without_space[high] and high - low + 1 > maxLength:
		  start = low
		  maxLength = high - low + 1
 
	longest_palindrome = string_without_space[start:start + maxLength] 
	words = string.split(" ")
	locations = []
	# print(f"Words: {words}")
	for index,word in enumerate(words): 
		if word in longest_palindrome:
			locations.append(index)
	# print(f"locations: {locations}")
	if len(locations) > 1:
		real_pal = longest_palindrome.replace(words[locations[0]],"")
		print(f'Real Palindrome: {real_pal}')
		# if words[locations[1]] 
		longest_palindrome = words[locations[0]]+' '+words[locations[1]]

	return longest_palindrome



result = convertBinaryToDecimal(10011)
print(f"result convertBinaryToDecimal: {result}")

result2 = convertDecimalToBinary(19)
print(f"result convertDecimalToBinary: {result2}")


text = "aku suka makan nasi"
text = "di rumah saya ada kasur rusak"
# text = "abcde edcbza"
longest_pal = longestPalindrome(text)
print(f"LOngest Palindrome: {longest_pal}")
