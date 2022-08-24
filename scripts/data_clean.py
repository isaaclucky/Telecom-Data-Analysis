from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
minmax_scaler = MinMaxScaler()


def drop_cols(df:  pd.DataFrame, cols):
    for col in cols:
        df = df.drop(columns=col)
    return df

# mix-max scale the data between 0 and 1


def scale_dataframe(df: pd.DataFrame,cols):
    df = pd.DataFrame(data = minmax_scaler.fit_transform(df),columns=cols)
    return df


