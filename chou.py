file= open(r'C:\Users\Administrator\Desktop\o.xlsx','r')
lines = file.readlines()
#抽取每行的学号和姓名，保存到字典
student={}
for line in lines:
    tmp_list = line.spilt(',')
    xuehao = tmp_list[0]
    xingming = tmp_list[1]
    students[xuehao] = xingming

print(students)
#从学号中随机抽n个学号
import random
num = int(input("人数："))
xuehao_list = random.sample(students.keys(),num)
xuehao_list
#根据随机抽取的学号，打印输出对应的姓名
for xuehao in xuehao_list:
    print(students[xuehao])