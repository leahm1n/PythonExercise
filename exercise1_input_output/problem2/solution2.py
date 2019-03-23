name = input('你的名字？')
age = input('你的年龄？')
number = input('你的学号？')
email = input('你的邮箱？')


#程序运行结果正确，但是程序里使用了一些如x, y, m, h之类的变量名来存储要打印的字符串
#变量名字要起得有含义写，比如name_str, age_str, email_str之类的。
print('名字'+':'+name)
print('年龄'+':'+age)
print('学号'+':'+number)
print('邮箱'+':'+email)

tall = input('你的身高？')
wegiht = input('你的体重？')

BIM = str(float(wegiht)/(float(tall)**2))
massage = '你的BIM值为' + ':' + BIM
print(massage)