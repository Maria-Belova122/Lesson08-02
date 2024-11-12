# ЗАДАНИЕ ПО ТЕМЕ "Сложные моменты и исключения в стеке вызовов функции"

def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in range(len(numbers)):
        try:
            result += numbers[i]
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы – {numbers[i]}')
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    try:
        list_items = []
        quantity_items = 0
        for item in numbers:
            list_items.append(item)
            quantity_items += 1
        total = personal_sum(list_items)
        average = total[0] / (quantity_items - total[1])
    except ZeroDivisionError:
        average = 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        average = None
    return average


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
