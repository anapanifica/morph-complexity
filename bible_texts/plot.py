from matplotlib import pyplot as plt
from json import dumps

with open("agx-luke_cnt.txt", 'r') as f:
	ar1 = [float(x) for x in f.readline().strip().split()][:100000]

with open("ava-luke_cnt.txt", 'r') as f:
	ar2 = [float(x) for x in f.readline().strip().split()][:100000]

with open("dar-luke_cnt.txt", 'r') as f:
	ar3 = [float(x) for x in f.readline().strip().split()][:100000]

with open("eng-luke_cnt.txt", 'r') as f:
	ar4 = [float(x) for x in f.readline().strip().split()][:100000]

with open("rus-luke_cnt.txt", 'r') as f:
	ar5 = [float(x) for x in f.readline().strip().split()][:100000]

with open("tab-luke_cnt.txt", 'r') as f:
	ar6 = [float(x) for x in f.readline().strip().split()][:100000]



plt.plot(list(range(len(ar1))), ar1, label="agul (17 901 tokens)")
plt.plot(list(range(len(ar2))), ar2, label="avar (18 311 tokens)")
plt.plot(list(range(len(ar3))), ar3, label="dargwa (17 211 tokens)")
plt.plot(list(range(len(ar4))), ar4, label="eng (23 541 tokens)")
plt.plot(list(range(len(ar5))), ar5, label="rus (18 072 tokens)")
plt.plot(list(range(len(ar6))), ar6, label="tabasaran (17 766 tokens)")


plt.ylabel('Different types of tokens')
plt.xlabel('Total no. of tokens')

plt.legend()
plt.show()
