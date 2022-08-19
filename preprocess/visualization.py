import csv
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] ='D2Coding'

matplotlib.rcParams['axes.unicode_minus'] =False

csv_file = open("data_extracted.csv", "r", newline="" )

f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

header = next(f)
rows = []

for row in f:
    rows.append(row)

# 기준이 될 키와 몸무게의 index
height_index = 11 # 예를 들어 rows[0][height_index]를 하면 그 사람의 키를 가르킨다.
weight_index = 134

height_values = []
weight_values = []

for row in rows:
    height_values.append(float(row[height_index]))
    weight_values.append(float(row[weight_index]))

for i in range(10, len(header)):
    x_label = header[i]
    height_label = header[height_index]
    weight_label = header[weight_index]

    x_values = []


    for row in rows:
        if i == height_index or i == weight_index:
            break
        else:
            x_values.append(float(row[i]))
    
    try:
        plt.subplot(2, 1, 1)
        plt.plot(x_values, height_values, 'go', markersize=2)
        plt.title('{} 와 {}의 관계'.format(str(header[i]),height_label))
        plt.xlabel(str(header[i]))
        plt.ylabel(height_label)

        plt.subplot(2, 1, 2)
        plt.plot(x_values, weight_values, 'go', markersize=2)
        plt.title('{} 와 {}의 관계'.format(str(header[i]),weight_label))
        plt.xlabel(str(header[i]))
        plt.ylabel(weight_label)


        plt.subplots_adjust(left=0.125, bottom=0.1,  right=0.9, top=0.9, wspace=0.2, hspace=0.5)

        plt.savefig(f'{str(header[i])}.png')
        print('{} / {}'.format(i, len(header)))
    except ValueError:
        pass

