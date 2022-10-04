import math
import unittest
from unittest.case import skip

"""
 * Дан массив целых чисел arr отсортированных по возрастанию.
 * Массив размера N, для каждого элемента 1 <= arr[i] <= N
 * <p>
 * Один элемент убрали из массива -- найдите отсутствующий элемент.
 * <p>
 * Пример:
 * input: arr = [1, 2, 3, 5, 6, 7]
 * output: 4
"""

def solve(arr):
    start= 1
    last = len(arr)
    mediana = math.trunc(last / 2)
    return binsearch(arr, start, last, mediana)


def binsearch(arr, first, last, mediana):

    if len(arr) == 1:
        if first==1 and arr[0]!=1:
            return 1
        return first + 1

    if arr[mediana] != mediana + first:
        arr = arr[0:mediana]

    else:
        arr = arr[mediana: last]
        first=first+mediana

    last = len(arr)
    mediana = math.trunc(last / 2)
    return binsearch(arr, first, last, mediana)


# @skip  # remove this to run tests
class T01(unittest.TestCase):
    testCases = [
            { "input": [[1, 2, 3, 5, 6, 7]], "expected": 4 },
            { "input": [[2, 3, 4, 5]], "expected": 1 },
            { "input": [[1, 2, 3, 4, 5, 6]], "expected": 7 },
            { "input": [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14]], "expected": 13 },
            { "input": [[1, 3, 4, 5, 6, 7]], "expected": 2 },
            { "input": [[1]], "expected": 2 },
            { "input": [[2]], "expected": 1 }
        ]

    def test(self):
        print("Executing: 01 Find the Missing Number in a sorted array")

        for i, test in enumerate(self.testCases):
            with self.subTest(f"Test index: {i}"):
                self.assertEqual(solve(
                    test["input"][0]), test["expected"])




"""
 * Экстра задача.
 * Дан односвязный список, для простоты будем работать только с целыми числами.
 * Нужно определить, есть ли цикл в данном списке.
 * Циклом мы называем множество элементов которые формируют кольцо.
 * Например:
 * 1 -> 2 -> 3 -> 4 -> 5
 * .....|--------------|
 * <p>
 * Где элемент (5) ссылается снова на элемент (2)
 * <p>
 * На вход дается объект Node (val, next).
 * Функция должна вернуть TRUE если цикл присутствует, либо FALSE если его нету.
 * Дополнительное условие: можно ли решить задачу без дополнительной памяти, т.е. О(1) ?
"""
# node = {val, next}
def solve(node):
    slow, fast = node, node
    try:
        while fast is not None and node['next'] is not None:

            fast = fast['next']['next']
            slow = slow['next']

            if fast == slow:
                return True  # found the cycle
        return False
    except:
        return False



# @skip  # remove this to run tests
class T02(unittest.TestCase):
    def makeNode(self, val, prev=None):
        node = {val: val, next: None}
        if (prev):
            prev["next"] = node
        return node

    def test(self):
        print("Executing: 02 Does linked list have a loop")

        n1 = self.makeNode(1)
        n2 = self.makeNode(2, n1)
        n3 = self.makeNode(3, n2)
        n4 = self.makeNode(4, n3)
        n5 = self.makeNode(5, n4)
        # n1 -> n2 -> n3 -> n4 -> n5

        n5["next"] = n2
        self.assertEqual(solve(n1), True)

        n5["next"] = None
        self.assertEqual(solve(n1), False)

        n5["next"] = n1
        self.assertEqual(solve(n1), True)

        n5["next"] = n4
        self.assertEqual(solve(n1), True)

        a1 = self.makeNode(10)
        self.assertEqual(solve(a1), False)

        a1["next"] = a1
        self.assertEqual(solve(a1), True)
