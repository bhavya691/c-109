import plotly.figure_factory as ff
import pandas as pd
import csv
import statistics
df = pd.read_csv('data.csv')
height_list = df["Height(Inches)"].tolist()
mean = statistics.mean(height_list)
stdev = statistics.stdev(height_list)
print(mean)
print(stdev)
stdev_1_start, stdev_1_end = mean-stdev, mean+stdev
stdev_2_start, stdev_2_end = mean - (2*stdev), mean + (2*stdev)
stdev_3_start, stdev_3_end = mean - (3*stdev), mean+(3*stdev)

list_of_stdev_1 = [result for result in height_list if result > stdev_1_start and result < stdev_1_end]
list_of_stdev_2 = [result for result in height_list if result > stdev_2_start and result < stdev_2_end]
list_of_stdev_3 = [result for result in height_list if result > stdev_3_start and result < stdev_3_end]

print("{} % of data within stdev 1".format(len(list_of_stdev_1)*100.0/len(height_list)))
print(len(list_of_stdev_2)*100.0/len(height_list))
print(len(list_of_stdev_3)*100.0/len(height_list))

fig = ff.create_distplot([df["Height(Inches)"].tolist()], ["Height"], show_hist=False)
fig.show()