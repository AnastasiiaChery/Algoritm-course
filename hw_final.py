# import unittest
# from unittest.case import skip
#
# """
#  * Warmup task :)
#  * <p>
#  * Дана строка, представленная как массив символов. Сделайте реверс порядка слов.
#  * <p>
#  * Слово -- это последовательность символов без пробела. Слова отделены друг от друга всегда одним пробелом.
#  * <p>
#  * Верните строку, состоящую из слов в обратном порядке разделенных одиночными пробелами.
#  * Алгоритм должен работать за O(n) времени и не использовать встроенные функции как split(), join(), reverse(), StringBuffer, etc.
#  * <p>
#  * Доп условие: Так же, алгоритм должен работать in-place (после обработки верните тот же chars что бы соблюсти сигнатуру),
#  * то есть не расходовать дополнительную память совсем (новый массив для символов уже является доп памятью)
#  * <p>
#  * Возможные символы: [a-z], [A-Z] и пробелы.
#  * <p>
#  * Пример:
#  * Input: s = "last task in course"
#  * Output: "course in task last"
# """
#
#
# def solve(chars):
#     a = ""
#     b = ""
#     for i in range(len(chars)):
#         if chars[i] != " ":
#             a += chars[i]
#         else:
#             if b == "":
#                 b = a
#                 a = ""
#             elif a:
#                 b = a + " " + b
#                 a = ""
#             else:
#                 pass
#     return list(a + " " + b if b else a)
#
#
# # @skip  # remove this to run tests
# class T01(unittest.TestCase):
#     testCases = [
#         {
#             "input": [list("last task in course")],
#             "expected": list("course in task last")
#         },
#         {
#             "input": [list("I love algo")],
#             "expected": list("algo love I")
#         },
#         {
#             "input": [list("singlewordhere")],
#             "expected": list("singlewordhere")
#         },
#         {
#             "input": [list("a b c d e f g")],
#             "expected": list("g f e d c b a")
#         }
#     ]
#
#     def test(self):
#         print("Executing: Warmup task, reverse words")
#
#         for i, test in enumerate(self.testCases):
#             with self.subTest(f"Test index: {i}"):
#                 input = test["input"]
#                 self.assertEqual(
#                     solve(input[0]),
#                     test["expected"]
#                 )
import unittest

# class Cache:
#
#     def __init__(self, capacity):
#         self.capacity= capacity
#         self.values = []
#         self.cash = {}
#
#     def get(self, key):
#         # если у нас уже есть ключ, мы удаляем его из списка и вставляем в конец
#         if key in self.cash:
#             self.values.remove(key)
#             self.values.append(key)
#             return self.cash[key]
#         return -1
#
#     def put(self, key, value) -> None:
#
#         if key in self.cash:
#             # если такой ключ уже есть мы обновляем его
#             self.values.remove(key)
#             self.values.append(key)
#             self.cash[key] = value
#         elif len(self.values) == self.capacity:
#             # если места нет - = освобождаем
#             self.cash.pop(self.values[0])
#             self.values.remove(self.values[0])
#             self.values.append(key)
#             self.cash[key] = value
#         else:
#             # просто добавляем новый элемент
#             self.values.append(key)
#             self.cash[key] = value
#
# def test_2():
#
#     cache_ex = Cache(2)
#
#     # данных еще нет
#     assert cache_ex.get(1) == -1
#     assert cache_ex.get(2) == -1
#     assert cache_ex.get(3) == -1
#     assert cache_ex.get(4) == -1
#
#     # добавили данные
#     assert cache_ex.put(1, 1) == None
#     assert cache_ex.put(2, 2) == None
#     assert cache_ex.put(3, 3) == None
#     assert cache_ex.put(4, 4) == None
#
#
#     # кеш == 2, а значит первых двух значений не будет
#     assert cache_ex.get(1) == -1
#     assert cache_ex.get(2) == -1
#
#     # данные еть
#     assert cache_ex.get(3) == 3
#     assert cache_ex.get(4) == 4
#


"""
Разрабатывая систему для подсказок при вводе адреса, нам нужно реализовать базовый движок для поиска.

Мы определили два базовых варианта которые нам нужно обрабатывать при поиске:
* поиск по точному адресу: если у нас есть точно то что ввел пользователь, например "airport kbp"
* поиск по префику: если пользователь вводит адрес и ждет подсказку, например "airpo"

Для простоты реализации мы будем работать с адресами в виде обычной строки, никаких сложных объектов.

Так же, для простоты в контексте данной задачи требования к структуре будут упрощены, а именно:
* можно рассчитывать что вся структура поместится в память, и нам не нужно удалять из нее что-либо
* insert(str): добавляет строку в структуру
* search(str): возвращает TRUE если точно такая же строка есть в структуре, иначе FALSE
* startsWith(prefix): возвращает TRUE если есть адрес с таким префиксом, иначе FALSE
* количество поисков превышает количество вставок, но операции могут выполнятся в любом порядке
"""


class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word):
        trie = self.trie
        # разбиваем слова на буквы и вставляем их в виде связного списка.
        # что бы потом было легче реализовать поиск по префиксу
        for letter in word:
            if letter not in trie:
                trie[letter] = {}
            trie = trie[letter]
        trie["next_letter"] = True

    def search(self, word):
        trie = self.trie
        for letter in word:
            if letter in trie:
                trie = trie[letter]
            else:
                return False
        return "next_letter" in trie

    def startsWith(self, prefix):
        trie = self.trie
        for letter in prefix:
            if letter in trie:
                trie = trie[letter]
            else:
                return False
        return True


def test_3():

    trie = Trie()


    assert trie.insert('Городоцька') == None
    assert trie.search('Городоцька') == True
    assert trie.startsWith('Гор') ==  True
    assert trie.startsWith('Кар') == False
    assert trie.startsWith('Зари') == False
    assert trie.insert('Зарицьких') == None
    assert trie.startsWith('Зари') ==  True
    assert trie.search('Зарицьких') == True
