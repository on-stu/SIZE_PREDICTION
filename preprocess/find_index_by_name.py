
def find_column_by_name():
    import csv

    csv_file = open("data_extracted.csv", "r", newline="" )

    f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

    header = next(f)
    to_search = input('검색어 입력 : ')
    isFound = False
    for i, col in enumerate(header):
        if(to_search in col):
            print(col, i)
            isFound = True
    if(not isFound):
        print('Not Found')