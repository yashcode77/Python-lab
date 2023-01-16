num = int(input("Enter the number: "))
def fibo(num):
    if num<=1:
        return num
    else:
        return (fibo(num-1) + fibo(num-2))

for i in range(num):
       print(fibo(i))
