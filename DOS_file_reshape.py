import numpy as np
import os
filelist = os.listdir('.')
for i in filelist: 
 t1 = np.loadtxt(i)
 t2 = np.split(t1,8,0)  # 8 is the numbers of pdos, if change it, the folling code will be changed, too.
 t3 = np.hstack((t2[0],t2[1],t2[2],t2[3],t2[4],t2[5],t2[6],t2[7]))
 np.savetxt(i+'.csv',t3,delimiter = ',')
