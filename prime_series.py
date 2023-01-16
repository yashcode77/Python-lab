num = int(input("Enter the number till which you want to print prime: "))
def is_prime(num):
    flag = True
    for i in range(2,num):
        if(num % i == 0):
            flag = False
    return flag

for i in range(2,num+1):
    if(is_prime(i)):
        print(i)
