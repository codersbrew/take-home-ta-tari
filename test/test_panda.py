from unittest import TestCase
import pandas as pd
import numpy as np

from homework.panda import calc_div_group


class TestCPV(TestCase):

    def setup_func(self):
        pass

    def teardown_func(self):
        pass

    def test_calc_div_group(self):
        print("Testing Division Calc")
        first = pd.DataFrame(np.arange(25).reshape((5, 5)), columns=['A', 'B', 'C', 'D', 'E'])
        result = calc_div_group(first, "A", "B")
        self.assertEqual(result, 0.91)

    def test_calc_div_group_by_zero(self):
        print("Testing Division Calc by Zero")
        first = pd.DataFrame(columns=['A', 'B'])
        first['A'] = pd.Series([1, 0])
        first['B'] = pd.Series([0.0, 0.0])
        result = calc_div_group(first, "A", "B")
        self.assertEqual(result, 0)
