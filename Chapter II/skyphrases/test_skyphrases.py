import unittest
from skyphrases import check_valid_skyphrases


class TestSkyphrase(unittest.TestCase):
    def test_valid_skyphrase(self):
        skyphrase = ['aa bb cc dd ee']
        self.assertTrue(check_valid_skyphrases(skyphrase))
        skyphrase = ['aa bb cc dd aaa']
        self.assertTrue(check_valid_skyphrases(skyphrase))

    def test_invalid_skyphrase(self):
        skyphrase = ['aa bb cc dd aa']
        self.assertFalse(check_valid_skyphrases(skyphrase))
        skyphrase = ['aa bb cc dd bb']
        self.assertFalse(check_valid_skyphrases(skyphrase))


if __name__ == '__main__':
    unittest.main()
