import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(10, 5), 15)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-1, -1), -2)
        self.assertEqual(calculator.add(2.5, 2.5), 5.0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)
        self.assertEqual(calculator.subtract(-1, 1), -2)
        self.assertEqual(calculator.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(10, 5), 50)
        self.assertEqual(calculator.multiply(-1, 1), -1)
        self.assertEqual(calculator.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 5), 2)
        self.assertEqual(calculator.divide(-1, 1), -1)
        self.assertEqual(calculator.divide(-1, -1), 1)
        self.assertEqual(calculator.divide(5, 2), 2.5)
        # ทดสอบกรณีหารด้วย 0 ตามที่เขียนดักไว้ในโค้ดหลัก
        self.assertEqual(calculator.divide(10, 0), "ข้อผิดพลาด: ไม่สามารถหารด้วยศูนย์ได้")

if __name__ == '__main__':
    unittest.main()