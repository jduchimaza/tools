#program to turn XYZ format to gen format for DFTB+
#
# Takes the name of the xyz file as the first argument.
# 1 - open the xyz file
# 2 - iterate through and do several things
#   a - add index number (1 - N, N=number of atoms)
#   b - change atom ID to number and store in array (TypeNames)
# 3 - write to geometry.gen
#   a - first line: "N C"
#   b - second line: array of TypeNames
#   c - next lines: the (formatted) xyz coordinates

import sys

print 'Converting ' + str(sys.argv[1])

coords=[]
idx = 1
typenames=[]
typeidx=0

geo_in = str(sys.argv[1])

with open(geo_in,'r') as xyz:
   for line in xyz.readlines():
      if line.split()[0] not in typenames:
         typenames.append(line.split()[0])
         typeidx=len(typenames)
      else:
         typeidx=typenames.index(line.split()[0])+1
      line = str(idx)+"\t"+str(typeidx)+"   "+line.split()[1]+"   "+line.split()[2]+"   "+line.split()[3]+"\n"
      idx += 1
      coords.append(line)

typeline = ""
for type in typenames:
   typeline += type+" "

gen = open('geometry.gen','w')
gen.write(str(len(coords))+" C \n")
gen.write(typeline + "\n")
for coord in coords:
   gen.write(coord)

print typeline
print str(typenames)
print str(len(coords))
