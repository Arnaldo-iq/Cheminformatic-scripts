#!/usr/bin/env python3


x1 = [ ]
y1 = [ ]
z1 = [ ] 

with open('mol1.xyz', 'r') as mol1:
	for line in mol1:
		xyz_data = []
		xyz_data = line.split()
		xa = float(xyz_data[0])
		ya = float(xyz_data[1])
		za = float(xyz_data[2])
		x1.append(xa)
		y1.append(ya)
		z1.append(za)

x2 = [ ]
y2 = [ ]
z2 = [ ]

with open('mol2.xyz', 'r') as mol2:
        for line in mol2:
                xyz_data = []
                xyz_data = line.split()
                xb = float(xyz_data[0])
                yb = float(xyz_data[1])
                zb = float(xyz_data[2])
                x2.append(xb)
                y2.append(yb)
                z2.append(zb)


def rms_func(X1, Y1, Z1, X2, Y2, Z2):
	rmsd = []
	l=len(X1)
	for i in range(l):
		x1atom =  X1[i]
		y1atom =  Y1[i]
		z1atom =  Z1[i]
		x2atom =  X2[i]
		y2atom =  Y2[i]
		z2atom =  Z2[i]
		rmsd_atoms = (((x1atom-x2atom)**2)+((y1atom-y2atom)**2)+ ((z1atom-z2atom)**2))
		rmsd.append(rmsd_atoms)
	rmsd =  ((sum(rmsd))/l)**0.5
	return rmsd 

result = rms_func(x1,y1,z1,x2,y2,z2)
print(result)
