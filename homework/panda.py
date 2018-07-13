import pandas as pd


def calc_div_group(group, numerator, denominator):
    """
    CPV = Spend / Views
    :param group: Group Series from pandas .apply()
    :param numerator:
    :param denominator:
    :return: float round(2)
    """
    try:
        value = round(float(group[numerator].sum() / group[denominator].sum()), 2)
    except ZeroDivisionError:
        value = 0
    return value


def cpv_creatives(spots):
    """
    Use Pandas DataFrame to group by creative and aggregate spend and views to find cpv
    :param spots: list of Spot Objects
    :return: panda dataFrame grouped and aggregated
    """
    df = pd.DataFrame([[s.creative, s.date, s.rotation, s.spend, s.time, s.views, s] for s in spots],
                      columns=['creative', 'date', 'rotation', 'spend', 'time', 'views', 'spot'])
    results = df.groupby('creative').apply(lambda x: calc_div_group(x, "spend", "views"))
    return results


def cpv_rotations_days(spots):
    """
    Use Pandas DataFrame to group by date,rotation and aggregate spend and views to find cpv
    :param spots: list of Spot Objects
    :return: panda dataFrame groups and aggregated
    """
    df = pd.DataFrame([[s.creative, s.date, s.rotation, s.spend, s.time, s.views, s] for s in spots],
                      columns=['creative', 'date', 'rotation', 'spend', 'time', 'views', 'spot'])
    real = un_nest(df, 'rotation')
    results = real.groupby(['date', 'rotation']).apply(lambda x: calc_div_group(x, "spend", "views"))
    return results


def un_nest(df, col, reset_index=False):
    """
    This took a while to do, if I have a nested column I need to expand it
    borrowed a few lines from stack exchange as I am not 100% savvy with py pandas
    :param df: data frame
    :param col: column that needs unnested
    :param reset_index: reset index in dataframe
    :return:
    """
    col_flat = pd.DataFrame([[i, x]
                             for i, y in df[col].apply(list).iteritems()
                             for x in y], columns=['I', col])
    col_flat = col_flat.set_index('I')
    df = df.drop(col, 1)
    # Merge in list expansion after removing original series
    df = df.merge(col_flat, left_index=True, right_index=True)
    if reset_index:
        df = df.reset_index(drop=True)
    return df
