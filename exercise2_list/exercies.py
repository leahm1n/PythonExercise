s_mes =( "\n请输入大于0的数字（输入q结束输入)")

mes = []
while mes != 'q':
    a_mes = input(s_mes)   
    if a_mes == 'q':
        break
    else:
        mes.append(int(a_mes))

print(mes)