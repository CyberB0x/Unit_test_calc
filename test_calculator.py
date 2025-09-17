import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def setUp(self):
        print("\n[Начала теста]")

    def tearDown(self):
        print("[Завершение теста]")


    def test_add(self):
        print("Тест: сложение 2 + 3")
        result = add(2,3)
        self.assertEqual(result, 5)
        print("Пройден: 2 + 3 = 5")

    def test_subtract(self):
        print("Тест: вычитание 5 - 2")
        result = subtract(5,2)
        self.assertEqual(result, 3)
        print("Пройден: 5 - 2 = 3")


    def test_multiply(self):
        print("Тест: умножение 4 * 3")
        result = multiply(4, 3)
        self.assertEqual(result, 12)
        print("Пройден 4 * 3 = 12")

    def test_divide(self):
        print("Тест: деление 10 / 2")
        result = divide(10,2)
        self.assertEqual(result, 5)
        print("Пройден: 10 / 2 = 5")

    def test_divide_by_zero(self):
        print("Тест: деление на 0 должен вызвать ошибку")
        with self.assertRaises(ValueError):
            divide(5,0)
        print("Пройден: корректно обработано деление на ноль")

if __name__ == "__main__":
    unittest.main()


