import missingno as msno
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import numpy as np
import pandas as pd

minmax_scaler = MinMaxScaler()


def fix_outlier(df, column):
    df[column] = np.where(df[column] > df[column].quantile(
        0.95), df[column].median(), df[column])

    return df[column]


def get_numerical_summary(df, missing_cols):
    total = df.shape[0]
    missing_percent = {}
    for col in missing_cols:
        null_count = df[col].isnull().sum()
        per = (null_count/total) * 100
        missing_percent[col] = per
        print("{} : {} ({}%)".format(col, null_count, round(per, 3)))
    return missing_percent


# Checking unique values from Categorical Columns
def get_value_counts(df):
    print('----------------------------------')
    for col in df.columns[(df.dtypes == 'object').values].tolist():
        print(col, '\n')
        print(df[col].value_counts())
        print('----------------------------------')


def data_description(df, df_desc, cols):
    for name in cols:
        col_index = df_desc[df_desc['Fields'] == name].index
        if col_index.size > 0:
            print(name + " ==  " + df_desc['Description'].iloc[col_index[0]])


def plot_missingno(df):
    msno.matrix(df)
    plt.figure(figsize=(100, 60))
    plt.show()


def top_handsets_per_top_manufactueres(df, manufacturers, handsets):
    m = list(df['Handset Manufacturer'].value_counts().index[:manufacturers])
    print("Top " + str(handsets) + " Handsets per top " +
          str(manufacturers) + " Manufacturers is: \n")
    for i in m:
        print("Top " + str(m.index(i)+1) + " Manufacturer: " +
              i + "\n And top products are :")
        h = list(df.groupby(['Handset Manufacturer']).get_group(
            i)['Handset Type'].value_counts().index[:handsets])
        h_v = list(df.groupby(['Handset Manufacturer']).get_group(i)[
                   'Handset Type'].value_counts()[:handsets])
        h_sum = df.groupby(['Handset Manufacturer']).get_group(i)[
            'Handset Type'].value_counts().sum()
        for j in h:
            print("\t\t" + str(h.index(j)+1) + "." + j + ":  " +
                  str((h_v[h.index(j)]/h_sum*100).round(3)) + "%")


def scaler_plot(df):
    scaled_data = minmax_scaler.fit_transform(df)

    # plot both together to compare
    fig, ax = plt.subplots(1, 2, figsize=(10, 6))
    sns.histplot(df, ax=ax[0])
    ax[0].set_title("Original Data")
    sns.histplot(scaled_data, ax=ax[1])
    ax[1].set_title("Scaled data")




# Function to calculate missing values by column

def format_float(value):
    return f'{value:,.2f}'


def find_agg(df: pd.DataFrame, agg_column: str, agg_metric: str, col_name: str, top: int, order=False) -> pd.DataFrame:

    new_df = df.groupby(agg_column)[agg_column].agg(agg_metric).reset_index(name=col_name).\
        sort_values(by=col_name, ascending=order)[:top]

    return new_df


def convert_bytes_to_megabytes(df, bytes_data):
    """
        This function takes the dataframe and the column which has the bytes values
        returns the megabytesof that value

        Args:
        -----
        df: dataframe
        bytes_data: column with bytes values

        Returns:
        --------
        A series
    """

    megabyte = 1*10e+5
    df[bytes_data] = df[bytes_data] / megabyte
    return df[bytes_data]


def fix_outlier(df, column):
    df[column] = np.where(df[column] > df[column].quantile(
        0.95), df[column].median(), df[column])

    return df[column]


###################################PLOTTING FUNCTIONS###################################

def plot_hist(df: pd.DataFrame, column: str, color: str) -> None:
    # plt.figure(figsize=(15, 10))
    # fig, ax = plt.subplots(1, figsize=(12, 7))
    sns.displot(data=df, x=column, color=color, kde=True, height=7, aspect=2)
    plt.title(f'Distribution of {column}', size=20, fontweight='bold')
    plt.show()


def plot_count(df: pd.DataFrame, column: str) -> None:
    plt.figure(figsize=(12, 7))
    sns.countplot(data=df, x=column)
    plt.title(f'Distribution of {column}', size=20, fontweight='bold')
    plt.show()


def plot_bar(df: pd.DataFrame, x_col: str, y_col: str, title: str, xlabel: str, ylabel: str) -> None:
    plt.figure(figsize=(12, 7))
    sns.barplot(data=df, x=x_col, y=y_col)
    plt.title(title, size=20)
    plt.xticks(rotation=75, fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel(xlabel, fontsize=16)
    plt.ylabel(ylabel, fontsize=16)
    plt.show()


def plot_heatmap(df: pd.DataFrame, title: str, cbar=False) -> None:
    plt.figure(figsize=(12, 7))
    sns.heatmap(df, annot=True, cmap='viridis', vmin=0,
                vmax=1, fmt='.2f', linewidths=.7, cbar=cbar)
    plt.title(title, size=18, fontweight='bold')
    plt.show()


def plot_box(df: pd.DataFrame, x_col: str, title: str) -> None:
    plt.figure(figsize=(12, 7))
    sns.boxplot(data=df, x=x_col)
    plt.title(title, size=20)
    plt.xticks(rotation=75, fontsize=14)
    plt.show()


def plot_box_multi(df: pd.DataFrame, x_col: str, y_col: str, title: str) -> None:
    plt.figure(figsize=(12, 7))
    sns.boxplot(data=df, x=x_col, y=y_col)
    plt.title(title, size=20)
    plt.xticks(rotation=75, fontsize=14)
    plt.yticks(fontsize=14)
    plt.show()


def plot_scatter(df: pd.DataFrame, x_col: str, y_col: str, title: str, hue: str, style: str) -> None:
    plt.figure(figsize=(12, 7))
    sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue, style=style)
    plt.title(title, size=20)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.show()


pd.options.display.float_format = format_float
