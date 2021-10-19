
import os

## define the path of where mol files to be calculated are and where to store gaussian input files
mol_dir="/users/wmm/Desktop/rdkit"
script_dir="/users/wmm/Desktop/rdkit_DFT/"


files=os.listdir(mol_dir)
n=0
for file in files:
  name=files[n]
  if name.split(".")[1]=='sdf':
      ## open the mol file to be cal, get its coordinates and bond information
      with open(file) as mol_f:
          info=mol_f.readlines()
          print(info)
          atom_num=info[3][2]
          #print(atom_num)
          ## read the atoms coordinates and element from sdf file
          element=[]
          coordinates=[]
          molinfo_line=4
          molinfo_totalline=4+int(atom_num)-1
          while molinfo_line <= molinfo_totalline:
              current_element=info[molinfo_line][31]
              #print(current_element)
              element.append(current_element)
              current_coordinates=info[molinfo_line][0:30]
              #print(current_coordinates)
              coordinates.append(current_coordinates)
              molinfo_line+=1
          #print(element)
          #print(coordinates)
          ## read bond information from sdf file
          bond_info=[]
          bond_line=molinfo_totalline+1
          for line in info:
              if line.find("M  END") > -1:
                  endline=info.index(line)
                  #print(endline)
          while bond_line < endline:
              #print(info[bond_line][0:10])
              bond_info.append(info[bond_line][0:10])
              bond_line+=1
          #print(bond_info)
      order=name.split("out")[0]
      print(order)
      ## with molecule's coordinates, element and bond informaiton, now can utilize them to generate
      ## a gaussian single point energy calculation input file
      with open(script_dir+order+".gjf", "a+") as f:
          ## write the informaiton of the gaussian calcualtion type and theory chosen
          f.write("%chk="+str(order)+"out.chk")
          f.write("\n")
          f.write("#p b3lyp/6-311+g(2d,p) geom=connectivity")
          f.write("\n")
          f.write("\n")
          f.write("Title Card Required")
          f.write("\n")
          f.write("\n")
          f.write("0 1")
          f.write("\n")
          ## now start to write molecule element and coordinates information
          ele_num=0
          while ele_num < int(atom_num):
              f.write(" "+element[ele_num]+"                 "+coordinates[ele_num][3:10]+"0000   "+coordinates[ele_num][13:20]+"0000   "+coordinates[ele_num][23:30]+"0000   ")
              f.write("\n")
              ele_num+=1
          f.write("\n")
          ## not to write bond information
          bond_num=0
          while bond_num < len(bond_info):
              f.write(" "+bond_info[bond_num][2]+" "+bond_info[bond_num][5]+" "+bond_info[bond_num][8]+".0")
              f.write("\n")
              bond_num+=1
          f.write(" "+atom_num)
      f.close()
  n+=1