import pandas
import re

def add_virtual_column(df: pandas.DataFrame, role: str, new_column: str) -> pandas.DataFrame:
    # role and new_column contain only allowed symbols
    if re.search("[^a-zA-Z_ +*-]", role) or re.search("[^a-zA-Z_]", new_column):
        return pandas.DataFrame([])

    split_role = re.findall("[a-zA-Z_]+|[+*-]", role)

    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
    }

    # role has exact structure of "column_name operator column_name"
    if (len(split_role) == 3
            and split_role[1] in operations.keys()
            and split_role[2] in df.columns
            and split_role[0] in df.columns):
        df[new_column] = operations[split_role[1]](df[split_role[0]], df[split_role[2]])
        return df

    return pandas.DataFrame([])
