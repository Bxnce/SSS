# -*- coding: utf-8 -*-
import redlab as rl
import numpy as np
import time
    
    
if __name__ == "__main__":
    tmp = []
    for i in range(1,31):
        tmp.append(np.sin(i/31*2*np.pi)+1)
    
    while(True):    
        for val in tmp:
            time.sleep(0.01)
            rl.cbVOut(0,0,101,val)
            