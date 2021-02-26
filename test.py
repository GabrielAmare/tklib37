import unittest
from tklib37 import *
from datetime import datetime, date


class TestTypedEntry(unittest.TestCase):
    def test_001(self):
        tk = Tk()

        for value in [1, False, "x", 1.5, date.today(), datetime.now()]:
            type_ = type(value)

            entry = TypedEntry(tk, type_=type_, value=value)
            self.assertIsInstance(entry.get(), type_)

    def test_002(self):
        """Test that the number of calls to the callback function is equal to the number of changes of the value"""
        tk = Tk()

        d = {"n": 0}

        entry = TypedEntry(tk, type_=int, value=0, callback=lambda val: d.__setitem__("n", d["n"] + 1))

        for value in [0, 1, 1, 2, 2, 3, 3, 3, -5]:
            entry.set(value)

        self.assertEqual(d["n"], 4)


if __name__ == '__main__':
    unittest.main()
