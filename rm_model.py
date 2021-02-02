# -- coding:UTF-8
 
import os 
import sys 
import pdb 
import shutil

s1=0
e1=19
for i in range(s1,e1):
    mydir='/home/d1/chenlei/self_rec/yelpModel/yelp/selfonlypairs'+str(i)
    try:
        shutil.rmtree(mydir)
    except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror))

exit()

# dataset_base_path='/home/d1/chenlei/fairness/fm0addModel/lastfm/filter_lineargcnadd12_ba6'#'../data/amazon-book'  
dataset_base_path='/home/d1/chenlei/self_rec/mv20m2Model/ml20m/selfp2n10s0'
save_epoch=60

s1=0
e1=save_epoch-15
s2=save_epoch+15
e2=400
for i in range(s1,e1):
    print(i) 
    path=dataset_base_path+'/epoch'+str(i)+'user_e.npy' 
    if os.path.exists(path):
        os.remove(path)
    else:
        print("The file does not exist") 
    path=dataset_base_path+'/epoch'+str(i)+'item_e.npy' 
    if os.path.exists(path):
        os.remove(path) 
    path=dataset_base_path+'/epoch'+str(i)+'.pt' 
    if os.path.exists(path):
        os.remove(path)
        
for i in range(s2,e2):
    print(i) 
    path=dataset_base_path+'/epoch'+str(i)+'user_e.npy' 
    if os.path.exists(path):
        os.remove(path)
    else:
        print("The file does not exist") 
    path=dataset_base_path+'/epoch'+str(i)+'item_e.npy' 
    if os.path.exists(path):
        os.remove(path) 
    path=dataset_base_path+'/epoch'+str(i)+'.pt' 
    if os.path.exists(path):
        os.remove(path)
exit()     

base_path='/home/d1/chenlei/self_rec/data/ml-20m/traing_sample_neg100_noly'
count=0
for i in range(400):
    source_path=base_path+'/'+str(i)+'.npy'
    if os.path.exists(source_path):
        if i==count:
            print(i,'have')
            continue
        else:
            target_path=base_path+'/'+str(count)+'.npy'
            os.rename(source_path,target_path)
            count+=1

exit()
