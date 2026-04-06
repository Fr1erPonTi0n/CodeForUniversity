from unittest import TestCase
import random

def total(n1, n2):
    return n1 + n2

class TotalTestCase(TestCase):
    def test_total(self) -> None:
        n1 = random.randint(1, 100)
        n2 = random.randint(1, 100)
        result = total(n1, n2)
        expected_result = n1 + n2
        self.assertEqual(result, expected_result)
