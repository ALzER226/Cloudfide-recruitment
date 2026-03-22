import pandas
import re

def add_virtual_column(df: pandas.DataFrame, role: str, new_column: str) -> pandas.DataFrame:
    # role and new_column contain only allowed symbols
    if re.search("[^a-zA-Z_ +*-]", role) or re.search("[^a-zA-Z_]", new_column):
        return pandas.DataFrame([])

    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
    }

    split_role = re.findall("[a-zA-Z_]+|[+*-]", role)

    column1 = split_role[0]
    column2 = split_role[2]
    operation = split_role[1]

    # role has exact structure of "column_name operator column_name"
    if not (len(split_role) == 3 and operation in operations.keys()):
        return pandas.DataFrame([])

    # columns provided in role are inside Dataframe
    if not(column1 in df.columns and column2 in df.columns):
        return pandas.DataFrame([])

    df[new_column] = operations[operation](df[column1], df[column2])
    return df
