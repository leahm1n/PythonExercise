from time import strptime #导入模板

time_format = "%Y-%m-%d"  #时间格式
mdays = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31) #将每月的号数储存到mdays中

today = input("输入年月日: ") #用函数input()获取参数，向用户说明或提示，输入储存到变量today中
today_stime = strptime(today, time_format) #将时间字符串转换成时间元组

#days = sum(mdays[:today_stime.tm_mon - 1]) + today_stime.tm_mday 
days = 0 #定义days为0
for i in range(today_stime.tm_mon - 1): #让i在数列today_stime.tm_mon-1(用户输入的月份减一)
    days = days + mdays[i] #days等于days加上用户输入月份减一的之前的号数之和
days = days + today_stime.tm_mday #days等于用户输入的时间

FEBRURY = 2  #FEBRURY等于2
if today_stime.tm_mon > FEBRURY \
   and ((today_stime.tm_year % 4 == 0 \
   and today_stime.tm_year % 100 != 0) \
   or today_stime.tm_year % 400 == 0):  #如果用户输入的年份除以4余0,并且年份除以100余数不为零，或者年份除以100余0
    days = days + 1 

print("这一天为{}年的第{}天。".format(today_stime.tm_year, days))  #打印字符串
   