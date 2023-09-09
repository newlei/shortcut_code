import os
import torch
import pdb
import time
import math
def get_gpu_memory():
    os.system('nvidia-smi -q -d Memory | grep -A80 GPU | grep Free > tmp.txt')
    memory_gpu = [int(x.split()[2]) for x in open('tmp.txt','r').readlines()]
    os.system('rm tmp.txt')
    return memory_gpu

count_gpu =0
while(1):
    gpu_memory = get_gpu_memory()
    gpu_free =[0]*8
    for i in range(8):
        j = i*3+1
        gpu_free[i] =gpu_memory[i*3]#+gpu_memory[j]
    # try:
    #     count0 = math.floor(gpu_free[0]/574)
    #     x1=torch.ones([count0*1000, count0*1000], dtype=torch.float64).cuda(0)#574M
    #     x2= x1*torch.randn(count0*1000, count0*1000).cuda(0)
    # except:
    #     print('gpu 0 is error')
    
    # try :
    #     count0 = math.floor(gpu_free[3]/574)
    #     x3=torch.ones([count0*1000, count0*1000], dtype=torch.float64).cuda(3)#574M
    #     x4= x3*torch.randn(count0*1000, count0*1000).cuda(3)
    # except:
    #     print('gpu 3 is error')

    try:
        count0 = math.floor(gpu_free[5]/574)
        x5=torch.ones([count0*1000, count0*1000], dtype=torch.float64).cuda(5)#574M
        x6= x5*torch.randn(count0*1000, count0*1000).cuda(5)
    except:
        print('gpu 5 is error')

    print(count_gpu,'end')
    count_gpu+=1
    time.sleep(60)




#  memoryo pu list = np.argsort(gpu memory)f-1]pu list str ='.join(map(str, gpu list))
# s.environ.setdefault(“"CUDA_ VISIBLE DEVICES", gpu_list_str)
# brint("ngpu free memory: {" format(gpu_memory))
# orint("CUDA_VISIBLE_DEVICES :{".format(os.environ["CUDA_ VISIBLE_DEVICES"])