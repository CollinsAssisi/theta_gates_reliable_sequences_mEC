import sys
import math
import json
import multiprocessing as mp
import numpy as np

def genNsets_once(l_pars):
    #Read the parameters off the argument list l_pars
    i2i = l_pars[0]
    init_cond = l_pars[1]
    

    numEs = 1

   
    NUMES = str(numEs)
   
    
    INITCOND = str(init_cond)
    
    I2I = str(i2i)
    
    outfile = open("configure_files/nsets_Neuron_%si2i.isf"%I2I,"w")
    print("configure_files/nsets_Neuron_%si2i.isf"%I2I)

    np.random.seed(init_cond)
    #g_vs = n qp.random.random([numEs,8])
    #g_vs[:,0] = np.random.choice(np.arange(-80,-10,0.5))

    asympt = json.load(open("configure_files/asymptode_v_stellate_i2e-3.6.txt"))
    strToFile = ""
    
    for i in range(numEs):
        PMIN = -3.6
        TAURISE = str(np.random.choice(np.arange(100.0,300.0,1.0),1)[0])
        strToFile += "\"neuron %s\"dxdt:7,v:%s,m:%s,n:%s,h:%s,ms:%s,mhs:%s,mhf:%s,gh:1.5,I_syn:0.0,ampSin:0.0,ampNoise:0.008,freq:0.0,phase:0.0,V_th_Osc:-80,tau_fact:1.0,PulseDuration:10000,PulseStart:500,PulseEnd:9500,tau_rise:%s,tau_fall:20.0,PulseMax:%s,PulseMin:%s,I_PeriodicPulse:0.0,I_OscillatoryDrive:0.0, I_Na_Stellate_HR2005:0.0, I_K_Stellate_HR2005:0.0, I_Leak_Stellate_HR2005:0.0, I_NaP_Stellate_HR2005:0.0, I_Hs_Stellate_HR2005:0.0, I_Hf_Stellate_HR2005:0.0, ;\n\n"%(str(i),str(asympt["v"]),str(asympt["m"]),str(asympt["n"]),str(asympt["h"]),str(asympt["ms"]),str(asympt["mhs"]),str(asympt["mhf"]),TAURISE,I2I,PMIN)
    outfile.write(strToFile)
    outfile.close()

l_i2is = [-2.8,-2.75,-2.7,-2.65,-2.6]

cnt = 0

l_phases = [0]

for init_cond in [1]:
    for i2i in l_i2is:
        genNsets_once([i2i,init_cond])
        cnt += 1

print(cnt)
