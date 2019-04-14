nums = int(input('输入数字N:'))  #函数input()接受一个参数，返回值是整型，并储存到num中

primes_list = [] #设置一个空列表，并储存到primes_list中

for num in range(2, nums + 1): #让num在数列2~num+1中循环迭代
    is_prime = True #是素数就是真
    for i in range(2, num): #i在数列num中循环迭代
        if num % i == 0:  #如果num除以i，余数为0
            is_prime = False #否则就是假
            break #跳出循环
    
    if is_prime: #如果是素数
        primes_list.append(num) #把是素数的话就就添加到primes_list的列表中

print("从2~{}之间的所有素数：{}".format(nums, " ".join([str(n) for n in primes_list]))) #打印字符串


