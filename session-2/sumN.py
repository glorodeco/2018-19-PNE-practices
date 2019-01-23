def sum(n):


    numb=0

    for num in range(n):
        numb=num+numb+1


    return numb
#        Main Programme

num=int(input('Introduce a numb:'))
total_sum=sum(num)
print('Total sum is:', total_sum)
