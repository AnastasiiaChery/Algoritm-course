import unittest
from unittest.case import skip

# """
# * Вам дан массив целых чисел nums, найдите подмассив (содержащий как минимум 1 число) который имеет наибольшую сумму и верните сумму.
# * <p>
# * Подмассив - это непрерывная часть массива.
# * Например, для массива [1,2,3,4], массив [2,3] является подмассивом, но [2,4] не является, так как это не непрерывная часть массива.
# * <p>
# * Пример
# * Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# * Output: 6
# * Пояснение: [4,-1,2,1] имеет наибольшую сумму = 6.
# * <p>
# * Ограничения:
# * 1 <= nums.length <= 10^5
# * -10^4 <= nums[i] <= 10^4
# """
#
#
# def solve(nums):
#     curr_sum = 0
#     max_sum = 0
#     for i in nums:
#         if i < 0:
#             if (curr_sum + i) > 0:
#                 curr_sum += i
#             else:
#                 curr_sum = 0
#         else:
#             curr_sum += i
#         if curr_sum > max_sum:
#             max_sum = curr_sum
#     if max_sum:
#         return max_sum
#     else:
#         return max(nums)
#
#
# @skip  # remove this to run tests
# class T01(unittest.TestCase):
#     testCases = [
#         {
#             "input": [[-2, 1, -3, 4, -1, 2, 1, -5, 4]],
#             "expected": 6
#         },
#         {
#             "input": [[1]],
#             "expected": 1
#         },
#         {
#             "input": [[5, 4, -1, 7, 8]],
#             "expected": 23
#         },
#         {
#             "input": [[8, 2, 3]],
#             "expected": 13
#         },
#         {
#             "input": [[8, -2]],
#             "expected": 8
#         },
#         {
#             "input": [[-8, -2]],
#             "expected": -2
#         },
#     ]
#
#     def test(self):
#         print("Executing: 01 Maximum Subarray")
#
#         for i, test in enumerate(self.testCases):
#             with self.subTest(f"Test index: {i}"):
#                 input = test["input"]
#                 self.assertEqual(
#                     solve(input[0]),
#                     test["expected"]
#                 )
#
# """
# * Вам дана матрица (сетка) MxN, заполненная неотрицательными целыми числами.
# * Найдите путь с верхней левой (left top) клетки в правую нижнюю (bottom right) с наименьшей суммой чисел по пути.
# * При условии что можно двигаться ТОЛЬКО вниз либо вправо на любом шаге.
# * <p>
# * Пример:
# * Input: grid = [
# * [1,3,1],
# * [1,5,1],
# * [4,2,1]
# * ]
# * Output: 7
# * Пояснение: путь 1 → 3 → 1 → 1 → 1 имеет наименьшую сумму.
# * <p>
# * Ограничения:
# * m == grid.length
# * n == grid[i].length
# * 1 <= m, n <= 200
# * 0 <= grid[i][j] <= 100
# """
#
#
# def solve(grid):
#
#     if type(grid[0]) != int:
#         m = len(grid)
#         n = len(grid[0])
#
#         for i in range(1, m):
#             grid[i][0] += grid[i - 1][0]
#         for j in range(1, n):
#             grid[0][j] += grid[0][j - 1]
#
#         for i in range(1, m):
#             for j in range(1, n):
#                 left = grid[i][j - 1]
#                 top = grid[i - 1][j]
#                 min_v = min(left, top)
#                 grid[i][j] += min_v
#
#         return grid[m - 1][n - 1]
#     else:
#         return grid[0]
#
#
# # @skip  # remove this to run tests
# class T02(unittest.TestCase):
#     testCases = [
#         {"input": [[[1, 3, 1], [1, 5, 1], [4, 2, 1]]], "expected": 7},
#         {"input": [[[1, 2, 3], [4, 5, 6]]], "expected": 12},
#         {"input": [[1]], "expected": 1},
#         {"input": [[[1, 1], [3, 1]]], "expected": 3},
#         {"input": [[[1, 1, 3], [4, 1, 1]]], "expected": 4},
#         {"input": [[[1, 2, 3], [1, 1, 8], [4, 1, 1], [4, 8, 1]]], "expected": 6},
#         {"input": [[[1, 2, 3, 2, 1]]], "expected": 9},
#     ]
#
#     def test(self):
#         print("Executing: 02 Minimum Path Sum")
#
#         for i, test in enumerate(self.testCases):
#             with self.subTest(f"Test index: {i}"):
#                 input = test["input"]
#                 self.assertEqual(
#                     solve(input[0]),
#                     test["expected"]
#                 )
#

#
# """
# * Вам даны 2 строки: text1 и text2. Верните длинну их наибольшой общей подпоследовательности. Если таковой нету -- верните 0.
# * <p>
# * Подпоследовательность строки это строка получена из оригинальной строки с некоторыми удаленными символами (может быть 0)
# * БЕЗ изменения относительного порядка оставшихся символов.
# * * например, 'ace' это подстрока 'abcde'
# * <p>
# * Общая последовательность двух строк это последовательность, которая есть в обеих строках.
# * <p>
# * Пример:
# * Input: text1 = "abcde", text2 = "ace"
# * Output: 3
# * Пояснение: самая длинная подпоследовательность -- "ace", длинною в 3 символа.
# * <p>
# * Ограничения:
# * 1 <= text1.length, text2.length <= 1000
# * text1 и text2 состоят только из букв английского алфавита в нижнем регистре [a-z]
# * <p>
# * Подсказка: постарайтесь решить эту задачу самостоятельно, но если никак не получается
# * -- поищите LCS (longest common subsequence) и разберитесь как это работает.
# """
#
#
# def solve(text1, text2):
#
#     height = len(text1)+1
#     width = len(text2)+1
#
#     dp = [[0] * width for i in range(height)]
#
#     for i in range(1, height):
#         for j in range(1, width):
#             if text1[i - 1] == text2[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1] + 1
#
#             dp[i][j] = max(dp[i][j], dp[i- 1][j], dp[i][j - 1])
#
#     return dp[-1][-1]
#
# # @skip  # remove this to run tests
# class T03(unittest.TestCase):
#     testCases = [
#         {"input": ["abcde", "ace"],
#             "expected": 3},
#         {"input": ["abc", "abc"],
#             "expected": 3},
#         {"input": ["abc", "def"], "expected": 0},
#         {"input": ["qwerty", "qy"], "expected": 2},
#         {"input": ["qwerty", "qklhy"], "expected": 2},
#     ]
#
#     def test(self):
#         print("Executing: 03 Longest Common Subsequence")
#
#         for i, test in enumerate(self.testCases):
#             with self.subTest(f"Test index: {i}"):
#                 input = test["input"]
#                 self.assertEqual(
#                     solve(input[0], input[1]),
#                     test["expected"]
#                 )


# """
# * Вы профессиональный грабитель, который планирует ограбления домов по одной прямой улице.
# * В каждом доме есть определенное количество денег, которые вы знаете и можете унести, единственное ограничение которое мешает вам ограбить все дома
# * это система безопасности домов. Вы можете отключить систему безопасности дома, но тогда у вас не получится отключить систему безопасности домов которые примыкают к этому дому.
# * То есть, если вы пробрались в дом i, это значит что у вас не получится пробраться в дома i-1 и i+1 (если они есть).
# * <p>
# * Вам дан массив целых чисел nums, который отображает количество денег в каждом доме.
# * Найдите максимальное количество денег которые вы сможете унести, без срабатывания системы безопасности.
# * <p>
# * Пример:
# * Input: nums = [1,2,3,1]
# * Output: 4
# * Пояснение: грабите дом №1 (money = 1) и потом дом №3 (money = 3). Всего вы уносите 4 единицы денег.
# * <p>
# * Ограничения:
# * 1 <= nums.length <= 100
# * 0 <= nums[i] <= 400
# """
#

def solve(nums):

    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    return dp[-1]


# @skip  # remove this to run tests
class T04(unittest.TestCase):
    testCases = [
        {"input": [[1, 2, 3, 1]], "expected": 4},
        {"input": [[1, 2, 3, 5]], "expected": 7},
        {"input": [[2, 7, 9, 3, 1]], "expected": 12},
        {"input": [[2, 7, 9, 3, 15, 10, 10, 10, 12]], "expected": 48},
    ]

    def test(self):
        print("Executing: 04 House Robber")

        for i, test in enumerate(self.testCases):
            with self.subTest(f"Test index: {i}"):
                input = test["input"]
                self.assertEqual(
                    solve(input[0]),
                    test["expected"]
                )
