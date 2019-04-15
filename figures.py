import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

SortAndSearch_Means  = np.asarray( [ 0.000002, 0.000002, 0.000002, 0.000002, 0.000003, 0.000004, 0.000006, 0.000010, 0.000019, 0.000036, 0.000075, 0.000163, 0.000343, 0.000755, 0.001597, 0.003263, 0.006755, 0.014400, 0.028883, 0.058093, 0.115283, 0.230631 ] )
PruneAndSearch_Means = np.asarray( [ 0.000005, 0.000008, 0.000022, 0.000046, 0.000085, 0.000171, 0.000363, 0.000670, 0.001276, 0.002470, 0.004891, 0.009697, 0.019643, 0.039769, 0.075800, 0.154484 ] )

SortAndSearch_Small_Means = np.asarray( [ 0.449646, 0.892595, 1.789482, 3.554875, 7.064915 ] )


num_display    = 8
num_sim_sets   = 27
x_sim_labels   = [ idx for idx in range(1, num_sim_sets+1) ]
x_Descriptions = [ "2^{}".format(idx) if (idx % (num_sim_sets//num_display)) == 0 else "" for idx in range(1, num_sim_sets+1) ]
  

num_real_sets_sort = len(SortAndSearch_Means)
x_real_sort_labels = [ idx for idx in range(1, num_real_sets_sort+1) ]

num_real_small_sets = len(SortAndSearch_Small_Means)
x_real_small_labels = [ idx for idx in range(num_real_sets_sort+1, num_real_sets_sort+num_real_small_sets+1)]

print(x_real_sort_labels, x_real_small_labels)

num_real_sets_prune = len(PruneAndSearch_Means)
x_real_prune_labels = [ idx for idx in range(1, num_real_sets_prune+1) ]


slope, intercept, r_value, p_value, std_err = linregress(x_real_prune_labels, np.log2(PruneAndSearch_Means))
Prune_Regression = []
Prune_Labels     = []
for idx in range(1, num_sim_sets+1):
    Prune_Labels.append(idx)
    Prune_Regression.append( slope*idx + intercept )


fSize = 14

plt.figure()
plt.title('Time Complexity Comparison of Sort and Search and\nPrune and Search', fontsize=fSize)
plt.xlabel('Number of Elements Per Trial', fontsize=fSize)
plt.ylabel('Log2 of the Mean over 10000 Trials', fontsize=fSize)
plt.plot(  x_real_sort_labels, np.log2(       SortAndSearch_Means ), '--o', color='b', label='Sort And Search')
plt.plot( x_real_small_labels, np.log2( SortAndSearch_Small_Means ), '--*', color='b', label='Sort And Search*')
plt.plot( x_real_prune_labels, np.log2(      PruneAndSearch_Means ), '--o', color='r', label='Prune And Search')
plt.plot(        Prune_Labels,                   Prune_Regression  , '--' , color='g', label='Extrapolation')
plt.xticks(x_sim_labels, x_Descriptions)
plt.legend(prop={'size': fSize})



x1 = []
x2 = []
for idx in range(2000):
    x1.append(idx * np.log2(idx))
    x2.append(idx*10)

plt.figure()
plt.plot(x1)
plt.plot(x2)








plt.show()

