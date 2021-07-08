  #!/share/apps/anaconda3/bin/python
#by Q Zhu 2021/7/8
#to find maximal "F" and minimum "T"in VASP's POSCAR Selective Dynamics 
#Attention:only suitable for all "T" (T T T) and all "F" (F F F)
with open('POSCAR')as pos:
    lines = pos.readlines()
    poss = []   #total file,saved as list
    atoms = []  #to calculate total atoms
    coor = []   #to save atom coordinate
    total = 0   #total atoms
    F_max = 0 
    T_min = 1
    for i in lines:
      poss.append(i.rstrip())
    tem=poss[6]
    atoms=tem.split()
    for k in atoms:
       total = total + int(k)
    for j in poss[9:(9+total)]:
      coor=j.split()
      z=coor[2]
      z=float(z.rstrip())
      tf=coor[3]
      if tf=='T':
        if z < T_min:
    	  T_min = z
      if tf=='F':
        if z > F_max:
    	  F_max = z
    print'T_min is', T_min
    print'F_max is', F_max 
    	
