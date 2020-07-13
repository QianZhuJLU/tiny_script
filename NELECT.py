#!/share/apps/anaconda3/bin/python
# to output the number of valence electrons in system ,conveniently setting VASP parameter "NELECT" 
# written by JT YANG , Q ZHU
import re
import os
str1 = os.popen("grep ZVAL POTCAR|awk '{print int($6)}'")
str2 = os.popen("sed -n '7p' POSCAR")
a = re.split('\s',str1.read())
b = re.split('\s',str2.read())
a = [x for x in a if x!='']
b = [x for x in b if x!='']
print("electrons",a)
print("atoms",b)
k=j=0
for i in a:
   j=j+int(i)*int(b[k])
   k=k+1
print(j)
print('echo \"NELECT =',j,' >> INCAR')
