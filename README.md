# Cloudfide recruitment task

## Virtual columns in pandas dataframe

You have a panda DataFrame with existing data and want to create a new DataFrame that includes
the original data along with an additional column calculated based on specified operations.
To achieve this, implement add_virtual_column function.

### Inputs
- df: Any pandas DataFrame
- role: A mathematical expression defining how to compute the values for the virtual column. For example, "first_column - second_column".
- new_column: The name of the new virtual column to be added. 

### Validations:
- Column labels must consist only of letters and underscores (_). 
- The function must support basic operations: addition (+), subtraction (-), and  multiplication (*). 
- If the role or any column label is incorrect, the function should return an empty DataFrame. 

### Additional requirements
- Role input has a form of: "column_name/operator/column_name" and there can be spaces separating and trailing each part of the expression
- Column types in df have valid addition, subtraction and multiplication operators