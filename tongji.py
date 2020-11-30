file = open(r'C:\Users\Administrator\Desktop\Walden.txt','r')
lines = file.readlines()

words = []
for line in lines:
    tmp_list = line.split(" ")
    for word in tmp_list:
        words.append(word.replace(',','').replace(',','').replace(',','').replace(',','').replace(',','').replace(',','').lower())
words
word_count = {}
word_set = set(words)
for word in word_set:
    count_num = words.count(word)
    word_count[word] = count_num
word_count
#对word_count字典进行排序，按照出现的次数进行排序
sorted(word_count.items(),key=lambda item: item[1],reverse=True)