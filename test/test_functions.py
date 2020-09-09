import unittest
from main import camper_age_input

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(72, camper_age_input.convert_to_months(6))


if __name__ == '__main__':
    unittest.main()
