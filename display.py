import matplotlib.pyplot as plt
from search import get_col, get_value_by_col

def print_percent(title:str, target:int, total:int):
    print('{0} - {1} / {2} : {3:.2f}%'.format(title, target, total, target / total * 100))

def display_scatter(data:list):
    normals = get_value_by_col(data, '체형분류', 'Normal', False)
    normals_x = get_col(normals, '몸무게')
    normals_y = get_col(normals, '키')
    plt.scatter(normals_x, normals_y, c='#95a5a6', s=5**2)

    thicks = get_value_by_col(data, '체형분류', 'Thick waist', False)
    thicks_x = get_col(thicks, '몸무게')
    thicks_y = get_col(thicks, '키')
    plt.scatter(thicks_x, thicks_y, c='#2980b9', s=5**2)

    thins = get_value_by_col(data, '체형분류', 'Thin waist', False)
    thins_x = get_col(thins, '몸무게')
    thins_y = get_col(thins, '키')
    plt.scatter(thins_x, thins_y, c='#27ae60', s=5**2)
    plt.show()

def display_plot(data:list):
    normals = get_value_by_col(data, '체형분류', 'Normal', False)
    normals_x = get_col(normals, '몸무게')
    normals_y = get_col(normals, '키')
    plt.plot(normals_x, normals_y, color='#95a5a6')

    thicks = get_value_by_col(data, '체형분류', 'Thick waist', False)
    thicks_x = get_col(thicks, '몸무게')
    thicks_y = get_col(thicks, '키')
    plt.plot(thicks_x, thicks_y, color='#2980b9')

    thins = get_value_by_col(data, '체형분류', 'Thin waist', False)
    thins_x = get_col(thins, '몸무게')
    thins_y = get_col(thins, '키')
    plt.plot(thins_x, thins_y, color='#27ae60')
    plt.show()

