#!/share/apps/anaconda3/bin/python
#by QZhu 2020/7/18
#to fix coordinate which greater than [0.32] in POSCAR(fractional coordinates)
import os
os.system("mv POSCAR POSCAR-backup")
with open('POSCAR-backup')as pos:
    lines = pos.readlines()
poss = []   #total file,saved as list
atoms = []  #to calculate total atoms
coor = []   #to save atom coordinate
total = 0   #total atoms
edge = 0.32 #fix-unfix edge
for i in lines:
    poss.append(i.rstrip())
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
    for j in poss[8:(8+total)]:
        coor=j.split()
        z=coor[2]
        z=float(z.rstrip())
        if z > edge:
            newpos.write(j+" T T T \n")
        else:
            newpos.write(j+" F F F \n")
