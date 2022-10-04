import unittest
from unittest.case import skip


"""
Дан массив чисел nums. 
Running sum для элемента i задан как сумма элементов [0..i], то есть runningSum[i] = sum(nums[0]..nums[i]).
Вычислите и верните массив running sum.

Пример:
Input: nums = [1, 2, 3]
Output: [1, 3, 6]

Сложность - O(n)
"""

def solve(nums):
    # Write your solution here
  for i in range(len(nums)):
    if i>0:
      nums[i] = nums[i] + nums[i-1]
  return nums

# @skip #remove this to run tests
class T01(unittest.TestCase):
    testCases = [
            {"input": [[1, 2, 3, 4, 5]], "expected": [1, 3, 6, 10, 15]},
            {"input": [[1, 2, 3, 4, 6]], "expected": [1, 3, 6, 10, 16]},
            {"input": [[1, 1, 1, 1]], "expected": [1, 2, 3, 4]},
            {"input": [[1, 2, -3, 4, 6]], "expected": [1, 3, 0, 4, 10]},
            {"input": [[-1, -1, -2, 4, 0]], "expected": [-1, -2, -4, 0, 0]}
        ]
    def test(self):
        print("Executing: 01 Running sum")

        for i, test in enumerate(self.testCases):
            with self.subTest(f"Test index: {i}"):
                self.assertEqual(solve(
                    test["input"][0]), test["expected"])


"""
Вам дана матрица MxN целых чисел - accounts. Где accounts[i][j] хранит количество денег
ith клиент имеет на jth счету. Верните состояние самого богатого клиента.

Состояние клиента это сумма всех его средств на всех счетах.

Пример:
Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10

Сложность - O(n^2)
"""


def solve(accounts):
    # Write your solution here
    max = 0
    for i in range(len(accounts)):
        sum = 0
        for j in accounts[i]:
            sum = sum + j
        accounts[i] = sum
        if sum > max:
            max = sum

    return max


# @skip #remove this to run tests
class T02(unittest.TestCase):
    testCases = [
        {"input": [[[1, 2, 3], [3, 2, 1]]], "expected": 6},
        {"input": [[[1, 5], [7, 3], [3, 5]]], "expected": 10},
        {"input": [[[2, 8, 7], [7, 1, 3], [1, 9, 5]]], "expected": 17},
        {"input": [[[2, 6, 7], [7, 1, 3], [1, 9, 5]]], "expected": 15},
        {"input": [[[8], [1, 2, 3], [10, -1]]], "expected": 9}
    ]

    def test(self):
        print("Executing: 02 Richest customer")

        for i, test in enumerate(self.testCases):
            with self.subTest(f"Test index: {i}"):
                self.assertEqual(solve(
                    test["input"][0]), test["expected"])




"""
Вам дан массив целых чисел nums.
Верните минимальное число операций требуемых для того, что бы сделать nums строго возрастающим.

Одна операция - это увеличение любого элемента в массиве на 1.

Массив nums будет строго возрастающим если nums[i] < nums[i+1] для всех 0 <= i < nums.length - 1
Массив с одним элементом считается строго возрастающим.

Пример:
Input: nums = [1,1,1]
Output: 3

Пояснение: строго возрастающим будет массив [1,2,3], потому нужно увеличить nums[1] ровно 1 раз, а nums[2] 2 раза.

Сложность - O(n)
"""

def solve(nums):
  counter=0
  if len(nums) > 1:
    for i in range(1, len(nums)):
      if nums[i]<=nums[i-1]:
        add= nums[i-1]-nums[i]+1
        nums[i]= nums[i]+add
        counter = counter+add

  return counter

# @skip #remove this to run tests
class T03(unittest.TestCase):
    testCases = [
            { "input": [[1, 1, 1]], "expected": 3 },
            { "input": [[1, 2, 1]], "expected": 2 },
            { "input": [[-3]], "expected": 0 },
            { "input": [[-3, -2, 10]], "expected": 0 },
            { "input": [[-3, -2, -5]], "expected": 4 },
            { "input": [[1, 5, 90, 0]], "expected": 91 },
            { "input": [[1, 0, 5, 4, 90, 0]], "expected": 95 }
        ]
    def test(self):
        print("Executing: 03 Min number of changes to make array increasing")

        for i, test in enumerate(self.testCases):
            with self.subTest(f"Test index: {i}"):
                self.assertEqual(solve(
                    test["input"][0]), test["expected"])


"""
Вам дана матрица MxN. Верните true если это Toeplitz матрица. Иначе, верните false.

Toeplitz матрица это матрица в котороый каждая диагональ 
(с верхнего левого элемента по нижний правый элемент) имеет одинаковые значения.

Пример Toeplitz матрицы:
1,2,3,4
5,1,2,3
9,5,1,2
Диагоналями являются: "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
Сложность - O(n^2)
"""


def solve(matrix):
    len_i = len(matrix)
    len_j = len(matrix[0])

    for i in range(len_i - 1):
        for j in range(len_j - 1):
            if (matrix[i][j] != matrix[i + 1][j + 1]):
                return False
    return True


# @skip #remove this to run tests
class T04(unittest.TestCase):
    testCases = [
        {"input": [[[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]], "expected": True},
        {"input": [[[1, 2, 3, 4], [5, 1, 3, 3], [9, 5, 1, 2]]], "expected": False},
        {"input": [[[1, 2], [1, 2]]], "expected": False},
        {"input": [[[1]]], "expected": True},
        {"input": [[[1, 1, 1, 11], [1, 1, 1, 1], [10, 1, 1, 1]]], "expected": True}
    ]

    def test(self):
        print("Executing: 04 Is Toeplitz matrix")

        for i, test in enumerate(self.testCases):
            with self.subTest(f"Test index: {i}"):
                self.assertEqual(solve(
                    test["input"][0]), test["expected"])


"""
Вам дан список (массив) слов words, и два слова word1, word2.
Посчитайте кратчайшую дистанцию между этими двумя словами в массиве.

word1 и word2 не совпадают и оба присутсвуют в массиве.

Пример:
Input: words = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3

Сложность - O(n)
"""


def solve(words, word1, word2):
    # Write your solution here
    first_word_index = None
    second_word_index = None
    distance = None
    for i in range(len(words)):
        if words[i] == word1:
            first_word_index = i
        elif words[i] == word2:
            second_word_index = i

        if first_word_index is not None and second_word_index is not None:
            new_distance = math.fabs(first_word_index - second_word_index)

            if distance is None:
                distance = new_distance
            else:
                if new_distance < distance:
                    distance = new_distance

    return distance


# @skip  # remove this to run tests
class T05(unittest.TestCase):
    testCases = [
        {"input": [["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"],
         "expected": 3},
        {"input": [["practice", "makes", "perfect", "coding", "makes"], "makes", "coding"],
         "expected": 1},
        {"input": [["coding", "practice", "makes", "perfect", "coding", "makes"], "makes", "coding"],
         "expected": 1},
        {"input": [["a", "b", "c", "d", "b", "q"], "a", "q"],
         "expected": 5},
        {"input": [["a", "q", "c", "d", "b", "q"], "a", "q"],
         "expected": 1},
    ]

    def test(self):
        print("Executing: 05 Shortest word distance")

        for i, test in enumerate(self.testCases):
            with self.subTest(f"Test index: {i}"):
                self.assertEqual(solve(
                    test["input"][0], test["input"][1], test["input"][2]), test["expected"])
