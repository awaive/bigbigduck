%%writefile 2.py
#打开并读取文件
file=open(r'C:\Users\Administrator\Desktop\o.xlsx','r')
lines=file.readlines()
#给每行添加行号，如#1#2
#用#去对齐
#最长行的长度
max_len = 0
for line in lines:
    if len(line)>max_len:
        max_len = len(line)
print(max_len)
    
line_num = 0
new_lines = []
for line in lines:
    line_num += 1
    tmp_line = line.rstrip() + '#' +str(line_num)
    print(tmp_line)
