import pandas as pd
from display import display_plot, display_scatter, print_percent

from search import *

output_list = []

df = pd.read_excel('data/8data.xlsx')
print('Successfully loaded data')

cols = df.values[5]
print('Successfully assign cols')
vals = df.values[6:]
print('Successfully assign values')


height = cols[12]    # 키
weight = cols[135]  # 몸무게
waist_round = cols[55]  # 허리 둘레
ass_round = cols[58]    # 엉덩이 둘레

for i, human in enumerate(vals):
    temp_dict = {}
    for j, col in enumerate(cols):
        temp_dict[col] = human[j]
    temp_ages = int(temp_dict['나이'] / 10)
    if(temp_dict['성별'] == '여' and 1< temp_ages < 4):
        body_type = ''
        drop = temp_dict[ass_round] - temp_dict[waist_round]
        if(140 < drop < 220):
            body_type = 'Normal'
        elif(220 <= drop <= 380):
            body_type = 'Thin waist'
            
        elif(drop <= 140):
            body_type = 'Thick waist'
           
        else:
            print('Error drop size : {}'.format(drop))
            body_type = 'Error drop size : {}'.format(drop)

        output_dict = {}
        output_dict['체형분류'] = body_type
        output_dict['나이대'] = '{}0대'.format(temp_ages)
        output_dict['키'] = temp_dict[height]
        output_dict['몸무게'] = temp_dict[weight]
        output_list.append(output_dict)

target_num_total = search_by_col(output_list, '체형분류', 'Normal', True )
total_ratio = target_num_total / len(output_list) * 100

target_num_20 = search_with_ages(output_list, '체형분류', 'Normal', True , '20대')
total_num_20 = search_by_col(output_list, '나이대', '20대', False)
ratio_20 = target_num_20 / total_num_20 * 100

target_num_30 = search_with_ages(output_list, '체형분류', 'Normal', True , '30대')
total_num_30 = search_by_col(output_list, '나이대', '30대', False)
ratio_30 = target_num_30 / total_num_30 * 100

print_percent('전체 타겟층 비율', target_num_total, len(output_list))
print_percent('20대 타겟층 비율', target_num_20, total_num_20)
print_percent('30대 타겟층 비율', target_num_30, total_num_30)

display_scatter(output_list)
display_plot(output_list)
