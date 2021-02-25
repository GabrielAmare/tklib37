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


if __name__ == '__main__':
    unittest.main()
