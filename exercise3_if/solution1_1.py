from time import strptime #导入模板

time_format = "%Y-%m-%d" #时间格式\
mdays = (31, (28, 29), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31) #将每月号数储存到mdays中

today = input("输入年月日: ")  #用函数input()获取参数，向用户说明或提示，输入储存到变量today中
today_stime = strptime(today, time_format) #将时间字符串转换成时间元组

#today_stime.tm_year 年
#today_stime.tm_mon 月
#today_stime.tm_mday 日

feb_mday_index = 0 #定义feb_mday_index为0

if (today_stime.tm_year % 4 == 0 \
   and today_stime.tm_year % 100 != 0) \
   or today_stime.tm_year % 400 == 0:   #如果用户输入的年份除以4余0,并且年份除以100余数不为零，或者年份除以100余0  
    feb_mday_index = 1 #则feb_mday_index为真

days = 0 #定义days为0
for i in range(today_stime.tm_mon-1): #让i在数列today_stime.tm_mon-1(用户输入的月份减一)
    if i == 1: #如果i等于1 ，即二月份
        days = days + mdays[i][feb_mday_index]  #days等于days加二月份的天数(29天)
    else: #否则
        days = days + mdays[i] #days等于days加二月份的28天
days = days + today_stime.tm_mday  #days等于加上当前月份的天数
#s_today = '这一天为' + str(today_stime.tm_year) + '年的第' + str(days) + '天。'
s_today = "这一天为{}年的第{}天。".format(today_stime.tm_year, days) #格式化字符串，并储存到s_today中
print(s_today) #打印

