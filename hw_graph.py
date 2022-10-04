import unittest
from collections import deque, defaultdict
from unittest.case import skip


"""
* Дано бинарное дерево поиска с целочисленными значениями и два числа - from & to.
* Нужно вернуть сумму всех элементов которые есть в дерево и попадают в диапазон [from; to] (включительно).
* <p>
* Note: в тестах дерево задано через массив, но на вход дается УЗЕЛ, а именно - корень дерева.
* Структура узла следующая:
* Node {
*     int data;
*     Node left;
*     Node right
* }
*
"""

#
# def solve(root, fromVal, toVal):
#     list_val = []
#
#     def check(root, list_val):
#         if not root:
#             return
#         check(root['left'], list_val)
#         if fromVal <= root['data'] <= toVal:
#             list_val.append(root['data'])
#         check(root['right'], list_val)
#
#     check(root, list_val)
#
#     return sum(list_val)
#
#
#
# # @skip  # remove this to run tests
# class T01(unittest.TestCase):
#     testCases = [
#         {"input": [[15, 10, 17, 4, 13, 16, 20, None, 6, None,
#                     None, None, None, 19, 22], 16, 20], "expected": 72},
        # {"input": [[15, 10, 17, 4, 13, 16, 20, None, 6, None,
        #             None, None, None, 19, 22], 16, 21], "expected": 72},
        # {"input": [[15, 10, 17, 4, 13, 16, 20, None, 6, None,
        #             None, None, None, 19, 22], 17, 21], "expected": 56},
        # {"input": [[15, 10, 17, 4, 13, 16, 20, None, 6, None,
        #             None, None, None, 19, 22], 0, 12], "expected": 20},
    # ]
    #
    # def test(self):
    #     print("Executing: 01 Range sum in BST")
    #
    #     for i, test in enumerate(self.testCases):
    #         with self.subTest(f"Test index: {i}"):
    #             input = test["input"]
    #             self.assertEqual(
    #                 solve(self.arrayToTree(input[0]), input[1], input[2]),
    #                 test["expected"]
    #             )
    #
    # def arrayToTree(self, values, i = 0):
    #     if (i >= len(values) or values[i] is None):
    #         return None
    #
    #     return {"data": values[i], "left": self.arrayToTree(values, 2 * i + 1),
    #             "right": self.arrayToTree(values, 2 * i + 2)}


"""
* Дано бинарное дерево (НЕ ПОИСКА).
* "Хорошим" узлом считается такой узел, значение которого больше или равно всех значений узлов которые находятся по пути от корня к данному узлу.
* <p>
* Вернуть количество "хороших" узлов в нем.
* <p>
* Пример дерева
*                (3)
*          1              (4)
*     (3)              1       (5)
* Output: 4
* Узлы выделенные скобками в примере являются "хорошими" узлами.
* Например, для узла (5) справделиво условие, так как узлы по пути от корня к нему - [3, 4] имеют значения меньше.
*
* Note: в тестах дерево задано через массив, но на вход дается УЗЕЛ, а именно - корень дерева.
* Структура узла следующая:
* Node {
*     int data;
*     Node left;
*     Node right
* }
"""


# def solve(root):
#     list_val = []
#     base = root['data']
#     def check(root, list_val):
#         if not root:
#             return
#         check(root['left'], list_val)
#         if root['data'] >= base:
#             list_val.append(root['data'])
#         check(root['right'], list_val)
#
#     check(root, list_val)
#
#     return len(list_val)
#
#
# # @skip  # remove this to run tests
# class T02(unittest.TestCase):
#
#     testCases = [
#         {"input": [[3, 1, 4, 3, None, 1, 5]], "expected": 4},
#         {"input": [[1, 2, 3, 4, 5, 6, 7]], "expected": 7},
#         {"input": [[7, 6, 5, 4, 3, 2, 1]], "expected": 1},
#         {"input": [[3, 3, None, 4, 2]], "expected": 3},
#     ]
#
#     def test(self):
#         print("Executing: 02 Good nodes count")
#
#         for i, test in enumerate(self.testCases):
#             with self.subTest(f"Test index: {i}"):
#                 input = test["input"]
#                 self.assertEqual(
#                     solve(self.arrayToTree(input[0])),
#                     test["expected"]
#                 )
#
#     def arrayToTree(self, values, i=0):
#         if (i >= len(values) or values[i] is None):
#             return None
#
#         return {"data": values[i], "left": self.arrayToTree(values, 2 * i + 1),
#                 "right": self.arrayToTree(values, 2 * i + 2)}
#


# """
# * Дано бинарное дерево, проверить является ли оно бинарным деревом поиска.
# * <p>
# * Note: в тестах дерево задано через массив, но на вход дается УЗЕЛ, а именно - корень дерева.
# * Структура узла следующая:
# * Node {
# *     int data
# *     Node left;
# *     Node right
# * }
# """
#
#
def solve(root):
    def check(root, min=float('-inf'), max=float('inf')):

        if root:
            if root['data'] > min and root['data'] < max:
                return (check(root['left'],  min, root['data']) and check(root['right'], root['data'], max))
            else:
                return False
        return True

    return check(root)


# @skip  # remove this to run tests
class T03(unittest.TestCase):

    testCases = [
        {"input": [[3, 1, 4, 3, None, 1, 5]], "expected": False},
        {"input": [[1, None, 3, None, None, 2, 7]], "expected": True},
        {"input": [[1]], "expected": True},
        {"input": [[1, 2, 3]], "expected": False},
        {"input": [[2, 1, 3]], "expected": True},
        {"input": [[5, 1, 4, None, None, 3, 6]], "expected": False},
    ]

    def test(self):
        print("Executing: 03 Check if binary tree is BST")

        for i, test in enumerate(self.testCases):
            with self.subTest(f"Test index: {i}"):
                input = test["input"]
                self.assertEqual(
                    solve(self.arrayToTree(input[0])),
                    test["expected"]
                )

    def arrayToTree(self, values, i=0):
        if (i >= len(values) or values[i] is None):
            return None

        return {"data": values[i], "left": self.arrayToTree(values, 2 * i + 1),
                "right": self.arrayToTree(values, 2 * i + 2)}



# """
# * Есть система для поездок такси. Эта система умеет присылать нам события, когда поездка завершена. Вместе с событием мы получаем длинну поездки (в километрах, всегда округлена к целому числу). От нашей системы требуется отдавать K самых коротких поездок в любой момент времени.
# * <p>
# * Система должна уметь обрабатывать разные запросы, среди которых
# * Запрос #1: поездка произошла
# * Запрос #2: вернуть K самых коротких поездок на текущий момент (эти поездки больше не будут участвовать в следующих запросах)
# * <p>
# * Запросы задаются как массив, где первым значением будет ключ запроса: 1 - поездка произошла, 2 - вернуть K самых коротких поездок.
# * Значение K задается только в начале.
# * Значения запросов во входных данных всегда валидно.
# * <p>
# * Пример запросов:
# * [1, 54] - означает что произошла поездка и ее дистанция равняется 54 километрам
# * [2] - означает что нужно вернуть K самых коротких поездок на этот момент, в неубывающем порядке (если всего поездок меньше, вернуть те что есть)
# * <p>
# * Порядок запросов может быть разный.
# * Так как все команды передаются сразу в виде списке, вернуть нужно лишь результат всех операций в правильном порядке.
# * Пример input:
# * K = 3, requests = [[1, 54], [1, 32], [2], [1, 85], [1, 4], [1, 5], [1, 22], [1, 2], [2]]
# * Пример output:
# * [[32, 54], [2, 4, 5]
# """
#
#
# def solve(k, requests):
#     count = k
#     ansver_list = []
#     result_list=[]
#     for i in range(len(requests)):
#         if requests[i] == [2]:
#             ansver_list.append(sorted(result_list))
#             result_list = []
#         else:
#             if len(result_list)<count:
#                 result_list.append(requests[i][1])
#             else:
#                 max_result = max(result_list)
#                 if max_result >= requests[i][1]:
#                     change_index = result_list.index(max_result)
#                     result_list[change_index] = requests[i][1]
#
#     return ansver_list
#
#
# # @skip  # remove this to run tests
# class T04(unittest.TestCase):
#     testCases = [
#         {"input": [3, [[1, 54], [1, 32], [2], [1, 85], [1, 4], [1, 5], [1, 22], [1, 2], [2]]],
#          "expected": [[32, 54], [2, 4, 5]]},
#         {"input": [2, [[2], [1, 54], [1, 32], [1, 85], [1, 4], [2], [1, 5], [2]]], "expected": [[], [4, 32], [5]]},
#     ]
#
#     def test(self):
#         print("Executing: 04 Process trips")
#
#         for i, test in enumerate(self.testCases):
#             with self.subTest(f"Test index: {i}"):
#                 input = test["input"]
#                 self.assertEqual(
#                     solve(input[0], input[1]),
#                     test["expected"]
#                 )

#
# """
# * Дан неориентированный ациклический граф, состоящий из N вершин, пронумерованных от 1 до N.
# * Граф-звезда это такой граф, в котором есть ровно одна центральная вершина и ровно N-1 ребер соединяющие центр-вершину с другими.
# * Дан валидный граф-звезда. Нужно найти центр вершину.
# * Ребро может быть только между центральной вершиной и любой другой вершиной.
# * <p>
# * На вход подается список ребер (from -> to)
# * <p>
# * Input: [[1,2],[2,3],[4,2]]
# * Output: 2
# *
# * Экстра вопрос: существует ли О(1) решение? Да или нет -- напишите Ваше мнение ниже :)
# """
#
#
# def solve(edges):
#     a = edges[0][0]
#     b = edges[0][1]
#
#     if edges[1][0] == a or edges[1][1] == a:
#         return a
#     else:
#         return b
#
#
# @skip  # remove this to run tests
# class T05(unittest.TestCase):
#     testCases = [
#         {"input": [[1, 2], [2, 3], [4, 2]], "expected": 2},
#         {"input": [[1, 2], [5, 1], [1, 3], [1, 4]], "expected": 1},
#         {"input": [[6, 3], [2, 6], [1, 6], [6, 5], [4, 6]], "expected": 6},
#     ]
#
#     def test(self):
#         print("Executing: 05 Center of Star Graph")
#
#         for i, test in enumerate(self.testCases):
#             with self.subTest(f"Test index: {i}"):
#                 input = test["input"]
#                 self.assertEqual(solve(input), test["expected"])
#
#
# # """
# # * Дан неориентированный (бинаправленый) ациклический граф состоящий из N вершин.
# # * Каждая вершина пронумерована от 0 до N-1.
# # * Нужно определить, есть ли путь из вершины A в вершину B.
# # * На вход подается список ребер в виде [from, to] (что в неориентированной графе означает что существует и [to, from]).
# # * Если путь есть вернуть True, иначе -- False.
# # """
# #
# #
# def solve(n, edges, a, b):
#     # Write your solution here
#     pointlist = {}
#     for i in edges:
#         if i[0] in pointlist:
#             pointlist[i[0]].append(i[1])
#         else:
#             pointlist[i[0]] = [i[1]]
#
#         if i[1] in pointlist:
#             pointlist[i[1]].append(i[0])
#         else:
#             pointlist[i[1]] = [i[0]]
#
#     queue = [a]
#     visited = [a]
#
#     while queue:
#         val = queue.pop(0)
#         if val == b:
#             return True
#
#         if val in pointlist:
#             for j in pointlist[val]:
#
#                 if j not in visited:
#                     queue.append(j)
#                     visited.append(j)
#
#     return False
#
#
# @skip  # remove this to run tests
# class T06(unittest.TestCase):
#     testCases = [
#         {"input": [3, [[1, 2], [2, 3], [1, 3]], 1, 3], "expected": True},
#         {"input": [5, [[1, 2], [2, 3], [1, 3], [4, 5]], 1, 5],
#          "expected": False},
#         {"input": [5, [[1, 2], [2, 3], [3, 5], [4, 5]], 1, 4], "expected": True},
#         {"input": [6, [[1, 2], [2, 6], [1, 5], [
#             3, 5], [5, 4]], 3, 6], "expected": True},
#         {"input": [6, [[1, 2], [2, 6], [3, 4], [
#             3, 5], [5, 4]], 3, 6], "expected": False}
#     ]
#
#     def test(self):
#         print("Executing: 06 Is there a path in a graph")
#
#         for i, test in enumerate(self.testCases):
#             with self.subTest(f"Test index: {i}"):
#                 input = test["input"]
#                 self.assertEqual(
#                     solve(input[0], input[1], input[2], input[3]),
#                     test["expected"]
#                 )
