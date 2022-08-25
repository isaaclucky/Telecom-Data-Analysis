
import unittest
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join("../")))
sys.path.append(os.path.abspath(os.path.join("scripts")))

from data_clean import *
from data_preprocess import *





class Test_preprocess(unittest.TestCase):

    def test_impute_skewed(self):
        df = pd.read_pickle('data/sample.pkl')
        df_imp = pd.read_pickle('data/sample_impute.pkl')
        col_imp = [x for x in df.columns if df[x].isnull().sum()>0 and df[x].dtype=='float64' ]

        self.assertEqual(df_imp.values.all(), impute_skewed(df=df[col_imp],cols=col_imp).values.all())
        
        
        
        
        


if __name__ == '__main__':
    unittest.main()
