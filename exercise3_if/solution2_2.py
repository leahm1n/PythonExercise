def is_prime(number):
    """判断number是不是素数, 若是则返回True, 否则返回False"""
    flag = True #是素数标识
    for i in range(2, number):  #让i在数列2到number循环迭代
        if number % i == 0: #如果number除以i余数为0
            flag = False #不是素数标识
            break  #跳出循环
    return flag #返回标识

nums = int(input('输入数字N:'))  #函数input()接受一个参数，返回值是整型，并储存到num中

primes_list = [] #设置一个空列表，并储存到primes_list中。
for num in range(2, nums + 1): #让num在数列2到num+1中循环迭代
    if is_prime(num): #如果是素数
        primes_list.append(num) #把是素数的添加到primes_list中


#1. print("从2~{}之间的所有素数：{}".format(参数1, 参数2))
#2. print("从2~{}之间的所有素数：{}".format(nums, 参数2))
#3. 参数2 --> "2 3 5 7" ==> [2, 3, 5, 7] --> "2 3 5 7"
#4. " ".join(['2', '3', '5', '7']) --> "2 3 5 7" ==> [2, 3, 5, 7] --> ['2', '3', '5', '7']
#5. [str(n) for n in primes_list] ==> [2, 3, 5, 7] --> ['2', '3', '5', '7']
print("从2~{}之间的所有素数：{}".format(nums, " ".join([str(n) for n in primes_list]))) #打印字符串