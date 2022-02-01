
#######################################################################
##
## Here is the script to write .com fie for a given cyclohexyl
##
#######################################################################

import sys
from rdkit import Chem
from rdkit.Chem import rdmolfiles
from rdkit.Chem import rdmolops
from rdkit.Chem import AllChem
from rdkit.Chem import TorsionFingerprints
from rdkit.Chem.Draw import IPythonConsole

def GetRingSystems(mol, includeSpiro=False):
  ri = mol.GetRingInfo()
  systems = []
  for ring in ri.AtomRings():
    ringAts = set(ring)
    nSystems = []
    for system in systems:
      nInCommon = len(ringAts.intersection(system))
      if nInCommon and (includeSpiro or nInCommon > 1):
        ringAts = ringAts.union(system)
      else:
        nSystems.append(system)
    nSystems.append(ringAts)
    systems = nSystems
  return systems

with open("/Users/wmm/Desktop/Test_list2.txt", "r") as f_list:
  inchi_list=f_list.readlines()
  #print(inchi_list)
  mol_order=0
  for inchi in inchi_list:
    inchi_str=inchi.strip("\n")
    #print(inchi_str)
    m=Chem.MolFromInchi(inchi_str)
    m=Chem.AddHs(m)
    AllChem.EmbedMolecule(m)
    #Chem.MolToMolFile(m,"compare_"+str(mol_order)+".mol")
    ring=GetRingSystems(m)
    num_of_ring=len(ring)
    ring_info=[]
    for item in ring:
      ring_info.append(list(item))
    torsion_list=TorsionFingerprints.CalculateTorsionLists(m)
    #Inchi=Chem.MolToInchi(m)
    #print("InChI:", Inchi)
    #print(torsion_list)
    print("ring_atoms:", ring)
    print("num_of_ring:", len(ring))
    print(ring_info)
    #mol_order+=1



    ###########################################################################################
    ##
    ## from here to write corresponding .com file for certian molecule
    ##
    ###########################################################################################

    with open("compare_"+str(mol_order)+".com","a+")  as f_com:
      f_com.write("compare_"+str(mol_order)+".mae")
      f_com.write("\n")
      f_com.write("compare_"+str(mol_order)+"-out.maegz")
      f_com.write("\n")
      f_com.write(" MMOD       0      1      0      0     0.0000     0.0000     0.0000     0.0000\n")
      f_com.write(" DEBG    1003      0      0      0     0.0000     0.0000     0.0000     0.0000\n")
      f_com.write(" FFLD       1      1      0      0     1.0000     0.0000     0.0000     0.0000\n")
      f_com.write(" BDCO       0      0      0      0    41.5692 99999.0000     0.0000     0.0000\n")
      f_com.write(" READ       0      0      0      0     0.0000     0.0000     0.0000     0.0000\n")
      f_com.write(" CRMS       0      0      0      0     0.0000     0.5000     0.0000     0.0000\n")
      f_com.write(" LMCS    4000      0      0      0     0.0000     0.0000     3.0000     6.0000\n")
      f_com.write(" NANT       0      0      0      0     0.0000     0.0000     0.0000     0.0000\n")
      f_com.write(" MCNV       1      5      0      0     0.0000     0.0000     0.0000     0.0000\n")
      f_com.write(" MCSS       2      0      0      0    21.0000     0.0000     0.0000     0.0000\n")
      f_com.write(" MCOP       1      0      0      0     0.5000     0.0000     0.0000     0.0000\n")
      f_com.write(" DEMX       0    833      0      0    21.0000    42.0000     0.0000     0.0000\n")


      ###########################################################################################
      ##
      ## this part to calculate carbon information
      ##
      ###########################################################################################

      with open("compare_"+str(0)+".mae", 'r') as f:
        mol_info=f.readlines()
        atom_info=[]
        for line in mol_info:
          #print(line)
          if line.find("C") > -1:
            #print(line)
            atom_info.append(int(line[2:4]))
        #print("ATTENTION!!!")
        #print(atom_info)

        atom_line=[]
        len_line=0
        line_need=len(atom_info)//4+1
        #print(line_need)
        line_atom=[]
        while len_line < line_need:
          line_atom.append(atom_info[len_line*4:len_line*4+4])
          #print(line_atom[len_line])
          if len_line==line_need-1:
            while len(line_atom[len_line]) < 4:
              line_atom[len_line].append(0)
          len_line+=1
        #print(line_atom)
        #print(type(line_atom))
        line_write=0
        while line_write < line_need:
          current_list=line_atom[line_write]
          atom_str=" COMP "
          for num in current_list:
             if num//10==0:
               atom_str=atom_str+"      "+str(num)
             else:
               atom_str=atom_str+"     "+str(num)
          atom_str=atom_str+"     0.0000     0.0000     0.0000     0.0000"
          #print("ATTENTION!!!!!!!!!!!")
          #print(atom_str)
          f_com.write(atom_str)
          f_com.write("\n")
          line_write+=1
        f_com.write(" MSYM       0      0      0      0     0.0000     0.0000     0.0000     0.0000\n")
        f_com.write(" AUOP       0      0      0      0   100.0000     0.0000     0.0000     0.0000\n")

        ###########################################################################################
        ##
        ## this part to calculate torsion angle atoms
        ## and ring information
        ##
        ###########################################################################################

        ## here to calculate the number of atom in ring torsion angle needed to be close
        i=0
        torsion_close_atom=[]
        while i < num_of_ring:
          if i==0:
            torsion_close_atom.append([ring_info[i][5]+1])
            torsion_close_atom[i].append(ring_info[i][0]+1)
            torsion_close_atom[i].append(ring_info[i][1]+1)
            torsion_close_atom[i].append(ring_info[i][2]+1)
          else:
            torsion_close_atom.append([ring_info[i][1]+1])
            torsion_close_atom[i].append(ring_info[i][0]+1)
            torsion_close_atom[i].append(ring_info[i][5]+1)
            torsion_close_atom[i].append(ring_info[i][4]+1)
          i+=1
        print("ATTENTION!!!!!")
        print(torsion_close_atom)
        
        ## here to calculate the atoms needed to be removed from torsion angle core atom pairs
        atom_pair_removed=[]
        for atom_pair in torsion_close_atom:
          atom_pair_removed.append(atom_pair[1:3])
        print(atom_pair_removed)


        #print(type(torsion_list[0][0]))
        ## here to calculate all the core atom pairs in torsion angle
        torsion_angle_pair=[]

        for torsion_info in torsion_list:
          tor_num=0
          while tor_num < len(torsion_info):
            tor_list=0
            while tor_list < len(torsion_info[tor_num][0]):
              torsion_angle_pair.append(sorted(torsion_info[tor_num][0][tor_list][:2]))
              torsion_angle_pair.append(sorted(torsion_info[tor_num][0][tor_list][1:3]))
              tor_list+=1
            tor_num+=1
        #print(torsion_angle_pair)

        torsion_angle_pair_final=[]
        current_list=[]
        for item in torsion_angle_pair:
          for ele in item:
            ele+=1
            current_list.append(ele)
          torsion_angle_pair_final.append(current_list)
          current_list=[]
        torsion_angle_pair_final.sort()

        torsion_atoms=[]
        for item in torsion_angle_pair_final:
          if (item not in torsion_atoms) and (item not in atom_pair_removed):
            torsion_atoms.append(item)
        print(torsion_atoms)

        ## write torsion information in .com file
        line_torsion=0
        while line_torsion < len(torsion_atoms):
          current_torsion_list=torsion_atoms[line_torsion]
          current_torsion=" TORS "
          for num in current_torsion_list:
             if num//10==0:
               current_torsion=current_torsion+"      "+str(num)
             else:
               current_torsion=current_torsion+"     "+str(num)
          current_torsion=current_torsion+"      0      0     0.0000   180.0000     0.0000     0.0000"
          f_com.write(current_torsion)
          f_com.write("\n")
          line_torsion+=1

        ## write ring_torson information in .com file
        line_ring_torsion=0
        while line_ring_torsion < len(torsion_close_atom):
          current_ring_torsion_list=torsion_close_atom[line_ring_torsion]
          current_ring_torsion=" RCA4 "
          for num in current_ring_torsion_list:
             if num//10==0:
               current_ring_torsion=current_ring_torsion+"      "+str(num)
             else:
               current_ring_torsion=current_ring_torsion+"     "+str(num)
          current_ring_torsion=current_ring_torsion+"     0.5000     2.5000     0.0000     0.0000"
          f_com.write(current_ring_torsion)
          f_com.write("\n")
          line_ring_torsion+=1

        f_com.write(" CONV       2      0      0      0     0.0500     0.0000     0.0000     0.0000\n")
        f_com.write(" MINI       1      0   2500      0     0.0000     0.0000     0.0000     0.0000\n")
      f_com.close()
    mol_order+=1
