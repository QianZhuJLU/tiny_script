#!/share/apps/anaconda3/bin/python
#by QZhu 2020/7/18
#to fix coordinate which less than [0.09] in POSCAR(fractional coordinates)
import os
os.system("cp *.vasp POSCAR_bak")
with open('POSCAR_bak')as pos:
    lines = pos.readlines()
poss = []   #total file,saved as list
atoms = []  #to calculate total atoms
coor = []   #to save atom coordinate
total = 0   #total atoms
cor_start_row = 0
edge = 0.09 #fix-unfix edge
for i in lines:
    poss.append(i.rstrip())
if poss[7] == "Direct":
  cor_start_row = 9
elif poss[8] == "Direct":
  cor_start_row = 10
else:
  print('Error!not in fractional coordinates，please check')  
if cor_start_row > 8 :
  with open('POSCAR','w') as newpos:
      i=1
      for j in poss[0:7]:
          if i==7:
              atoms=j.split()
              for k in atoms:
                  total = total + int(k)
              newpos.write(j+"\nS\n")
              newpos.write("Direct\n")
          else:
              newpos.write(j+"\n")
          i=i+1
      for j in poss[cor_start_row-1:(cor_start_row-1+total)]:
          coor=j.split()
          z=coor[2]
          z=float(z.rstrip())
          if z > edge:
              newpos.write(j+" T T T \n")
          else:
              newpos.write(j+" F F F \n")
      print('fix line is',edge)
      print('done.')
