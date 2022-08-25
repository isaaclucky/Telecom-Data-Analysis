import unittest
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join("../")))
sys.path.append(os.path.abspath(os.path.join("scripts")))
from data_clean import *

df_temp = pd.DataFrame(data=[[4, 5, 37, 10], [3, 44, 5, 6], [
                               23, 4, 34, 5]], columns=['A', 'B', 'C', 'D'])


class Test_clean_df(unittest.TestCase):

    def test_drop_cols(self):
        

        df_check = drop_cols(df=df_temp, cols='A')

        self.assertEqual(3, df_check.columns.shape[0])

    def test_scale_dataframe(self):
        
        df_temp_scaled = scale_dataframe(df=df_temp, cols=['A', 'B', 'C', 'D'])
        df_scaled = pd.DataFrame([[0.05, 0.02, 1.00, 1.00], [0.00, 1.00,	0.00, 0.20], [
            1.00, 0.00,	0.91, 0.00]], columns=['A', 'B', 'C', 'D'])

        self.assertEqual(df_temp_scaled.values.all(), df_scaled.values.all())


if __name__ == '__main__':
    unittest.main()
