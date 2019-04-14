from time import strptime #导入模板

time_format = "%Y-%m-%d" #时间格式

today = input("输入年月日: ") #用函数input()获取参数，向用户说明或提示，输入储存到变量today中
today_stime = strptime(today, time_format) #将时间字符串转换成时间元组

print("这一天为{}年的第{}天。".format(today_stime.tm_year, today_stime.tm_yday)) #打印字符串