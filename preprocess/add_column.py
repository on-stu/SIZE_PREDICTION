from cmath import nan
import csv

"""
3d 측정이랑 직접 측정 둘 다 있으면 직접측정을 써서 만듦 -> 자동적으로 새로 생길 필드에 3d 측정값이 필요할 경우 nan으로 표기 -> 이후에 drop가능
header의 index
배꼽수준허리높이 : 96
배꼽수준허리둘레 : 43
허리높이 : 16
허리둘레 : 154
키 : 11
몸무게 : 82
샅높이 : 18
가는허리높이 (허리기준선높이) : 15
볼기고량높이 : 102
넙다리둘레 : 45
몸통수직길이 : 137
배너비 : 209
배두께 : 191
넙다리중간너비 : 212
엉덩이둘레 : 44

전처리해야하는 새로운 필드

가는허리높이_A : (가는허리높이 - 샅높이) / 키 -> (15 - 18) / 11

배꼽수준허리높이_A : (배꼽수준허리높이-샅높이)/키 -> (19 - 22) / 11
배꼽수준허리높이_B :  (허리높이-배꼽수준허리높이)/키 -> (18 - 19) / 11

허리높이_A : (허리높이-샅높이)/키 -> (18 - 22) / 11
허리높이_B : (허리높이-배꼽수준허리높이)/키 -> (18 - 19) / 11

배너비_A : 배너비 / 배두께 / 몸무게 -> 209 / 191 / 82
배너비_B : 배너비 / 몸무게 -> 209 / 83

배두께_A : 배너비 / 배두께 / 몸무게 -> 209 / 191 / 82
배두께_B : 배두께 / 몸무게 -> 191 / 82

샅높이_A : (샅높이 - 몸통수직길이) / 키 -> (18 - 137) / 11
샅높이_B : 샅높이 / 키 -> 18 / 11

샅길이_A : (허리높이 - 볼기고량높이) / 키 -> (16 - 102) / 11

허리둘레_A : (허리둘레 - 넙다리둘레) / 몸무게 -> (154 - 45) / 82
허리둘레_B : 허리둘레 / 몸무게 -> 154 / 82
허리둘레_C : 허리둘레 / 넙다리둘레 / 몸무게 -> 154 / 45 / 82
허리둘레_D : 허리둘레 / 엉덩이둘레 / 몸무게 -> 154 / 44 / 82
허리둘레_E : 허리둘레 * 0.5 / 넙다리둘레 / 몸무게 -> 154 * 0.5 / 45 / 82
허리둘레_F : (허리둘레 * 0.5 - 넙다리둘레) / 몸무게 -> (154 * 0.5 - 45) / 82
허리둘레_G : (배꼽수준허리둘레 - 허리둘레) / 몸무게 -> (43 - 154) / 82
허리둘레_H : 허리둘레 / 키 -> 154 / 82
허리둘레_I : (엉덩이둘레 - 배꼽수준허리둘레) / 몸무게 -> (44 - 43) / 82
허리둘레_J : (배꼽수준허리둘레 - 허리둘레) / 몸무게 ->  (43 - 154) / 82

배꼽수준허리둘레_A : 배꼽수준허리둘레 / 넙다리둘레 / 몸무게 -> 43 / 45 / 82
배꼽수준허리둘레_B : (배꼽수준허리둘레 - 허리둘레) / 몸무게 -> (43 - 154) / 82
배꼽수준허리둘레_C : (엉덩이둘레 - 배꼽수준허리둘레) / 몸무게 -> (44 - 43) / 82

엉덩이너비_A : 엉덩이너비 / 넙다리중간너비 / 몸무게 -> 43 / 212 / 82
엉덩이너비_B : 엉덩이너비 / 몸무게 -> 43 / 82

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

"""
가는허리높이_A : (가는허리높이 - 샅높이) / 키 -> (15 - 18) / 11
"""

def thin_waist_A(row):
    return (float(row[15]) - float(row[18])) / float(row[11])


"""
배꼽수준허리높이_A : (배꼽수준허리높이-샅높이)/키 -> (19 - 22) / 11
배꼽수준허리높이_B :  (허리높이-배꼽수준허리높이)/키 -> (18 - 19) / 11
"""

def navel_waist_A(row):
    return (float(row[19]) - float(row[22])) / float(row[11])

def navel_waist_B(row):
    return (float(row[18]) - float(row[19])) / float(row[11])


"""
허리높이_A : (허리높이-샅높이)/키 -> (18 - 22) / 11
허리높이_B : (허리높이-배꼽수준허리높이)/키 -> (18 - 19) / 11
"""

def waist_A(row):
    return (float(row[18]) - float(row[22])) / float(row[11])

def waist_B(row):
    return (float(row[18]) - float(row[19])) / float(row[11])


"""
배너비_A : 배너비 / 배두께 / 몸무게 -> 209 / 191 / 82
배너비_B : 배너비 / 몸무게 -> 209 / 83
"""

def stomach_width_A(row):
    return float(row[209]) / float(row[191]) / float(row[82])

def stomach_width_B(row):
    return float(row[209]) / float(row[82])

"""
배두께_A : 배너비 / 배두께 / 몸무게 -> 209 / 191 / 82
배두께_B : 배두께 / 몸무게 -> 191 / 82
"""

def stomach_thickness_A(row):
    return float(row[209]) / float(row[191]) / float(row[82])

def stomach_thickness_B(row):
    return float(row[191]) / float(row[82])

"""
샅높이_A : (샅높이 - 몸통수직길이) / 키 -> (18 - 137) / 11
샅높이_B : 샅높이 / 키 -> 18 / 11
"""

def sat_height_A(row):
    return (float(row[18]) - float(row[137])) / float(row[11])

def sat_height_B(row):
    return float(row[18]) / float(row[11])

"""
샅길이_A : (허리높이 - 볼기고량높이) / 키 -> (16 - 102) / 11
"""

def sat_length_A(row):
    return (float(row[16]) - float(row[102])) / float(row[11])

"""
허리둘레_A : (허리둘레 - 넙다리둘레) / 몸무게 -> (154 - 45) / 82
허리둘레_B : 허리둘레 / 몸무게 -> 154 / 82
허리둘레_C : 허리둘레 / 넙다리둘레 / 몸무게 -> 154 / 45 / 82
허리둘레_D : 허리둘레 / 엉덩이둘레 / 몸무게 -> 154 / 44 / 82
허리둘레_E : 허리둘레 * 0.5 / 넙다리둘레 / 몸무게 -> 154 * 0.5 / 45 / 82
허리둘레_F : (허리둘레 * 0.5 - 넙다리둘레) / 몸무게 -> (154 * 0.5 - 45) / 82
허리둘레_G : (배꼽수준허리둘레 - 허리둘레) / 몸무게 -> (43 - 154) / 82
허리둘레_H : 허리둘레 / 키 -> 154 / 82
허리둘레_I : (엉덩이둘레 - 배꼽수준허리둘레) / 몸무게 -> (44 - 43) / 82
허리둘레_J : (배꼽수준허리둘레 - 허리둘레) / 몸무게 ->  (43 - 154) / 82
"""

def waist_round_A(row):
    return (float(row[154]) - float(row[45])) / float(row[82])
def waist_round_B(row):
    return float(row[154]) / float(row[82])
def waist_round_C(row):
    return float(row[154]) / float(row[45]) / float(row[82])
def waist_round_D(row):
    return float(row[154]) / float(row[44]) / float(row[82])
def waist_round_E(row):
    return float(row[154]) * 0.5 / float(row[45]) / float(row[82])
def waist_round_F(row):
    return (float(row[154]) * 0.5 - float(row[45])) / float(row[82])
def waist_round_G(row):
    return (float(row[43]) - float(row[154])) / float(row[82])
def waist_round_H(row):
    return float(row[154]) /float(row[82])
def waist_round_I(row):
    return (float(row[44]) - float(row[43])) / float(row[82])
def waist_round_J(row):
    return (float(row[43]) - float(row[154])) / float(row[82])

"""
배꼽수준허리둘레_A : 배꼽수준허리둘레 / 넙다리둘레 / 몸무게 -> 43 / 45 / 82
배꼽수준허리둘레_B : (배꼽수준허리둘레 - 허리둘레) / 몸무게 -> (43 - 154) / 82
배꼽수준허리둘레_C : (엉덩이둘레 - 배꼽수준허리둘레) / 몸무게 -> (44 - 43) / 82
"""

def navel_waist_round_A(row):
    return float(row[43]) / float(row[45]) / float(row[82])
def navel_waist_round_B(row):
    return (float(row[43]) - float(row[154])) / float(row[82])
def navel_waist_round_C(row):
    return (float(row[44]) - float(row[43])) / float(row[82])

"""
엉덩이너비_A : 엉덩이너비 / 넙다리중간너비 / 몸무게 -> 43 / 212 / 82
엉덩이너비_B : 엉덩이너비 / 몸무게 -> 43 / 82
"""

def ass_width_A(row):
    return float(row[43]) / float(row[212]) / float(row[82])

def ass_width_B(row):
    return float(row[43]) / float(row[82])



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
        for i, row in enumerate(rows):
            row_string = str(row)
            file_open.write(row_string)
            if(i + 1 < len(rows)):
                file_open.write(',')
            else:
                file_open.write('\n')

def main():
    # find_column_by_name()
    new_columns = ["가는허리높이_A", "배꼽수준허리높이_A", "배꼽수준허리높이_B", "허리높이_A", "허리높이_B",
                "배너비_A", "배너비_B", "배두께_A", "배두께_B", "샅높이_A", "샅높이_B", "샅길이_A", "허리둘레_A",
                "허리둘레_B", "허리둘레_C", "허리둘레_D", "허리둘레_E", "허리둘레_F", "허리둘레_G", "허리둘레_H",
                "허리둘레_I", "허리둘레_J", "배꼽수준허리둘레_A", "배꼽수준허리둘레_B", "배꼽수준허리둘레_C",
                "엉덩이너비_A", "엉덩이너비_B"]
    for new_column in new_columns:
        header.append(new_column)

    new_rows = []
    for row in rows:
        temp_row = row
        temp_row.append(thin_waist_A(temp_row))
        temp_row.append(navel_waist_A(temp_row))
        temp_row.append(navel_waist_B(temp_row))
        temp_row.append(waist_A(temp_row))
        temp_row.append(waist_B(temp_row))
        temp_row.append(stomach_width_A(temp_row))
        temp_row.append(stomach_width_B(temp_row))
        temp_row.append(stomach_thickness_A(temp_row))
        temp_row.append(stomach_thickness_B(temp_row))
        temp_row.append(sat_height_A(temp_row))
        temp_row.append(sat_height_B(temp_row))
        temp_row.append(sat_length_A(temp_row))
        temp_row.append(waist_round_A(temp_row))
        temp_row.append(waist_round_B(temp_row))
        temp_row.append(waist_round_C(temp_row))
        temp_row.append(waist_round_D(temp_row))
        temp_row.append(waist_round_E(temp_row))
        temp_row.append(waist_round_F(temp_row))
        temp_row.append(waist_round_G(temp_row))
        temp_row.append(waist_round_H(temp_row))
        temp_row.append(waist_round_I(temp_row))
        temp_row.append(waist_round_J(temp_row))
        temp_row.append(navel_waist_round_A(temp_row))
        temp_row.append(navel_waist_round_B(temp_row))
        temp_row.append(navel_waist_round_C(temp_row))
        temp_row.append(ass_width_A(temp_row))
        temp_row.append(ass_width_B(temp_row))
        new_rows.append(temp_row)
        
    write_csv(header, new_rows, 'preprocessed_done.csv')
    


main()

