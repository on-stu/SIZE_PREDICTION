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

허리두께_A : 허리너비 / 허리두께 / 몸무게
허리두께_B : 허리두께 / 몸무게
허리두께_C : 허리두께/넙다리두께/몸무게

배꼽수준허리두께_A : 배꼽수준허리두께/몸무게
배꼽수준허리두께_B : 배꼽수준허리두께/넙다리두께/몸무게

배너비_A : 배너비/배두께/몸무게
배너비_B : 배너비 / 몸무게

배두께_A : 배너비 / 배두께 / 몸무게
배두께_B : 배두께 / 몸무게

배높이_A : 배높이 / 키

가는허리높이_A : (가는허리높이 - 샅높이) / 키 -> (15 - 18) / 11

배꼽수준허리높이_A : (배꼽수준허리높이-샅높이)/키 -> (19 - 22) / 11
배꼽수준허리높이_B :  (허리높이-배꼽수준허리높이)/키 -> (18 - 19) / 11
배꼽수준허리높이_C : 배꼽수준허리높이/키 -> 19 / 11

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

엉덩이둘레_A : 허리둘레-엉덩이둘레/몸무게 -> (42 - 44) / 82
엉덩이둘레_B : 엉덩이둘레/몸무게 -> 44 / 82

배꼽수준샅앞뒤길이_A : 배꼽수준샅앞뒤길이/몸무게 -> 180 / 82

엉덩이두께_A : 엉덩이너비/엉덩이두께/몸무게 -> 43 / 192 / 82
엉덩이두께_B : 엉덩이두께/몸무게 -> 192 / 82

엉덩이수직길이_A : 엉덩이수직길이/키 -> 138 / 11

엉덩이옆길이_A : 엉덩이옆길이/키 -> 221 / 11

샅앞뒤길이_A : 샅앞뒤길이/키 -> 51 / 11

넙다리중간둘레_A : 넙다리중간둘레/몸무게 -> 166 / 82
넙다리중간둘레_B : 엉덩이둘레/넙다리중간둘레/몸무게 -> 44 /166 / 82

넙다리둘레_A : 넙다리둘레/몸무게 -> 45 / 82
넙다리둘레_B : 허리둘레/넙다리둘레/몸무게 -> 42 / 45 / 82
넙다리둘레_C : 장딴지최대둘레/넙다리둘레/몸무게 -> 169 / 45 / 82
넙다리둘레_D : 무릎둘레/넙다리둘레/몸무게 -> 46 / 45 / 82

넙다리너비_A : 넙다리너비/몸무게 -> 211 / 82
넙다리너비_B : (넙다리너비-넙다리중간너비)/몸무게 -> (211-212)/82
넙다리너비_C : 넙다리너비/엉덩이너비/몸무게 -> 211/43/82

넙다리중간너비_A : 넙다리중간너비/몸무게 -> 212 / 82

넙다리두께_A : 넙다리두께/몸무게 
넙다리두께_B : (넙다리두께-넙다리중간두께)/몸무게

넙다리중간두께_A : 넙다리중간두께/몸무게

넙다리직선길이_A : 넙다리직선길이/키

무릎둘레_A : 무릎둘레/넙다리중간둘레/몸무게
무릎둘레_B : 무릎둘레/몸무게

무릎너비_A : 무릎너비/넙다리중간너비/몸무게
무릎너비_B : 무릎너비/몸무게

장딴지최대둘레_A : 장딴지최대둘레/몸무게
장딴지최대둘레_B : 장딴지최대둘레/넙다리중간둘레/몸무게

장딴지둘레_A : 장딴지둘레/몸무게
장딴지둘레_B : 장딴지둘레/넙다리중간둘레/몸무게

장딴지너비_A : 장딴지너비/몸무게
장딴지너비_B : 장딴지너비/넙다리중간너비/몸무게

장딴지두께_A : 장딴지두께/몸무게
장딴지두께_B : 장딴지두께/넙다리중간두께/몸무게

정강뼈위점높이_A : 무릎높이/키

장딴지높이_A : 장딴지높이/키
장딴지높이_B : 장딴지높이/볼기고랑높이/키

무릎높이_A : 무릎높이/키
무릎높이_B : 위앞엉덩뼈가시높이/무릎높이/키

발목둘레_A : 발목둘레/몸무게
발목둘레_B : 장딴지둘레/발목둘레/키

발목최대둘레_A : 발목최대둘레/몸무게
발목최대둘레_B : 발목최대둘레/장딴지최대둘레/몸무게

발목너비_A : 발목너비/몸무게
발목너비_B : 장딴지너비/발목너비/몸무게

종아리최소둘레_A : 종아리최소둘레/몸무게
종아리최소둘레_B : 종아리최소둘레/장딴지최대둘레/몸무게

종아리아래너비_A : 종아리아래너비/몸무게
종아리아래너비_B : 종아리아래너비/장딴지너비/몸무게

종아리아래두께_A : 종아리아래두께/몸무게
종아리아래두께_B : 종아리아래두께/장딴지두께/몸무게

가쪽복사높이_A : 가쪽복사높이/키
가쪽복사높이_B : 가쪽복사높이/장딴지높이/키

다리가쪽길이_A : 다리가쪽길이/키

다리안쪽높이_A : 다리안쪽높이(볼기고랑높이)/키

위앞엉덩뼈가시높이_A : 위앞엉덩뼈가시높이/키

엉덩이높이_A : 엉덩이높이/키

엉덩이최대둘레높이_A : 엉덩이최대둘레높이/키

뒤허리높이_A : 뒤허리높이/키

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
허리두께_A : 허리너비 / 허리두께 / 몸무게
허리두께_B : 허리두께 / 몸무게
허리두께_C : 허리두께/넙다리두께/몸무게
"""
def waist_thick_A(row):
    return float(row[23]) / float(row[28]) / float(row[82])

def waist_thick_B(row):
    return float(row[28]) / float(row[82])

def waist_thick_C(row):
    return float(row[28])/float(row[193])/float(row[82])



"""
배꼽수준허리두께_A : 배꼽수준허리두께/몸무게
배꼽수준허리두께_B : 배꼽수준허리두께/넙다리두께/몸무게
"""
def navel_waist_thick_A(row):
    return float(row[190])/float(row[82])

def navel_waist_thick_B(row):
    return float(row[190])/float(row[193])/float(row[82])


"""
배높이_A : 배높이 / 키
"""

def stomach_height_A(row):
    return float(row[97]) / float(row[11])

"""
가는허리높이_A : (가는허리높이 - 샅높이) / 키 -> (15 - 18) / 11
"""

def thin_waist_A(row):
    return (float(row[15]) - float(row[18])) / float(row[11])


"""
배꼽수준허리높이_A : (배꼽수준허리높이-샅높이)/키 -> (19 - 22) / 11
배꼽수준허리높이_B :  (허리높이-배꼽수준허리높이)/키 -> (18 - 19) / 11
배꼽수준허리높이_C : 배꼽수준허리높이/키 -> 19 / 11
"""

def navel_waist_A(row):
    return (float(row[19]) - float(row[22])) / float(row[11])

def navel_waist_B(row):
    return (float(row[18]) - float(row[19])) / float(row[11])

def navel_waist_C(row):
    return float(row[19]) / float(row[11])


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


"""
엉덩이둘레_A : 허리둘레-엉덩이둘레/몸무게 -> (42 - 44) / 82
엉덩이둘레_B : 엉덩이둘레/몸무게 -> 44 / 82
"""

def ass_round_A(row):
    return (float(row[42]) - float(row[44])) / float(row[82])

def ass_round_B(row):
    return float(row[44]) / float(row[82])

"""
배꼽수준샅앞뒤길이_A : 배꼽수준샅앞뒤길이/몸무게 -> 180 / 82
"""

def navel_sat_A(row):
    return float(row[180]) / float(row[82])

"""
엉덩이두께_A : 엉덩이너비/엉덩이두께/몸무게 -> 43 / 192 / 82
엉덩이두께_B : 엉덩이두께/몸무게 -> 192 / 82
"""

def ass_thick_A(row):
    return float(row[43]) / float(row[192]) / float(row[82])

def ass_thick_B(row):
    return float(row[192]) / float(row[82])

"""
엉덩이수직길이_A : 엉덩이수직길이/키 -> 138 / 11
"""

def ass_vertical_length_A(row):
    return float(row[138]) / float(row[11])

"""
엉덩이옆길이_A : 엉덩이옆길이/키 -> 221 / 11
"""
def ass_side_length_A(row):
    return float(row[221]) /float(row[11])

"""
샅앞뒤길이_A : 샅앞뒤길이/키 -> 51 / 11
"""

def sat_front_back_A(row):
    return float(row[51]) / float(row[11])


"""
넙다리중간둘레_A : 넙다리중간둘레/몸무게 -> 166 / 82
넙다리중간둘레_B : 엉덩이둘레/넙다리중간둘레/몸무게 -> 44 /166 / 82
"""

def nub_leg_middle_round_A(row):
    return  float(row[166]) / float(row[82])

def nub_leg_middle_round_B(row):
    return  float(row[44]) /float(row[166]) / float(row[82])

"""
넙다리둘레_A : 넙다리둘레/몸무게 -> 45 / 82
넙다리둘레_B : 허리둘레/넙다리둘레/몸무게 -> 42 / 45 / 82
넙다리둘레_C : 장딴지최대둘레/넙다리둘레/몸무게 -> 169 / 45 / 82
넙다리둘레_D : 무릎둘레/넙다리둘레/몸무게 -> 46 / 45 / 82
"""

def nub_leg_round_A(row):
    return float(row[45]) / float(row[82])

def nub_leg_round_B(row):
    return float(row[42]) / float(row[45]) / float(row[82])

def nub_leg_round_C(row):
    return float(row[169]) / float(row[45]) / float(row[82])

def nub_leg_round_D(row):
    return float(row[46]) / float(row[45]) / float(row[82])

"""
넙다리너비_A : 넙다리너비/몸무게 -> 211 / 82
넙다리너비_B : (넙다리너비-넙다리중간너비)/몸무게 -> (211-212)/82
넙다리너비_C : 넙다리너비/엉덩이너비/몸무게 -> 211/43/82
"""
def nub_leg_width_A(row):
    return float(row[211]) / float(row[82])

def nub_leg_width_B(row):
    return (float(row[211])-float(row[212]))/float(row[82])

def nub_leg_width_C(row):
    return float(row[211])/float(row[43])/float(row[82])


"""
넙다리중간너비_A : 넙다리중간너비/몸무게 -> 212 / 82
"""
def nub_leg_middle_width_A(row):
    return float(row[212]) / float(row[82])

"""
넙다리두께_A : 넙다리두께/몸무게 
넙다리두께_B : (넙다리두께-넙다리중간두께)/몸무게
"""

def nub_leg_thick_A(row):
    return  float(row[193])/float(row[82]) 

def nub_leg_thick_B(row):
    return  (float(row[193])-float(row[194]))/float(row[82])

"""
넙다리중간두께_A : 넙다리중간두께/몸무게
"""

def nub_middle_thick_A(row):
    return  float(row[194])/float(row[82])

"""
넙다리직선길이_A : 넙다리직선길이/키
"""
def nub_line_length_A(row):
    return float(row[140])/float(row[11])

"""
무릎둘레_A : 무릎둘레/넙다리중간둘레/몸무게
무릎둘레_B : 무릎둘레/몸무게
"""
def knee_round_A(row):
    return float(row[46])/float(row[166])/float(row[82])

def knee_round_B(row):
    return float(row[46])/float(row[82])

"""
무릎너비_A : 무릎너비/넙다리중간너비/몸무게
무릎너비_B : 무릎너비/몸무게
"""
def knee_width_A(row):
    return float(row[213])/float(row[212])/float(row[82])

def knee_width_B(row):
    return float(row[213])/float(row[82])

"""
장딴지최대둘레_A : 장딴지최대둘레/몸무게
장딴지최대둘레_B : 장딴지최대둘레/넙다리중간둘레/몸무게
"""
def jang_max_round_A(row):
    return float(row[169])/float(row[82])

def jang_max_round_B(row):
    return float(row[169])/float(row[166])/float(row[82])


"""
장딴지둘레_A : 장딴지둘레/몸무게
장딴지둘레_B : 장딴지둘레/넙다리중간둘레/몸무게
"""
def jang_round_A(row):
    return float(row[47])/float(row[82])

def jang_round_B(row):
    return float(row[47])/float(row[166])/float(row[82])

"""
장딴지너비_A : 장딴지너비/몸무게
장딴지너비_B : 장딴지너비/넙다리중간너비/몸무게
"""
def jang_width_A(row):
    return float(row[215])/float(row[82])

def jang_width_B(row):
    return float(row[215])/float(row[212])/float(row[82])

"""
장딴지두께_A : 장딴지두께/몸무게
장딴지두께_B : 장딴지두께/넙다리중간두께/몸무게
"""

def jang_thick_A(row):
    return float(row[197])/float(row[82])

def jang_thick_B(row):
    return float(row[197])/float(row[194])/float(row[82])

"""
장딴지높이_A : 장딴지높이/키
장딴지높이_B : 장딴지높이/볼기고량높이/키
"""
def jang_height_A(row):
    return float(row[105])/float(row[11])

def jang_height_B(row):
    return float(row[105])/float(row[102])/float(row[11])

"""
정강뼈위점높이_A : 무릎높이/키
"""
def jung_bone_height_A(row):
    return float(row[104])/float(row[11])


"""
무릎높이_A : 무릎높이/키
무릎높이_B : 위앞엉덩뼈가시높이/무릎높이/키
"""
def knee_height_A(row):
    return float(row[104])/float(row[11])

def knee_height_B(row):
    return float(row[17])/float(row[104])/float(row[11])


"""
발목둘레_A : 발목둘레/몸무게
발목둘레_B : 장딴지둘레/발목둘레/키
"""
def ankle_round_A(row):
    return float(row[363])/float(row[82])
def ankle_round_B(row):
    return float(row[47])/float(row[363])/float(row[11])

"""
발목최대둘레_A : 발목최대둘레/몸무게
발목최대둘레_B : 발목최대둘레/장딴지최대둘레/몸무게
"""
def ankle_max_round_A(row):
    return float(row[171])/float(row[82])
def ankle_max_round_B(row):
    return float(row[171])/float(row[169])/float(row[82])

"""
발목너비_A : 발목너비/몸무게
발목너비_B : 장딴지너비/발목너비/몸무게
"""
def ankle_width_A(row):
    return float(row[25])/float(row[82])
def ankle_width_B(row):
    return float(row[215])/float(row[25])/float(row[82])

"""
종아리최소둘레_A : 종아리최소둘레/몸무게
종아리최소둘레_B : 종아리최소둘레/장딴지최대둘레/몸무게
"""
def jong_min_round_A(row):
    return float(row[170])/float(row[82])
def jong_min_round_B(row):
    return float(row[170])/float(row[169])/float(row[82])

"""
종아리아래너비_A : 종아리아래너비/몸무게
종아리아래너비_B : 종아리아래너비/장딴지너비/몸무게
"""
def jong_below_width_A(row):
    return float(row[25])/float(row[82])

def jong_below_width_B(row):
    return float(row[25])/float(row[215])/float(row[82])


"""
종아리아래두께_A : 종아리아래두께/몸무게
종아리아래두께_B : 종아리아래두께/장딴지두께/몸무게
"""
def jong_below_thick_A(row):
    return float(row[198])/float(row[82])

def jong_below_thick_B(row):
    return float(row[198])/float(row[197])/float(row[82])



"""
가쪽복사높이_A : 가쪽복사높이/키
가쪽복사높이_B : 가쪽복사높이/장딴지높이/키
"""
def ga_copy_height_A(row):
    return float(row[19])/float(row[11])

def ga_copy_height_B(row):
    return float(row[19])/float(row[105])/float(row[11])

"""
다리가쪽길이_A : 다리가쪽길이/키
"""

def leg_ga_length_A(row):
    return float(row[223])/float(row[11])

"""
다리안쪽높이_A : 볼기고랑높이/키
"""
def leg_inner_height(row):
    return float(row[102])/float(row[11])

"""
위앞엉덩뼈가시높이_A : 위앞엉덩뼈가시높이/키
"""
def upfront_ass_bone_torn_height(row):
    return float(row[17])/float(row[11])

"""
엉덩이높이_A : 엉덩이높이/키
"""
def ass_height_A(row):
    return float(row[100])/float(row[11])

"""
엉덩이최대둘레높이_A : 엉덩이최대둘레높이/키
"""
def ass_max_round_height_A(row):
    return float(row[227])/float(row[11])


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
    new_columns = ["허리두께_A","허리두께_B","허리두께_C","배꼽수준허리두께_A","배꼽수준허리두께_B", "배높이_A ", "가는허리높이_A", "배꼽수준허리높이_A", "배꼽수준허리높이_B", "배꼽수준허리높이_C", "허리높이_A", "허리높이_B",
                "배너비_A", "배너비_B", "배두께_A", "배두께_B", "샅높이_A", "샅높이_B", "샅길이_A", "허리둘레_A",
                "허리둘레_B", "허리둘레_C", "허리둘레_D", "허리둘레_E", "허리둘레_F", "허리둘레_G", "허리둘레_H",
                "허리둘레_I", "허리둘레_J", "배꼽수준허리둘레_A", "배꼽수준허리둘레_B", "배꼽수준허리둘레_C",
                "엉덩이너비_A", "엉덩이너비_B", "엉덩이둘레_A", "엉덩이둘레_B", "배꼽수준샅앞뒤길이_A", "엉덩이두께_A", "엉덩이두께_B",
                "엉덩이수직길이_A", "엉덩이옆길이_A", "샅앞뒤길이_A", "넙다리중간둘레_A", "넙다리중간둘레_B", "넙다리둘레_A", "넙다리둘레_B", 
                "넙다리둘레_C", "넙다리둘레_D", "넙다리너비_A", "넙다리너비_B", "넙다리너비_C", "넙다리중간너비_A", "넙다리두께_A", "넙다리두께_B",
                "넙다리중간두께_A", "넙다리직선길이_A", "무릎둘레_A", "무릎둘레_B", "무릎너비_A", "무릎너비_B", "장딴지최대둘레_A", "장딴지최대둘레_B",
                "장딴지둘레_A", "장딴지둘레_B", "장딴지너비_A", "장딴지너비_B", "장딴지두께_A", "장딴지두께_B", "장딴지높이_A", "장딴지높이_B", "정강뼈위점높이_A",
                "무릎높이_A", "무릎높이_B", "발목둘레_A", "발목둘레_B", "발목최대둘레_A", "발목최대둘레_B", "발목너비_A", "발목너비_B", 
                "종아리최소둘레_A", "종아리최소둘레_B", "종아리아래너비_A", "종아리아래너비_B", "종아리아래두께_A", "종아리아래두께_B", "가쪽복사높이_A",
                "가쪽복사높이_B", "다리가쪽길이_A", "다리안쪽높이_A", "위앞엉덩뼈가시높이_A", "엉덩이높이_A", "엉덩이최대둘레높이_A"] 
    for new_column in new_columns:
        header.append(new_column)

    new_rows = []
    for row in rows:
        temp_row = row
        temp_row.append(waist_thick_A(temp_row))
        temp_row.append(waist_thick_B(temp_row))
        temp_row.append(waist_thick_C(temp_row))
        temp_row.append(navel_waist_thick_A(temp_row))
        temp_row.append(navel_waist_thick_B(temp_row))
        temp_row.append(stomach_height_A(temp_row))
        temp_row.append(thin_waist_A(temp_row))
        temp_row.append(navel_waist_A(temp_row))
        temp_row.append(navel_waist_B(temp_row))
        temp_row.append(navel_waist_C(temp_row))
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
        temp_row.append(ass_round_A(temp_row))
        temp_row.append(ass_round_B(temp_row))
        temp_row.append(navel_sat_A(temp_row))
        temp_row.append(ass_thick_A(temp_row))
        temp_row.append(ass_thick_B(temp_row))
        temp_row.append(ass_vertical_length_A(temp_row))
        temp_row.append(ass_side_length_A(temp_row))
        temp_row.append(sat_front_back_A(temp_row))  
        temp_row.append(nub_leg_middle_round_A(temp_row))
        temp_row.append(nub_leg_middle_round_B(temp_row))
        temp_row.append(nub_leg_round_A(temp_row))
        temp_row.append(nub_leg_round_B(temp_row))
        temp_row.append(nub_leg_round_C(temp_row))
        temp_row.append(nub_leg_round_D(temp_row))
        temp_row.append(nub_leg_width_A(temp_row))
        temp_row.append(nub_leg_width_B(temp_row))
        temp_row.append(nub_leg_width_C(temp_row))
        temp_row.append(nub_leg_middle_width_A(temp_row))
        temp_row.append(nub_leg_thick_A(temp_row))
        temp_row.append(nub_leg_thick_B(temp_row))
        temp_row.append(nub_middle_thick_A(temp_row))
        temp_row.append(nub_line_length_A(temp_row))
        temp_row.append(knee_round_A(temp_row))
        temp_row.append(knee_round_B(temp_row))
        temp_row.append(knee_width_A(temp_row))
        temp_row.append(knee_width_B(temp_row))
        temp_row.append(jang_max_round_A(temp_row))
        temp_row.append(jang_max_round_B(temp_row))
        temp_row.append(jang_round_A(temp_row))
        temp_row.append(jang_round_B(temp_row))
        temp_row.append(jang_width_A(temp_row))
        temp_row.append(jang_width_B(temp_row))
        temp_row.append(jang_thick_A(temp_row))
        temp_row.append(jang_thick_B(temp_row))
        temp_row.append(jang_height_A(temp_row))
        temp_row.append(jang_height_B(temp_row))
        temp_row.append(jung_bone_height_A(temp_row))
        temp_row.append(knee_height_A(temp_row))
        temp_row.append(knee_height_B(temp_row))
        temp_row.append(ankle_round_A(temp_row))
        temp_row.append(ankle_round_B(temp_row))
        temp_row.append(ankle_max_round_A(temp_row))
        temp_row.append(ankle_max_round_B(temp_row))
        temp_row.append(ankle_width_A(temp_row))
        temp_row.append(ankle_width_B(temp_row))
        temp_row.append(jong_min_round_A(temp_row))
        temp_row.append(jong_min_round_B(temp_row))
        temp_row.append(jong_below_width_A(temp_row))
        temp_row.append(jong_below_width_B(temp_row))
        temp_row.append(jong_below_thick_A(temp_row))
        temp_row.append(jong_below_thick_B(temp_row))
        temp_row.append(ga_copy_height_A(temp_row))
        temp_row.append(ga_copy_height_B(temp_row))
        temp_row.append(leg_ga_length_A(temp_row))
        temp_row.append(leg_inner_height(temp_row))
        temp_row.append(upfront_ass_bone_torn_height(temp_row))
        temp_row.append(ass_height_A(temp_row))
        temp_row.append(ass_max_round_height_A(temp_row))
        new_rows.append(temp_row)
        
    write_csv(header, new_rows, 'preprocessed_done.csv')
    


main()

