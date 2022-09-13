import csv

"""
header의 index
배꼽수준허리높이 : 19
허리높이 : 18
키 : 11
샅높이 : 22

전처리해야하는 새로운 필드

배꼽수준허리높이_A : (배꼽수준허리높이-샅높이)/키 -> (19 - 22) / 11
배꼽수준허리높이_B :  (허리높이-배꼽수준허리높이)/키 -> (18 - 19) / 11

허리높이_A : (허리높이-샅높이)/키 -> (18 - 22) / 11
허리높이_B : (허리높이-배꼽수준허리높이)/키 -> (18 - 19) / 11

"""


csv_file = open("data_extracted.csv", "r", newline="" )

f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

header = next(f)
rows = []

for row in f:
    rows.append(row)

def find_column_by_name():
    to_search = input('검색어 입력 : ')
    isFound = False
    for i, col in enumerate(header):
        if(to_search in col):
            print(col, i)
            isFound = True
    if(not isFound):
        print('Not Found')

def navel_waist_A(row):
    return (float(row[19]) - float(row[22])) / float(row[11])

def navel_waist_B(row):
    return (float(row[18]) - float(row[19])) / float(row[11])

def waist_A(row):
    return (float(row[18]) - float(row[22])) / float(row[11])

def waist_B(row):
    return (float(row[18]) - float(row[19])) / float(row[11])

def write_csv(col_names, values, file_path):
    file_open = open(file_path, 'w')
    for i, col in enumerate(col_names):
        col_name = str(col)
        file_open.write(col_name)
        if(i + 1 < len(col_names)):
            file_open.write(',')
        else:
            file_open.write('\n')

    for rows in values:
        rows = rows[1:]
        for i, row in enumerate(rows):
            row_string = str(row)
            file_open.write(row_string)
            if(i + 1 < len(rows)):
                file_open.write(',')
            else:
                file_open.write('\n')

def main():
    # find_column_by_name()
    new_columns = ["배꼽수준허리높이_A", "배꼽수준허리높이_B", "허리높이_A", "허리높이_B"]
    for new_column in new_columns:
        header.append(new_column)

    new_rows = []
    for row in rows:
        temp_row = row
        temp_row.append(navel_waist_A(temp_row))
        temp_row.append(navel_waist_B(temp_row))
        temp_row.append(waist_A(temp_row))
        temp_row.append(waist_B(temp_row))
        new_rows.append(temp_row)

    write_csv(header, new_rows, 'preprocessed.csv')
    


main()