"""
This module migrates the existing quilt database to neo4j database
"""

import quilt
import pandas as pd
import numpy as np


def preprocess(df, drop_col=None, drop_na=False, strip_col=None):
    if drop_col is not None:
        df = df.drop(drop_col, axis=1)
    if drop_na:
        df.replace([""], float("NaN"), inplace=True)
        df.dropna(inplace=True)
    if strip_col is not None:
        df[strip_col] = df[strip_col].apply(lambda x: x.strip())
    return df


def setup_dfs():
    "returns the tables in the quilt database"
    app = quilt.load('qxf2/dev_survey')
    # users
    users = app.users()
    users['fullName'] = users['first_name'] + " " + users['last_name']
    users = preprocess(users, strip_col="fullName")
    users.columns = ['ID','firstName','lastName', 'email', "author_name", 'status', 'fullName']
    # response
    response = app.response()
    response = preprocess(response, drop_col="id", strip_col='answer')
    response['date'] = pd.to_datetime(response['date'], errors = 'coerce', format = '%Y-%m-%d').dt.strftime("%Y-%m-%d")
    # technology
    technology = app.technology()
    technology = preprocess(technology, drop_na=True, strip_col='technology')
    return users, response, technology


def get_help_dates(response, question_no=None, help=None):
    "returns datafame with employee ids and help taken/given employee names along with the dates"
    df_list = []
    for i, help_type in zip(question_no, help):
        df = response.loc[response['question_no'] == i]
        df['answer'].replace('', np.nan, inplace=True)
        df.dropna(subset=['answer'], inplace=True)
        df = (df.groupby(['respondent_id', 'answer'])['date'].apply(set)).apply(list)\
                                                          .reset_index(name=help_type)
        df_list.append(df)
        df.columns = ['ID',f"{help_type}_names", f"{help_type}_dates"]
    help_taken_names, help_given_names = [df_list[i] for i in [0, 1]]
    return help_taken_names, help_given_names


def get_first_seen_date(df):
    "returns datafame with technologies and the dates of their first entry in the database"
    df['technology'] = df['technology'].str.upper()
    df = (df.groupby('technology')['date'].apply(list)).reset_index(name='first_seen')
    df['first_seen'] = df.first_seen.sort_values().apply(lambda x: sorted(x)[0])
    df['first_seen'] = pd.DataFrame(df['first_seen']).reset_index(drop=True)
    df.columns = ['technology_name','first_seen']
    df = preprocess(df, drop_na=True)
    return df


def get_technology_learnt_dates(df):
    "returns datafame with employee ids and the technologies learnt along with the dates"
    df1 = (df.groupby(['respondent_id', 'technology'])['date']).apply(list).\
                                             reset_index(name="learnt_dates")
    df1['technology'] = df1['technology'].str.upper()
    df1.columns = ['ID','technology_name', 'learnt_dates']
    return df1


def merge_dfs(df1, df2):
    "returns the merged dataframe of the given two dataframes on a common column"
    df1['ID']=df1['ID'].astype('int64')
    merged = df1.join(df2.set_index('ID'), on='ID', how='left')
    columns = ['fullName'] + list(df2.columns)
    merged = merged[columns]
    merged = merged.drop(["ID"], axis=1)
    return merged


if __name__ == "__main__":
    users, response, technology = setup_dfs()
    # employee
    users.to_csv("employee.csv")
    # employee relationship
    helptaken_dates, helpgiven_dates = get_help_dates(response, [1, 2], ['helptaken','helpgiven'])
    employee_helptaken = merge_dfs(users, helptaken_dates)
    employee_helptaken.to_csv("employee_helptaken.csv")
    employee_helpgiven = merge_dfs(users, helpgiven_dates)
    employee_helpgiven.to_csv("employee_helpgiven.csv")
    # technology
    technology1 = get_first_seen_date(technology)
    technology1.to_csv("technology.csv")
    # technology relationship
    technology_learnt = get_technology_learnt_dates(technology)
    technology1 = merge_dfs(users, technology_learnt)
    technology1.to_csv("technology_relationship.csv")
