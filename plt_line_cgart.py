import matplotlib.pyplot as plt
import numpy as np
import pdb

#
plt.figure(figsize=(12,8))#画布大小
plt.rc('font', size=40)   

x =  [0.1,0.2,0.3,0.4,0.5,0.6,0.7]#点的横坐标
hr_bpr = [0.1964,0.196,0.1965,0.1965,0.1967,0.1956,0.1899]
ndcg_bpr = [0.1574,0.1569,0.1577,0.1570,0.1573,0.1572,0.155]
dp_bpr = [0.58206,0.564962,0.553503,0.539183,0.540963,0.559931,0.609777]
eo_bpr = [0.606328,0.587001,0.582522,0.565552,0.567583,0.577673,0.612036]
ndcg_b = [0.1602,0.1602,0.1602,0.1602,0.1602,0.1602,0.1602]
eo_b = [0.644967,0.644967,0.644967,0.644967,0.644967,0.644967,0.644967]


fig = plt.figure(figsize=(13,10))

ax=fig.gca();#获得坐标轴的句柄
ax.spines['bottom'].set_linewidth(10);###设置底部坐标轴的粗细
ax.spines['left'].set_linewidth(10);####设置左边坐标轴的粗细
ax.spines['right'].set_linewidth(10);###设置右边坐标轴的粗细
ax.spines['top'].set_linewidth(10);####设置上部坐标轴的粗细

ax1 = fig.add_subplot(111) 
ax1.plot(x, ndcg_bpr,'o-',color = 'r',markersize=15,linewidth=7,label = "NDCG ")
# ax1.plot(x, ndcg_bpr,'s-',color = 'r',markersize=15,linewidth=10, label = "NDCG of FairData")
# ax1.plot(x, ndcg_b,'o-',color = 'r',linestyle='--',markersize=15,linewidth=10,label = "NDCG of GCN")
ax1.set_ylim((0.12, 0.17))
ax1.set_ylabel('NDCG@20')
ax1.yaxis.label.set_color('r')
ax1.tick_params(axis='y', colors='r')  
# ax1.set_title("Double Y axis")

ax2 = ax1.twinx()  # this is the important function
# ax2.plot(x, eo_bpr, 'o--', markerfacecolor='none', color = 'black',markersize=15,linewidth=7,label = "EO")
ax2.plot(x, eo_bpr, 's-', color = 'g',markersize=15,linewidth=7,label = "EO")
# ax2.plot(x, eo_bpr, 's-',color = 'g',markersize=15,linewidth=10,label = "EO of FairData")
# ax2.plot(x, eo_b, 'o-',color = 'g',linestyle='--',markersize=15,linewidth=10,label = "EO of GCN")
ax2.set_ylim((0.54, 0.65))
ax2.set_ylabel('EO@20')
ax2.set_xlabel('ratio')
ax2.yaxis.label.set_color('g')
ax2.tick_params(axis='y', colors='g')  

# fig.legend(loc=1)
# fig.legend(loc=1, bbox_to_anchor=(0.43,0.3), bbox_transform=ax.transAxes)
fig.legend(loc=1,prop={'size': 50}, bbox_to_anchor=(0.51,0.36), bbox_transform=ax.transAxes)

plt.show()
fig.savefig('./ratio_bpr3.png')
exit()


plt.figure(figsize=(13,10))#画布大小
plt.rc('font', size=40)

x =  [0.1,0.2,0.3,0.4,0.5,0.6,0.7]#点的横坐标
hr_gcn = [0.1964,0.1969,0.197,0.1976,0.196,0.196,0.1803]
ndcg_gcn = [0.1566,0.1574,0.1578,0.158,0.1569,0.1556,0.142]
dp_gcn = [0.576571,0.56892,0.552657,0.544962,0.537646,0.551252,0.562047]
eo_gcn = [0.602537,0.59131,0.575452,0.56933,0.566287,0.572573,0.575233]
ndcg_g = [0.164,0.164,0.164,0.164,0.164,0.164,0.164]
eo_g = [0.647661,0.647661,0.647661,0.647661,0.647661,0.647661,0.647661]

hr_bpr = [0.1964,0.196,0.1965,0.1965,0.1967,0.1956,0.1899]
ndcg_bpr = [0.1574,0.1569,0.1577,0.1573,0.1578,0.1572,0.155]
dp_bpr = [0.58206,0.564962,0.553503,0.539183,0.540963,0.559931,0.609777]
eo_bpr = [0.606328,0.587001,0.582522,0.565552,0.567583,0.577673,0.612036]
ndcg_b = [0.1602,0.1602,0.1602,0.1602,0.1602,0.1602,0.1602]
eo_b = [0.644967,0.644967,0.644967,0.644967,0.644967,0.644967,0.644967]


fig = plt.figure(figsize=(13,10))

ax=fig.gca();#获得坐标轴的句柄
ax.spines['bottom'].set_linewidth(10);###设置底部坐标轴的粗细
ax.spines['left'].set_linewidth(10);####设置左边坐标轴的粗细
ax.spines['right'].set_linewidth(10);###设置右边坐标轴的粗细
ax.spines['top'].set_linewidth(10);####设置上部坐标轴的粗细

ax1 = fig.add_subplot(111)
ax1.plot(x, ndcg_gcn,'o-',color = 'r',markersize=15,linewidth=7,label = "NDCG ")
# ax1.plot(x, ndcg_gcn,'s-',color = 'r',markersize=15,linewidth=10,label = "NDCG of FairData")
# ax1.plot(x, ndcg_g,'o-',color = 'r',markersize=15,linewidth=10,linestyle='--',label = "NDCG of GCN")
ax1.set_ylim((0.12, 0.17))
ax1.set_ylabel('NDCG@20')
ax1.yaxis.label.set_color('r')
ax1.tick_params(axis='y', colors='r')  
# ax1.set_title("Double Y axis")

ax2 = ax1.twinx()  # this is the important function
ax2.plot(x, eo_gcn, 's-', color = 'g',markersize=15,linewidth=7,label = "EO")
# ax2.plot(x, eo_gcn, 'o-', markerfacecolor='none',color = 'g',markersize=15,linewidth=7,label = "EO")
# ax2.plot(x, eo_gcn, 's-',color = 'g',markersize=15,linewidth=10,label = "EO of FairData")
# ax2.plot(x, eo_g, 'o-',color = 'g',linestyle='--',markersize=15,linewidth=10,label = "EO of GCN")
ax2.set_ylim((0.54, 0.65))
ax2.set_ylabel('EO@20')
ax2.set_xlabel('ratio')
ax2.yaxis.label.set_color('g')
ax2.tick_params(axis='y', colors='g')  
# fig.legend(loc=1)
# fig.legend(loc=1, bbox_to_anchor=(0.42,0.29), bbox_transform=ax.transAxes)
fig.legend(loc=1,prop={'size': 50}, bbox_to_anchor=(0.52,0.36), bbox_transform=ax.transAxes)

# 0.43,0.3
plt.show()
fig.savefig('./ratio_gcn3.png')
exit()














# plt.plot(x,hr_bpr,'s-',color = 'r',label="HR")#s-:方形
# plt.plot(x,ndcg_bpr,'s-',color = 'y',label="NDCG")#o-:圆形

plt.plot(x,dp_bpr,'o-',lw=2,color = 'b',label="DP")#s-:方形
plt.plot(x,eo_bpr,'o-',lw=2,color = 'g',label="EO")#o-:圆形

# plt.plot(x,hr,'s-',color = 'r',label="HR")#s-:方形
# plt.plot(x,ndcg,'s-',color = 'y',label="NDCG")#o-:圆形

# plt.plot(x,dp,'o-',lw=2,color = 'b',label="DP")#s-:方形
# plt.plot(x,eo,'o-',lw=2,color = 'g',label="EO")#o-:圆形

plt.xlabel("ratio")#横坐标名字
plt.ylabel("fairness")#纵坐标名字
# plt.ylabel("accuracy")#纵坐标名字
plt.legend(loc = "best")#, borderpad=2), fontsize=20#图例
plt.show()