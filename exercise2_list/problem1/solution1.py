#exercise2.1
numbers = []   #定义变量numbers,值为空列表[]
while True:    #while循环判断条件为True，即为无限循环
    cli = input("请输入大于0的数字(输入q结束输入): ")  #函数input()接受一个参数，向用户说明或提示，输入储存到变量cli中
    if cli == 'q': #如果变量cli等于q
        break #跳出循环
    
    numbers.append(int(cli)) #将变量cli转换成整型并用append()方法添加到列表numbers中

print("本次录入结果: " + str(numbers)) #打印出字符串，注意不是字符串形式要转换成字符串形式


numbers.sort(reverse = True) #与顺序相反的顺序排列列表内元素，向sort()的方法传递参数(reverse = Ture)
print("降序排序: " + str(numbers)) #打印出想要的字符串
numbers.sort() #将列表numbers内的元素用sort()方法按顺序排序
print("升序排序: " + str(numbers)) #打印出想要的字符串


del(numbers[0]) #用del的方法删除列表numbers中第一个元素
del(numbers[-1]) #用del的方法删除列表numbers中倒数第一个
print("删除首尾数字后的列表: " + str(numbers)) #打印出想要的字符串


numbers.insert(0, 0) #用insert()的方法在列表numbers第一个元素之前加入一个元素0
print("在列表开头加入数字0: " + str(numbers)) #打印想要的字符串


sum = 0 #设一个变量sum等于0
for num in numbers[-3:]: #在切片[-3:](即后面三个元素)循环迭代
    sum += num 
    #sum = sum + num  
average = sum / 3 #求出平均值
print("列表最后3个数字的平均值为: " + str(average)) #打印想要的字符串