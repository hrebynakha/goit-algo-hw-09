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
from timeit import timeit

coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(input_sum):
    """Find coins by greedy alg"""
    result = {}
    iterator = iter(coins)
    current = next(iterator)
    while input_sum > 0:
        if current <= input_sum:
            input_sum = input_sum - current
            result[current] = result[current] + 1 if current in result else 1
        else:
            current = next(iterator)
    return result

def find_min_coins(input_sum):
    """Find coins using dynamic programming"""
    # Ініціалізація масиву для зберігання мінімальної кількості монет для кожної суми
    min_coins = [float('inf')] * (input_sum + 1)
    # базовий випадок
    min_coins[0] = 0
    # пустий список для зберігання останньої використоаної монети
    last_used = [0] * (input_sum + 1)
    result = {}
    for x in range(1, input_sum + 1):
        # print(x, "Min coins:\n", min_coins, "\nLast used\n", last_used)
        if x in coins:
            min_coins[x] = 1
            last_used[x] = x
            continue
        last = x - 1
        min_coins[x] = min_coins[last] + 1
        last_used[x] = last_used[last]

    result = {}
    while input_sum > 0:
        coin = last_used[input_sum]
        result[coin] = result[coin] + 1 if coin in result else 1
        input_sum -= coin
    return result


def test_greedy(input_sum):
    """Greedy alg test function"""
    find_coins_greedy(input_sum)

def test_dynamic(input_sum):
    """Dynamic alg test function"""
    find_coins_greedy(input_sum)

def run_test(func_part_name, input_sum, times=100):
    """Run test function"""
    print(f"Testing algoritm {alg_names[func_part_name]}" +\
          f" for input sum {input_sum} ......")
    print("" * 100)
    elapsed_time = timeit(
        f"test_{func_part_name}(input_sum)",
        setup=f"from __main__ import test_{func_part_name}",
        number=times, globals=globals()
    )
    return f"Result for algoritm {alg_names[func_part_name]}" +\
           f" elapsed time:{elapsed_time}"

alg_names = {
    "greedy" : "Жадібний алгортим",
    "dynamic" : "Динамічне програмування",
}

for func_short_name in alg_names:
    for input_sum in [113, 2757, 93232, 96273232]:
        print(run_test(func_short_name, input_sum, 100))
        print("=" * 100)

for input_sum in [113, 2757, 93232, 96273232]:
    print("*" * 100)
    print(f"Result for {input_sum} by greedy", find_coins_greedy(input_sum))
    print(f"Result for {input_sum} by dynamic", find_min_coins(input_sum))
