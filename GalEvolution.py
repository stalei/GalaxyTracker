#  © Shahram Talei @ 2020 The University of Alabama - All rights reserved.
#you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation; either version 3 of the License, or
#(at your option) any later version.
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

import h5py as h5
import numpy as np
from matplotlib.legend_handler import HandlerLine2D
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import argparse
import math
#import csv
#How to use: $python GalEvolution.py galaxy_file start_snap end_sap
#example: python GalEvolution.py  AllGals.ascii 40 264
#This works for a single halo/galaxy

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("GalFile", type=str)
    parser.add_argument("Si", type=int)
    parser.add_argument("Sf", type=int)
    args = parser.parse_args()
    #f=h5.File("StellarHalo.h5","r")
    LowerMass=1.0e12
    UpperMass=1.3e12
    NBins=6
    # Galaxies from Sage, read raw data
    # 51.1813,49.1431,49.1961,2.87634e+08,0.000723028,36,0,0,0,0
    Gals=np.genfromtxt(args.GalFile, delimiter = ',')
    Gx0=np.array(Gals[:,0])
    Gy0=np.array(Gals[:,1])
    Gz0=np.array(Gals[:,2])
    GMv0=np.array(Gals[:,3])
    GRv0=np.array(Gals[:,4])
    GS0=np.array(Gals[:,5])
    GSM0=np.array(Gals[:,6])
    GIndex0=np.array(Gals[:,7])
    HIndex0=np.array(Gals[:,8])
    CentralG0=np.array(Gals[:,9])
    #GSM0=np.array(Gals[:,6])
    #let's say we have the target galaxy in all snapshots
    L=args.Sf-args.Si
    snap=[0.0]*L
    MStar=[0.0]*L
    x=[0.0]*L
    y=[0.0]*L
    z=[0.0]*L
    mv=[0.0]*L
    c=0
    id=0
    for i in range(args.Si,args.Sf):
        #snap[i]=i
        print(i)
        Gx=Gx0[GS0 == i]
        Gy=Gy0[GS0 == i]
        Gz=Gz0[GS0 == i]
        GMv=GMv0[GS0 == i]
        GRv=GRv0[GS0 == i]
        GSM=GSM0[GS0 == i]
        print(GSM)
        GS=GS0[GS0 == i]
        GIndex=GIndex0[GS0 == i]
        HIndex=HIndex0[GS0 == i]
        CentralG=CentralG0[GS0 == i]
        # now I have all galaxies for this snapshot
        #id=0 # This ID tracking is not accurate, it jumps back and forth between galaxies.
        if(i !=args.Si):
            dx=Gx-x_pre
            dy=Gy-y_pre
            dz=Gz-z_pre
            r=np.sqrt(dx*dx+dy*dy+dz*dz)
            index=np.argmin(r)
            id=GIndex[index]
        x[c]=Gx[GIndex ==id]
        y[c]=Gy[GIndex ==id]
        z[c]=Gz[GIndex ==id]
        MStar[c]=GSM[GIndex ==id]
        mv[c]=GMv[GIndex ==id]
        snap[c]=i#GS[GIndex ==id]
        x_pre=x[c]
        y_pre=y[c]
        z_pre=z[c]
        M_pre=MStar[c]
        mv_pre=mv[c]
        c+=1
    #now let's plot!
    print(np.array(MStar))
    fig = plt.figure(0)
    ax1 = fig.add_subplot(221)#, projection='3d')
    ax1.plot(snap,MStar,'k.', markersize=1)
    #ax1.plot(snap,mv,'r.', markersize=1)
    #fig.set_size_inches(14,8)
    ax1.set_xlabel('Snapshot')
    ax1.set_ylabel('Stellar Mass')
    ax2 = fig.add_subplot(222)#, projection='3d')
    ax2.plot(snap,x,'k.', markersize=1)
    #fig.set_size_inches(14,8)
    ax2.set_xlabel('Snapshot')
    ax2.set_ylabel('X')
    ax3 = fig.add_subplot(223)#, projection='3d')
    ax3.plot(snap,y,'k.', markersize=1)
    #fig.set_size_inches(14,8)
    ax3.set_xlabel('Snapshot')
    ax3.set_ylabel('Y')
    ax4 = fig.add_subplot(224)#, projection='3d')
    ax4.plot(snap,z,'k.', markersize=1)
    #fig.set_size_inches(14,8)
    ax4.set_xlabel('Snapshot')
    ax4.set_ylabel('Z')
    fig2=plt.figure(1)
    ax20=fig2.add_subplot(111)
    ax20.plot(snap,mv,'k.', markersize=1)
    ax20.set_xlabel('Snapshot')
    ax20.set_ylabel('Virial Mass')
    plt.show()
