size_list = [int(i) for i in input().split()]
word_list = [size_list[ord(char)-ord('a')]for char in input()]
print(max(word_list)*len(word_list))