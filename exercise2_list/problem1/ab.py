num = [23, 13, 45, 14, 65, 35]
s_num = "本次录入结果是：" + str(num)
print(s_num)

num.sort(reverse=True)
c_num = '降序排序：' + str(num)
print(c_num)

num.sort()
b_num = "升序排序：" + str(num)
print(b_num)

del num[0]
popped_num = num.pop()
d_num = '删除首尾后的排序：' + str(num)
print(d_num)

num.insert(0,0)
e_num = '在列表开头加入数字0: ' + str(num)
print(e_num)

sum = 0
for i in num[-3:]:
    sum = sum + i

average = sum / 3   
f_num = '列表数字最后3个数字的平均值：' + str(average)
print(f_num)