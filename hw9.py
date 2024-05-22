"""
Функція жадібного алгоритму find_coins_greedy. 
Ця функція повинна приймати суму, яку потрібно видати покупцеві, і повертати словник із кількістю монет кожного номіналу,
що використовуються для формування цієї суми. Наприклад, для суми 113 це буде словник {50: 2, 10: 1, 2: 1, 1: 1}.
Алгоритм повинен бути жадібним, тобто спочатку вибирати найбільш доступні номінали монет.
Функція динамічного програмування find_min_coins.
Ця функція також повинна приймати суму для видачі решти, але використовувати метод динамічного програмування,
щоб знайти мінімальну кількість монет, необхідних для формування цієї суми.
Функція повинна повертати словник із номіналами монет та їх кількістю для досягнення заданої суми найефективнішим способом.
Наприклад, для суми 113 це буде словник {1: 1, 2: 1, 10: 1, 50: 2}

"""

def find_coins_greedy(input_sum):
    """Find coints by greedy alg"""
    coints = {}
    iterator = iter(monets)
    current = next(iterator)
    while input_sum > 0:
        if current <= input_sum:
            input_sum = input_sum - current
            coints[current] = coints[current] + 1 if current in coints else 1
        else:
            current = next(iterator)
    return coints

def find_min_coins(input_sum):
    pass


monets = [50, 25, 10, 5, 2, 1]

example_sum = 113 # input("Input sum to calculate")
print(f"Input sum: {example_sum}, monets:{find_coins_greedy(example_sum)}")
print(f"Input sum: {example_sum}, monets:{find_min_coins(example_sum)}")
