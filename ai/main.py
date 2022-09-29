import pandas as pd
from clustering import cluster

from clustering import cluster_prediction

data = pd.read_csv('preprocessed_done.csv')
data = data.dropna()

waist_side = ["허리두께_A","허리두께_B","허리두께_C","배꼽수준허리두께_A","배꼽수준허리두께_B"]
stomach_row = ["배너비_A", "배너비_B"]
stomach_side = ["배두께_A", "배두께_B"]
waist_stomach_length = ["가는허리높이_A", "배꼽수준허리높이_A", "배꼽수준허리높이_B", "배꼽수준허리높이_C", "배높이_A ", "허리높이_A", "허리높이_B", "샅높이_A", "샅높이_B", "샅길이_A"]
waist_stomach_side =  ["허리둘레_A", "허리둘레_B", "허리둘레_C", "허리둘레_D", "허리둘레_E", "허리둘레_F", "허리둘레_G", "허리둘레_H", "허리둘레_I", "허리둘레_J", "배꼽수준허리둘레_A", "배꼽수준허리둘레_B", "배꼽수준허리둘레_C"]
ass_row = ["엉덩이너비_A", "엉덩이너비_B", "엉덩이둘레_A", "엉덩이둘레_B"]
ass_side = ["배꼽수준샅앞뒤길이_A", "엉덩이두께_A", "엉덩이두께_B"]
ass_length = ["엉덩이수직길이_A", "엉덩이옆길이_A", "샅앞뒤길이_A"]
thigh_row = ["넙다리중간둘레_A", "넙다리중간둘레_B", "넙다리둘레_A", "넙다리둘레_B", "넙다리둘레_C", "넙다리둘레_D", "넙다리너비_A", "넙다리너비_B", "넙다리너비_C", "넙다리중간너비_A"]
thigh_side = ["넙다리두께_A", "넙다리두께_B", "넙다리중간두께_A"]
thigh_length = ["넙다리직선길이_A", "195. 넙다리직선길이 "] 
jong_row = ["무릎둘레_A", "무릎둘레_B", "무릎너비_A", "무릎너비_B", "장딴지최대둘레_A", "장딴지최대둘레_B",
                "장딴지둘레_A", "장딴지둘레_B", "장딴지너비_A", "장딴지너비_B"]
jong_side = ["장딴지두께_A", "장딴지두께_B"]
jong_length = ["장딴지높이_A", "장딴지높이_B", "정강뼈위점높이_A",
                "무릎높이_A", "무릎높이_B"]
ankle_row = ["발목둘레_A", "발목둘레_B", "발목최대둘레_A", "발목최대둘레_B", "발목너비_A", "발목너비_B", 
                "종아리최소둘레_A", "종아리최소둘레_B", "종아리아래너비_A", "종아리아래너비_B"] 
ankle_side = ["종아리아래두께_A", "종아리아래두께_B"]
ankle_length = ["가쪽복사높이_A", "가쪽복사높이_B"] 
all_length = ["다리가쪽길이_A", "다리안쪽높이_A", "위앞엉덩뼈가시높이_A", "엉덩이높이_A", "엉덩이최대둘레높이_A"] 
"""

"waist_side":waist_side,
    "stomach_row":stomach_row,
    "stomach_side":stomach_side,
    """
cluster_dict = {
    "waist_side":waist_side,
    "stomach_row":stomach_row,
    "stomach_side":stomach_side,
    "waist_stomach_length":waist_stomach_length,
"waist_stomach_side":waist_stomach_side,
"ass_row":ass_row,
"ass_side":ass_side,
"ass_length":ass_length,
"thigh_row":thigh_row,
"thigh_side":thigh_side,
"thigh_length":thigh_length,
"jong_row":jong_row,
"jong_side":jong_side,
"jong_length":jong_length,
"ankle_row":ankle_row,
"ankle_side":ankle_side,
"ankle_length":ankle_length,
"all_length":all_length
}


for key, value in cluster_dict.items():
    X = data[value]
    # print(key)
    cluster(X, key)
# y = data['472. 샅앞뒤길이 ']
# given_x = data[['432. 키 ', '503. 몸무게 ']]

# print(cluster_prediction(X, y, given_x, '엉덩이_길이_샅앞뒤길이'))
