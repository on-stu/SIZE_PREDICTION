import re
import pandas as pd

def write_csv(col_names, values, file_path):
    file_open = open(file_path, 'w')
    for i, col in enumerate(col_names):
        col_name = str(col)
        col_name = re.sub('\n', '', col_name)
        file_open.write(col_name)
        if(i + 1 < len(col_names)):
            file_open.write(',')
        else:
            file_open.write('\n')

    for rows in values:
        rows = rows[1:]
        for i, row in enumerate(rows):
            row_string = str(row)
            row_string = re.sub('\n', '', row_string)
            file_open.write(row_string)
            if(i + 1 < len(rows)):
                file_open.write(',')
            else:
                file_open.write('\n')

df = pd.read_excel(r'data/8data.xlsx', sheet_name=1)

cols = df.values[5][1:]
vals = df.values[6:]

write_csv(cols, vals, 'data_extracted.csv')


