from os import name
import random
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics
counts = []
dice_result = []
for i in range(0,100):
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    dice_result.append(dice_1+dice_2)
    counts.append(i)
print(counts,dice_result)
print(statistics.mean(dice_result))
print(statistics.median(dice_result))
print(statistics.mode(dice_result))
print(statistics.stdev(dice_result))
mean = statistics.mean(dice_result)
stdev = statistics.stdev(dice_result)
# fig =px.bar(x=dice_result, y=counts)
# fig.show()
stdev_1_start, stdev_1_end = mean - stdev, mean + stdev
stdev_2_start, stdev_2_end = mean - (2*stdev), mean + (2*stdev)
stdev_3_start, stdev_3_end = mean - (3*stdev), mean + (3*stdev)

fig = ff.create_distplot([dice_result], ['Dice'], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.17], mode = 'lines', name='Mean'))
fig.add_trace(go.Scatter(x=[stdev_1_start, stdev_1_start], y=[0,0.17], mode='lines', name='stdev_1_start'))
fig.add_trace(go.Scatter(x=[stdev_1_end, stdev_1_end], y=[0,0.17], mode='lines', name='stdev_1_end'))
fig.add_trace(go.Scatter(x=[stdev_2_start, stdev_2_start], y=[0,0.17], mode='lines', name='stdev_2_start'))
fig.add_trace(go.Scatter(x=[stdev_2_end, stdev_2_end], y=[0,0.17], mode='lines', name='stdev_2_end'))
fig.add_trace(go.Scatter(x=[stdev_3_start, stdev_3_start], y=[0,0.17], mode='lines', name='stdev_3_start'))
fig.add_trace(go.Scatter(x=[stdev_3_end, stdev_3_end], y=[0,0.17], mode='lines', name='stdev_3_end'))
fig.show()

list_of_data_within_stdev_1_range = [result for result in dice_result if result > stdev_1_start and result < stdev_1_end]
list_of_data_within_stdev_2_range = [result for result in dice_result if result > stdev_2_start and result < stdev_2_end]
list_of_data_within_stdev_3_range = [result for result in dice_result if result > stdev_3_start and result < stdev_3_end]
print(len(list_of_data_within_stdev_1_range)*100.0/len(dice_result))
print(len(list_of_data_within_stdev_2_range)*100.0/len(dice_result))
print(len(list_of_data_within_stdev_3_range)*100.0/len(dice_result))