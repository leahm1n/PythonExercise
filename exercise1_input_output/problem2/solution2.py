name = input('你的名字？')
age = input('你的年龄？')
number = input('你的学号？')
email = input('你的邮箱？')
x = '名字'+':'+name
y = '年龄'+':'+age
m = '学号'+':'+number
h = '邮箱'+':'+email

print(x)
print(y)
print(m)
print(h)


tall = input('你的身高？')
wegiht = input('你的体重？')

BIM = str(float(wegiht)/(float(tall)**2))
massage = '你的BIM值为' + ':' + BIM
print(massage)