def numodd(number):
    return number % 2 != 0
def oddsum(numbers):
    return sum(number for number in numbers if numodd(number)).split()
numbers = input("Enter numbers : ")
numbers = list(map(int, numbers))
odd_sum = oddsum(numbers)
print("The sum of odd numbers is: {odd_sum}")