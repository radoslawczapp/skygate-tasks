import unittest
from accounting import get_sum


class TestAccounting(unittest.TestCase):
    def test_none(self):
        self.assertEqual(get_sum(None), 0)

    def test_bool(self):
        self.assertEqual(get_sum(True), 0)
        self.assertEqual(get_sum(False), 0)

    def test_empty(self):
        self.assertEqual(get_sum(''), 0)
        self.assertEqual(get_sum([]), 0)
        self.assertEqual(get_sum({}), 0)

    def test_number(self):
        self.assertEqual(get_sum(15), 15)
        self.assertEqual(get_sum(-2), -2)
        self.assertEqual(get_sum(0), 0)

    def test_string(self):
        self.assertEqual(get_sum('string'), 0)
        self.assertEqual(get_sum('string}[]{'), 0)
        self.assertEqual(get_sum('string+-+'), 0)

    def test_list(self):
        self.assertEqual(get_sum(['a', -10, 'b', 'c', 100]), 90)
        self.assertEqual(get_sum([-10, 0, 100]), 90)
        self.assertEqual(get_sum([-10, True, 100]), 90)

    def test_dict(self):
        self.assertEqual(get_sum({'x': -10, 'y': 0, 'z': 100}), 90)
        self.assertEqual(get_sum({'x': -10, 'y': 100, 'z': 'string'}), 90)
        self.assertEqual(get_sum({'a': 100, 'x': -10, 'y': False, 'z': 'string'}), 90)

    def test_nesting(self):
        self.assertEqual(get_sum([-10, [0], [[100]]]), 90)
        self.assertEqual(get_sum({'a': {'b': -10}, 0: 100}), 90)
        self.assertEqual(get_sum({'a': 'string+-10', 'b': [0, 100]}), 90)


if __name__ == '__main__':
    unittest.main()
