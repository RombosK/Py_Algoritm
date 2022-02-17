import unittest


def num_back(num1: int):
    num2 = 0
    while num1 > 0:
        digit = num1 % 10
        num1 //= 10
        num2 *= 10
        num2 += digit
    return num2

print(num_back(123))
print(num_back(89897177755))

# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(num_back(123), 321)
