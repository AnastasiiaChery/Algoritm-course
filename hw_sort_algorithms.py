import unittest
from unittest.case import skip

"""
 * Дан массив целых чисел nums, верните True если любое значение встречается в массиве хотя бы 2 раза, иначе верните False
 * Не используйте ассоциативные массивы/хештаблицы/словари и тд.
 * Пример:
 * Input: nums = [1,2,3,1]
 * Output: true
"""


def solve(nums):
    i=0
    while i<=len(nums)-1:
        m=i
        j=i+1
        while j<len(nums):
            if nums[j]<nums[m]:
                m=j
            j+=1

        nums[i], nums[m] = nums[m], nums[i]

        if i>0:
            if nums[i]==nums[i-1]:
                return True
        i += 1

    return False


# @skip  # remove this to run tests
class T01(unittest.TestCase):
    testCases = [
        {"input": [[1, 2, 3, 1]], "expected": True},
        {"input": [[2, 3, 4, 5]], "expected": False},
        {"input": [[1, 2, 3, 4, 5, 6]], "expected": False},
        {"input": [[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]], "expected": True},
        {"input": [[1]], "expected": False},
        {"input": [[100, 4, 2, 1, 49, 99]], "expected": False},
        {"input": [[-2, -2]], "expected": True}
    ]

    def test(self):
        print("Executing: 01 Contains duplicate")

        for i, test in enumerate(self.testCases):
            with self.subTest(f"Test index: {i}"):
              self.assertEqual(solve(test["input"][0]), test["expected"])



"""
 * Есть автомобиль с определенной вместительностью пассажиров. Авто движется только на восток (т.е. не может поворачивать и ехать на запад)
 * <p>
 * Вам даны вместительность автомобиля (целое число) и массив поездок trips,
 * где trips[i] = [numPassengers, from, to] означает что
 * ith поездка имеет numPassengers пассажиров и локации для начала и конца поездки - from и to.
 * Локации даны как число километров к востоку от изначальной локации автомобиля.
 * <p>
 * Верните True если возможно отвезти всех пассажиров по всем поездкам, иначе верните False
 * <p>
 * Пример:
 * Input: trips = [[2,1,5],[3,3,7]], capacity = 4
 * Output: false
 * <p>
 * Ограничения:
 * 1 <= trips.length <= 1000
 * trips[i].length == 3
 * 1 <= numPassengers <= 100
 * 0 <= from < to <= 1000
 * 1 <= capacity <= 105
"""


def solve(capacity, trips):
    trip_dict = {}
    for trip in trips:
        passenger, start, stop = trip
        trip_dict[start] = trip_dict.get(start, 0) + passenger
        trip_dict[stop] = trip_dict.get( stop, 0) - passenger

    curr = 0
    for loc in sorted(trip_dict.keys()):
        curr += trip_dict[loc]
        if curr > capacity:
            return False

    return True


# @skip  # remove this to run tests
class T02(unittest.TestCase):

    testCases = [
        {"input": [4, [[2, 1, 5], [3, 3, 7]]], "expected": False},
        {"input": [5, [[2, 1, 5], [3, 3, 7]]], "expected": True},
        {"input": [5, [[3, 3, 7], [2, 1, 8], [5, 8, 20]]], "expected": True},
        {"input": [2, [[2, 1, 2], [2, 5, 20], [2, 3, 4]]], "expected": True},
        {"input": [1, [[2, 1, 2], [2, 3, 4], [2, 5, 20]]], "expected": False},
        {"input": [3, [[1, 10, 15], [2, 3, 4], [2, 5, 20],
                       [2, 1, 2], [1, 17, 19]]], "expected": True},
        {"input": [5, [[2, 1, 5], [3, 3, 7], [5, 3, 9]]], "expected": False}
    ]

    def test(self):
        print("Executing: 02 Car pooling")

        for i, test in enumerate(self.testCases):
            with self.subTest(f"Test index: {i}"):
                self.assertEqual(solve(
                    test["input"][0], test["input"][1]), test["expected"])
