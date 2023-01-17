def menu(choice):
   match choice:
      case 1:
         str = input("Enter a string or number: ")
         print(is_palindrome(str))
      case 2:
         num = int(input("Enter the number: "))
         fact = factorial(num)
         print("The factorial of {} is {}".format(num,fact))
      case 3:
         print("Thank you for using this program")
      case default:
         print("Enter a valid choice")

def is_palindrome(str):
   return str==str[::-1]

def factorial(num):
   ans = 1
   for i in range(1,num+1):
      ans *= i
   return ans

choice = 1
while choice!=3:
   print("1. Check palindrome")
   print("2. Find factorial")
   print("3. Exit")
   choice = int(input("Enter your choice: "))
   menu(choice)