# include 'Missing' category in the categorical features where there is a missing value
def add_missing(df, cat_missing_cols):
    df[cat_missing_cols] = df[cat_missing_cols].fillna('Missing')
    return df


def impute_normal_dist_cols(df, cols):
    for x in cols:
        df[x] = df[x].fillna(df[x].mean())
    return df


def impute_skewed(df, cols):
    for x in cols:
        df.loc[x] = df[x].fillna(df[x].median())
    return df


def frequency_encoder(df, cols):
    for col in cols:
        fe = df.groupby(col).size()/len(df)
        df[col+'_encoded'] = df[col].apply(lambda x: fe[x])
    return df
