#!/share/apps/anaconda3/bin/python
#by QZhu 2021/7/15  to print unfixed atoms in POSCAR
with open('POSCAR')as pos:
    lines = pos.readlines()
    poss = []   #total file,saved as list
    atoms = []  #to calculate total atoms
    coor = []   #to save atoms coordinate
    T_list = []
    row_ele = []
    ele_symbol = []
    total = 0   #total atoms
    T_number = 0
    for i in lines:
      poss.append(i.rstrip())
    atoms=poss[6]
    atoms=atoms.split()
    ele_types_num = len(atoms)
    for k in atoms:
       total = total + int(k)
    ele_symbol = poss[5]
    ele_symbol = ele_symbol.split()
    for b in range(0,ele_types_num):
      a = 0
      while a < int(atoms[(b)]):
        row_ele.append([ele_symbol[b],a+1])
        a = a + 1
    if poss[7] == 'Direct':
      print ('the POSCAR is not Selective Dynamics type')
    else:
      x = 0
      for y in poss[9:(9+total)]:
        coor=y.split()
        z=coor[3]
        if z=='T':
          T_list.append([x+1,row_ele[x],])
        x = x + 1
    print('the number of unfixed atoms is',len(T_list))
    for i in T_list:
      print(i)
