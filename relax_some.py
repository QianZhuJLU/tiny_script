#!/share/apps/anaconda3/bin/python
# by Q Zhu 2021/7/16
# to relax a few atoms   eg:  python relax_some.py C 1 2 3 H 1 2 3 
# so that the No.1,2,3 of C  and No.1,2,3 of H are set to "T T T", this script is suitable for both "Selective dynamics" and "non-Selective dynamics"
import sys
import os 

inn=sys.argv[1:]
print(inn)
z1=[];z2=[];z3=[];z4=[];z5=[];z6=[]
fen = 0
for i in inn:
  if not i.isdigit():
    fen = fen + 1 
    locals()['z'+str(fen)].append(i)
  else:
    locals()['z'+str(fen)].append(i)

os.system("cp *.vasp POSCAR.bak")
with open('POSCAR.bak')as pos:
    lines = pos.readlines()
    poss = []   
    atoms = []  
    coor = [] 
    T_list = []
    ele_symbol = []
    total = 0 
    for i in lines:
      poss.append(i.rstrip())
    ele_symbol = poss[5].split()
    atoms=poss[6].split()
    ele_types_num = len(atoms)
    for i in atoms:
       total = total + int(i)
    if poss[7] == "Direct":
      cor_start_row = 9
    elif poss[8] == "Direct":
      cor_start_row = 10
    else:
      print('Error!not in fractional coordinates，please check')  
    plus=[0,]
    for i in atoms:
      plus.append(plus[-1]+int(i))
    print(plus)

for i in range(1,fen+1):  
  tem = locals()['z'+str(i)]          
  serial = ele_symbol.index(tem[0])   
  for ii in tem[1:]:
    T_list.append(int(ii)+plus[serial])          
print(T_list)    
if cor_start_row > 8 :
  with open('POSCAR','w') as newpos:
      for j in poss[0:7]:
        newpos.write(j+"\n")
      newpos.write("Selective dynamics\n")
      newpos.write("Direct\n")
      y = 1;bai = "     "
      for j in poss[cor_start_row-1:(cor_start_row-1+total)]:
        coor=j.split()
        if y in T_list: 
          newpos.write(bai+str(coor[0])+bai+str(coor[1])+bai+str(coor[2])+bai+" T  T  T\n")
        else:
          newpos.write(bai+str(coor[0])+bai+str(coor[1])+bai+str(coor[2])+bai+"F  F  F\n")
        y = y +1
