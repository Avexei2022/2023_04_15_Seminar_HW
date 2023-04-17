import get_number_int

def print_task_condition():
    print("\nЗадача 1. Создайте список.\n"
          "Запишите в него N первых элементов последовательности Фибоначчи.\n"
          "6 –> 1 1 2 3 5 8\n")

def fibonacci(number):
    if number < 2:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)

def recursion_method(number) -> list:
    return [fibonacci(i) for i in range(number)]

def iteration_method(number):
    fib = [0, 1]
    for i in range(1, number - 1):
        fib.append(fib[i-1] + fib[i])
    return fib

def print_result(message, number, result_list):
    print(f"{message}{number} -> ", end="")
    print(*result_list)

print_task_condition()
num_min = 2
num_max = 30
message = f"Введите количество элементов N (от {num_min} до {num_max}):"
mes_false = "Условия ввода не выполнены."
n = get_number_int
number = n.get_number(message, num_min, num_max, mes_false)
print_result('Рекурсия: ', number, recursion_method(number))
print_result('Итерация: ', number, iteration_method(number))


