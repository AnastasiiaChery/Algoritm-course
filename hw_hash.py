import unittest
from unittest.case import skip

# """
# * Каждый имейл адрес состоит из имени почтового ящика и доменного имени,
# * которые разделены знаком '@'. Помимо символов нижнего регистра (a-z), имейл
# * может содержать так же знаки '.' или '+'
# * Например, в "alice@robotdreams.cc", часть "alice" это имя почтового ящика, а
# * "robotdreams.cc" это доменной имя.
# * <p>
# * Если добавить точки '.' между некоторыми символами в имени почтового ящика,
# * письмо отправленное туда будет перенаправленно на такой же адрес без точек в
# * имени ящика. Такое правило НЕ распространяется на доменное имя.
# * Например, "alice.k@robotdreams.cc" и "alicek@robotdreams.cc" направят на один
# * и тот же имейл адрес.
# * <p>
# * Если добавить плюс '+' в имя почтового ящика, все после первого плюса будет
# * проигнорировано. Это позволяет фильтровать определенные имейлы. Такое правило
# * НЕ распространяется на доменное имя.
# * Например, "alice.k+ads@robotdreams.cc" будет перенаправленно на
# * "alicek@robotdreams.cc"
# * <p>
# * Оба правила можно использовать одновременно.
# * <p>
# * Вам дан список (массив) имейлов (строки), куда мы хотим отправить письмо.
# * Но мы не хотим отправлять письмо на один и тот же финальный почтовый ящик.
# * Нужно посчитать финальное количество адресов которые действительно получат
# * письмо.
# * <p>
# * Пример
# * Input: ["alice.k@xyz.com", "bob.f@qwer.ty", "al.i.cek+rd@xyz.com",
# * "alicek@qwer.ty"]
# * Output: 3
# * Пояснение: всего останется 3 уникальных финальных адреса, а именно
# * ["alice.k@xyz.com", "bob.f@qwer.ty", "alicek@qwer.ty"]
# """
#
#
# def solve(emails):
#     if not emails:
#         return 0
#
#     seen = set()
#
#     for email in emails:
#         name, domain = email.split('@')
#         local = name.split('+')[0].replace('.', '')
#         seen.add(local + '@' + domain)
#     return len(seen)
#
# # @skip  # remove this to run tests
# class T01(unittest.TestCase):
#     testCases = [
#         {
#             "input": [["alice.k@xyz.com", "bob.f@qwer.ty", "al.i.cek+rd@xyz.com", "alicek@qwer.ty"]],
#             "expected": 3
#         },
#         {
#             "input": [["abc.xyz@q.w", "xyz.abc@q.w", "abc+xyz@q.w"]],
#             "expected": 3
#         },
#         {
#             "input": [["abc.xyz+rd@n.m", "a.bc.xy.z@n.m"]],
#             "expected": 1
#         },
#         {
#             "input": [["abc+qwe@n.m", "abc@m.n", "abc.qwe@n.m", "abc.qwe+rr.tt@n.m"]],
#             "expected": 3
#         },
#     ]
#
#     def test(self):
#         print("Executing: 01 Email unique list")
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
# * Даны две строки s и t.
# * Строка t сгенерирована случайной перестановкой букв в строке s, и потом одна дополнительная буква добавлена в случайную позицию.
# * <p>
# * Нужно найти и вернуть букву, которая была добавлена.
# * <p>
# * Пример
# * Input: s = "abcd", t = "acbed"
# * Output: "e"
# """
#
#
# def solve(s, t):
#     count_symb = {}
#
#     for i in t:
#         if i in count_symb:
#             count_symb[i] += 1
#         else:
#             count_symb[i] = 1
#
#     for i in s:
#         count_symb[i] -= 1
#
#     for i in count_symb:
#         if count_symb[i] == 1:
#             return i
#
#
# # # @skip  # remove this to run tests
# class T02(unittest.TestCase):
#
#     testCases = [
#         {"input": ["abde", "debca"], "expected": 'c'},
#         {"input": ["abde", "xdeba"], "expected": 'x'},
#         {"input": ["abde", "dabew"], "expected": 'w'},
#         {"input": ["aabbde", "adabelb"], "expected": 'l'},
#         {"input": ["aabbde", "adabedb"], "expected": 'd'},
#     ]
#
#     def test(self):
#         print("Executing: 02 Find extra character")
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
# * Дан список слов, нужно вернуть список слов которые могут быть набраны с помощью букв только на одном уровне "стандартной Американской клавиатуры".
# * Под уровнем имеется ввиду набор символов которые идут один за другим на одной горизонтали.
# * <p>
# * В "стандартной Американской клавиатуре":
# * <p>
# * первый уровень состоит из символов "qwertyuiop"
# * второй уровень состоит из символов "asdfghjkl"
# * третий уровень состоит из символов "zxcvbnm"
# * <p>
# * Вернуть слова нужно в том же порядке в котором они встречаются в исходном списке.
# * <p>
# * Пример:
# * Input: ["row", "trophy", "qaz", "hall"]
# * Output: ["row", "hall"]
# * Слово "trophy" содержит все буквы из одного уровня, кроме буквы 'h', которая располагается на втором уровне, в то время как остальные располагаются на первом.
# * Словл "qaz" имеет в себе буквы со всех 3х уровней, потому тоже не подходит.
# """
#
#
# def solve(words):
#     first = set("q w e r t y u i o p Q W E R T Y U I O P".split())
#     second = set("a s d f g h j k l A S D F G H J K L".split())
#     third = set("z x c v b n m Z X C V B N M".split())
#
#     results = []
#
#     for word in words:
#         letters = set(word)
#
#         if not len(letters - first):
#             results.append(word)
#             continue
#         if not len(letters - second):
#             results.append(word)
#             continue
#         if not len(letters - third):
#             results.append(word)
#             continue
#
#     return results
#
#
# # @skip  # remove this to run tests
# class T03(unittest.TestCase):
#
#     testCases = [
#         {"input": [["row", "trophy", "qaz", "hall"]],
#             "expected": ["row", "hall"]},
#         {"input": [["Hello", "Alaska", "Dad", "Peace"]],
#             "expected": ["Alaska", "Dad"]},
#         {"input": [["gjaskfie", "sadjgV", "vncmxkjqQ"]], "expected": []},
#     ]
#
#     def test(self):
#         print("Executing: 03 Keyboard row")
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
# * Даны две строки ransomNote и magazine, верните True если ransomNote может быть составлена из строки magazine и False в обратном случае.
# * <p>
# * Каждый символ в строке magazine может быть использован ровно один раз в ransomNote.
# * <p>
# * Пример:
# * Input: "ransom", "man or sort"
# * Output: True
# * Все буквы из "ransom" в точности присутствуют в строке "man or sort" и могут быть использованы
# """
#
#
# def solve(ransomNote, magazine):
#     dict_val = {}
#     for i in magazine:
#         if i not in dict_val:
#             dict_val[i] = 1
#         else:
#             dict_val[i] += 1
#
#     for i in ransomNote:
#         if i not in dict_val:
#             return False
#         elif dict_val[i] == 0:
#             return False
#         else:
#             dict_val[i] -= 1
#     return True
#

#
# # @skip  # remove this to run tests
# class T04(unittest.TestCase):
#
#     testCases = [
#         {"input": ["aa", "aab"], "expected": True},
#         {"input": ["aa", "ab"], "expected": False},
#         {"input": ["ransom", "man or sort"], "expected": True},
#         {"input": ["ransom", "man and sot"], "expected": False},
#         {"input": ["RanSom", "man or soRt"], "expected": False},
#         {"input": ["RanSom", "man or SoRt"], "expected": True},
#         {"input": ["Ran  Som", "man or SoRt"], "expected": True},
#         {"input": ["Ran  So m", "man or SoRt"], "expected": False},
#         {"input": ["Poke", "OK that is Poke"], "expected": True},
#         {"input": ["a", "b"], "expected": False},
#         {"input": ["qwertyuiop", "poiqwerytuueq"], "expected": True},
#         {"input": ["poiqwerytuueq", "qwertyuiop"], "expected": False},
#     ]
#
#     def test(self):
#         print("Executing: 04 Is ransom note possible")
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
# * Дан массив nums целых чисел длинною в N где все числа в nums лежат в диапазоне [1, N]
# * и каждое число встречается один либо два раза. Нужно найти и вернуть список чисел которые встречаются дважды.
# * <p>
# * Числа можно вернуть в любом порядке.
# * <p>
# * Условие: алгоритм должен работать за O(n)
# * Дополнительное условие: алгоритм должен работать за O(n) по времени и использовать O(1) доп памяти.
# """


def solve(nums):
    checked = set()
    result = []

    for x in nums:
        if x in checked:
            result.append(x)
        else:
            checked.add(x)

    return result

# @skip  # remove this to run tests
class T05(unittest.TestCase):
    testCases = [
        {"input": [[4, 3, 2, 7, 8, 2, 3, 1]], "expected": [2, 3]},
        {"input": [[1, 1, 2]], "expected": [1]},
        {"input": [[4, 3, 2, 7, 8, 3, 1]], "expected": [3]},
        {"input": [[5, 2, 3, 4, 1]], "expected": []},
        {"input": [[9, 5, 6, 3, 2, 5, 1, 4, 8, 6, 4, 9, 1, 2]],
         "expected": [1, 2, 4, 5, 6, 9]}
    ]

    def test(self):
        print("Executing: 05 Find all duplicates")

        for i, test in enumerate(self.testCases):
            with self.subTest(f"Test index: {i}"):
                input = test["input"]
                self.assertEqual(
                    sorted(solve(input[0])),
                    test["expected"]
                )
