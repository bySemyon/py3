#группа задач, которые должны выполняться с числами:
def reverse_number(num):
    reversed_num = int(str(num)[::-1])
    return reversed_num

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def process_numbers(numbers):
    reversed_numbers = []
    for num in numbers:
        reversed_num = reverse_number(num)
        if is_palindrome(num):
            print(f"{num} является палиндромом!")
        reversed_numbers.append(reversed_num)
    return reversed_numbers


#ввод чисел
def input_numbers():
    numbers = []
    n = int(input("Введите количество чисел: "))
    print("Введите числа:")
    for _ in range(n):
        num = int(input())
        numbers.append(num)
    return numbers
numbers = input_numbers()
reversed_numbers = process_numbers(numbers)
print("Перевернутые числа:", reversed_numbers)