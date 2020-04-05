import pandas as pd


"""
Reads in as much data as it can from the provided input file
(assumed Excel format) reading from start_row, and only selecting
the requested columns.
"""
def read(input_file, start_row, columns):
    print('Reading from', input_file)
    df = pd.read_excel(
      input_file,
      sheet_name='Sheet1',
      skiprows=start_row - 1,
      usecols=columns,
      header=None
    )

    tuples = list(df.itertuples(index=False, name=None))

    return tuples
