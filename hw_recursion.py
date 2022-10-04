import unittest
from unittest.case import skip

"""
 * Школьный кафетерий предлагает 2 вида сэндвичей, круглые и квадратные, помеченных как 0 и 1 соответсвенно.
 * Все ученики стоят в очереди. Каждый ученик желает либо квадратный либо круглый сэндвич.
 * <p>
 * Число сэндвичей в кафетерии равно числу учеников. Сэндвичи сложены стопкой (стек). На каждом шагу:
 * <p>
 * - Если ученик в начале очереди предпочитает сэндвич сверху стека -- он берет его и покидает очередь.
 * - Иначе, ученик не берет сэндвич и идет в конец очереди
 * <p>
 * Это продолжается пока никто из очереди учеников не хочет брать верхний сэндвич и потому не могут добраться к остальным и не могут покинуть очередь.
 * <p>
 * Даны 2 массива -- учеников и сэндвичей (students, sandwiches), где sandwiches[i] - вид ith сэндвича в стеке.
 * (i = 0 это вершина стека) и students[j] - предпочтение jth ученика в изначальной очереди
 * (j = 0 это начало (front) очереди).
 * Посчитайте количество учеников которые не смогу поесть.
 * <p>
 * Пример:
 * Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
 * Output: 0
 * Пояснение:
 * - Первый ученик оставляет верхний сэндвич и уходит в конец очереди, теперь students = [1,0,0,1].
 * - Первый ученик оставляет верхний сэндвич и уходит в конец очереди, теперь students = [0,0,1,1].
 * - Первый ученик берет верхний сэндвич и уходит из очереди, теперь students = [0,1,1] и sandwiches = [1,0,1].
 * - Первый ученик берет верхний сэндвич и уходит из очереди, теперь
 * - Первый ученик оставляет верхний сэндвич и уходит в конец очереди, теперь students = [1,1,0].
 * - Первый ученик берет верхний сэндвич и уходит из очереди, теперь students = [1,0] и sandwiches = [0,1].
 * - Первый ученик оставляет верхний сэндвич и уходит в конец очереди, теперь students = [0,1].
 * - Первый ученик берет верхний сэндвич и уходит из очереди, теперь students = [1] и sandwiches = [1].
 * - Первый ученик берет верхний сэндвич и уходит из очереди, теперь students = [] и sandwiches = [].
 * Все ученики взяли еду, 0 остались голодными
"""


def solve(students, sandwiches,  attempts=0):

    if not students:
        return attempts

    if attempts == len(students):
        return len(students)

    if students[0]==sandwiches[0]:
        students.pop(0)
        sandwiches.pop(0)
        attempts=0
    else:
        stud = students[0]
        students.pop(0)
        students.append(stud)
        attempts=attempts+1

    return solve(students, sandwiches,  attempts)


# @skip  # remove this to run tests
class T01(unittest.TestCase):
    testCases = [
        {"input": [[1, 1, 0, 0], [0, 1, 0, 1]], "expected": 0},
        {"input": [[1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]], "expected": 3},
        {"input": [[1, 1, 1, 0, 0], [1, 1, 1, 1, 1]], "expected": 2},
        {"input": [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]], "expected": 0},
        {"input": [[1, 1, 1, 1, 1], [0, 0, 0, 0, 0]], "expected": 5},
        {"input": [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1]], "expected": 5},
        {"input": [[1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]], "expected": 3}
    ]

    def test(self):
        print("Executing: 01 Hungry students")

        for i, test in enumerate(self.testCases):
            with self.subTest(f"Test index: {i}"):
                self.assertEqual(solve(
                    test["input"][0], test["input"][1]), test["expected"])





"""
 * Строка со скобками считается правильно если:
 * - Это пустая строка
 * - Она может быть записана как AB (А соединена с В), где А и В являются правильными
 * - Она может быть записана как (А), где А является правильной
 * <p>
 * Дана строка S. За одну операцию вы можете вставить скобку на любую позицию в строке.
 * Например, если s = "()))", вы можете вставить открывающую скобку и получить "(()))", или закрывающуюся и получить "())))".
 * <p>
 * Посчитайте минимальное количество операций нужных что бы сделать строку S правильной
 * <p>
 * Пример:
 * Input: s = "())"
 * Output: 1
"""


def solve(s):

    mass=[]
    counter=0
    return calculation(s, counter, mass)

def calculation(s, counter=0, mass=[]):

    if len(s)==0:
        if len(mass)>0:
            counter=counter+len(mass)
            return counter
        else:
            return counter

    if s[0]=='(':
        mass.append(')')
        s=s[1:]
    elif s[0]==')':
        if mass:
            if s[0]==mass[0]:
                mass.pop(0)
                s = s[1:]
            else:
                counter=counter+len(mass)
                mass=[]
                s = s[1:]
        else:
            counter=counter+1
            s = s[1:]

    return calculation(s, counter, mass)


# @skip  # remove this to run tests
class T02(unittest.TestCase):
    testCases = [
        {"input": ["())"], "expected": 1},
        {"input": ["((("], "expected": 3},
        {"input": ["(()"], "expected": 1},
        {"input": [")))((("], "expected": 6},
        {"input": ["()))(("], "expected": 4},
        {"input": ["()"], "expected": 0}
    ]

    def test(self):
        print("Executing: 02 Minimum change to make parentheses valid")

        for i, test in enumerate(self.testCases):
            with self.subTest(f"Test index: {i}"):
                self.assertEqual(solve(
                    test["input"][0]), test["expected"])



"""
 * Дана закодированная строка, верните раскодированную строку.
 * <p>
 * Правильно кодировки следующее: k[encoded_str], где encoded_str внутри квадратных скобок повторяется ровно k раз.
 * k гарантированно положительное число.
 * <p>
 * Вы можете быть уверены что входная строка всегда валидная; там нету лишних пробелов, квадратные скобки правильно стоят, итд
 * <p>
 * Более того, вы можете быть уверены что оригинальная строка не содержит чисел и числа используются только для повторений (k).
 * Например, не может быть входной строки как "3a" или "2[4]"
 * <p>
 * Пример:
 * Input: s = "3[a]2[bc]"
 * Output: "aaabcbc"
"""

def solve(s):
    result = ''
    count = 0
    stack = []
    return calc(s, result, count, stack)

def calc(s, result='', count=0, stack = []):

    if len(s) == 0:
        return result

    if s[0] == '[':
        stack.append(result)
        stack.append(count)
        result, count = '', 0
        s = s[1:]

    elif s[0] == ']':
        num = stack.pop()
        val = stack.pop()
        result = val + num * result
        s = s[1:]

    elif s[0].isdigit():
        count = count+ int(s[0])
        s = s[1:]

    else:
        result = result + s[0]
        s = s[1:]

    return calc(s, result, count, stack)



# @skip  # remove this to run tests
class T03(unittest.TestCase):
    testCases = [
            { "input": ["3[a]2[bc]"], "expected": "aaabcbc" },
            { "input": ["3[a2[c]]"], "expected": "accaccacc" },
            { "input": ["2[abc]3[cd]ef"], "expected": "abcabccdcdcdef" },
            { "input": ["ro2[bot]dr4[e]ams"], "expected": "robotbotdreeeeams" },
            { "input": ["qwe2[asd3[w2[e]]]"], "expected": "qweasdweeweeweeasdweeweewee" }
        ]

    def test(self):
        print("Executing: 03 Decode string")

        for i, test in enumerate(self.testCases):
            with self.subTest(f"Test index: {i}"):
                self.assertEqual(solve(
                    test["input"][0]), test["expected"])
