import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(6.8,5))#画布大小
plt.rc('font', size=16)   
ax=plt.gca();#获得坐标轴的句柄
ax.spines['bottom'].set_linewidth(3);###设置底部坐标轴的粗细
ax.spines['left'].set_linewidth(3);####设置左边坐标轴的粗细
ax.spines['right'].set_linewidth(3);###设置右边坐标轴的粗细
ax.spines['top'].set_linewidth(3);####设置上部坐标轴的粗细


# # 这两行代码解决 plt 中文显示的问题
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False

# 输入统计数据
waters = ('Call-LastFM', 'Ctest-LastFM', 'Call-MoviesLens', 'Ctest-MoviesLens')
buy_number_male = [0.3474, 0.4301, 0.3209, 0.4163]
buy_number_female = [0.2529, 0.3248, 0.2559, 0.3855]

buy_number_gcn = [0.3434, 0.4307, 0.3225, 0.4230]
buy_number_fairdata = [0.2525, 0.3147, 0.2542, 0.3694]

bar_width = 0.3  # 条形宽度
index_male = np.arange(len(waters))  # 男生条形图的横坐标
index_female = index_male + bar_width  # 女生条形图的横坐标

# 使用两次 bar 函数画出两组条形图
plt.bar(index_male, height=buy_number_male, width=bar_width, color='b', label='BPR')
plt.bar(index_female, height=buy_number_female, width=bar_width, color='darkorange', label='FairData')
# plt.bar(index_male, height=buy_number_gcn, width=bar_width, color='b', label='GCN')
# plt.bar(index_female, height=buy_number_fairdata, width=bar_width, color='darkorange', label='FairData')



plt.legend()  # 显示图例
plt.xticks(index_male + bar_width/2, waters)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
plt.ylabel('value')  # 纵坐标轴标题
# plt.title('Call result')  # 图形标题

plt.show()