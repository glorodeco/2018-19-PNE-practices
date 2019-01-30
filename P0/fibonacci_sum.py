def fibonacci(n):
    position_1 = 0
    position_2 = 1
    actual_number = 0
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n>2:
        for i in range(n-2):
            actual_number = position_1 + position_2
            position_1 = position_2
            position_2 = actual_number
        return actual_number

term = int(input("Your term is: "))
sum_num = 0
if term == 1:
    sum_num = 0
elif term == 2:
    sum_num = 1
elif term > 2:
    for i in range(3, term+1):
        value = fibonacci(i)
        sum_num += value
print("The result of the sum is ", sum_num)