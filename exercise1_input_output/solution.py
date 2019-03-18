name = input('你的名字：')
age = int(input('你的年龄：'))
year = str((2019 - age) + 100)

msg = name + '，' + '你将会在' + year + '年到100岁。'
print(msg)

times = int(input('请输入重复打印信息次数：'))

print(times * msg)
print(times * (msg + '\n'))
