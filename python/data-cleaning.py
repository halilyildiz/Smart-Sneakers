# Kullanılan Kütüphaneler
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os

#%% Dosya gezici
for dirname, _, filenames in os.walk('C:\\Users\\halil\\Desktop\\Tez\\smart-sneakers\\data\\datas'):
    for filename in filenames:
        print("")
                
#%% Aktiviteye göre dataframelerin oluşturulması
part = np.zeros((4,4))
count = np.zeros((4,4))
length =np.zeros((4,4))

#%% Değişkenler
nameOfActivity = ["downstairs","upstairs","walk","run"]
numberOfStep = [1,3,5,11]

#%% 
# Bir aktivitedeki aynı adım sayısına sahip verilerin seri uzunluklarının ortalaması
for activity in range(0, len(nameOfActivity)):
    for step in range(0,len(numberOfStep)):
        for i in range(1,11):  
            name = "{}{}step-{}.csv".format(nameOfActivity[activity],numberOfStep[step],i)
            for filename in filenames:   
                if(name == filename):
                    new_data= pd.read_csv("C:\\Users\\halil\\Desktop\\Tez\\smart-sneakers\\data\\datas\\{}".format(name))
                    
                    count[activity,step] += 1
                    part[activity,step] += len(new_data)
                    
        length[activity,step] = part[activity,step] / count[activity,step]
        
#%%
dataLength = pd.DataFrame(length,index = nameOfActivity,columns = numberOfStep )


#dataLength.to_csv("C:\\Users\\halil\\Desktop\\Tez\\smart-sneakers\\data\\data-length.csv",encoding = 'utf-8')                 

#%% 
## Bir aktivitedeki aynı adım sayısına sahip verilerin seri uzunluklarının eşitlenmesi
new_data = pd.DataFrame(np.zeros((2,2)))
for activity in range(0, len(nameOfActivity)):
    for step in range(0,len(numberOfStep)):
        for i in range(1,11):  
            name = "{}{}step-{}.csv".format(nameOfActivity[activity],numberOfStep[step],i)
            for filename in filenames:   
                if(name == filename):
                    new_data= pd.read_csv("C:\\Users\\halil\\Desktop\\Tez\\smart-sneakers\\data\\datas\\{}".format(name))
                    if(dataLength.iloc[activity,step] > len(new_data)):
                        fark = dataLength.iloc[activity,step] - len(new_data)  
                        a = np.zeros((int(fark)+1,7))
                        array = np.array([0,new_data.ax.mean(),new_data.ay.mean(),new_data.az.mean(),
                        new_data.gx.mean(),new_data.gy.mean(),new_data.gz.mean()])
                        for i in range(0,int(fark)+1):
                            a[i,:] = array
                        ar = pd.DataFrame(a,columns=["time","ax","ay","az","gx","gy","gz"])
                        data2 = pd.concat([new_data,ar],axis=0,ignore_index=True)    
                    else:
                        data2 = new_data.iloc[:int(dataLength.iloc[activity,step])+1,:]
                    
                    data2.to_csv("C:\\Users\\halil\\Desktop\\Tez\\smart-sneakers\\data\\cleaning-datas\\resize-data\\{}".format(name),
                    encoding='utf-8')
 
#%% Verilerin ortlamasını bir satır haline getirme. 
new_data4 = pd.DataFrame()
for activity in range(0, len(nameOfActivity)):
    for step in range(0,len(numberOfStep)):
        for i in range(1,11):  
            name = "{}{}step-{}.csv".format(nameOfActivity[activity],numberOfStep[step],i)
            for filename in filenames:   
                if(name == filename):
                    new_data= pd.read_csv("C:\\Users\\halil\\Desktop\\Tez\\smart-sneakers\\data\\cleaning-datas\\resize-data\\{}".format(name))
                    new_data2 = [[new_data.ax.mean(),new_data.ay.mean(),new_data.az.mean(),new_data.gx.mean(),new_data.gy.mean(),new_data.gz.mean()]]
                    new_data3 = pd.DataFrame(new_data2,columns = ["ax_mean","ay_mean","az_mean","gx_mean","gy_mean","gz_mean",
                                                                  ""])
                    new_data3["step"] = numberOfStep[step]
                    new_data3["activity"] = nameOfActivity[activity]
                    frames = [new_data4,new_data3]
                    new_data4 = pd.concat(frames)
                    new_data4.to_csv("C:\\Users\\halil\\Desktop\\Tez\\smart-sneakers\\data\\cleaning-datas\\concat-data\\md-data.csv",encoding='utf-8')
#%% Verilerin ortalamasını, standart sapmasını, medyanını, min ve max lerini alarak tek satıra indirgeme
                   
new_data4 = pd.DataFrame()
for activity in range(0, len(nameOfActivity)):
    for step in range(0,len(numberOfStep)):
        for i in range(1,11):  
            name = "{}{}step-{}.csv".format(nameOfActivity[activity],numberOfStep[step],i)
            for filename in filenames:   
                if(name == filename):
                    new_data= pd.read_csv("C:\\Users\\halil\\Desktop\\Tez\\smart-sneakers\\data\\cleaning-datas\\resize-data\\{}".format(name))
                    dict1 = {"ax_mean":[new_data.ax.mean()],"ay_mean":[new_data.ay.mean()],"az_mean":[new_data.az.mean()],
                    "gx_mean":[new_data.gx.mean()],"gy_mean":[new_data.gy.mean()],"gz_mean":[new_data.gz.mean()],
                             "ax_std":[new_data.ax.std()],"ay_std":[new_data.ay.std()],"az_std":[new_data.az.std()],
                             "gx_std":[new_data.gx.std()],"gy_std":[new_data.gy.std()],"gz_std":[new_data.gz.std()],
                             "ax_median":[new_data.ax.median()],"ay_median":[new_data.ay.median()],"az_median":[new_data.az.median()],
                             "gx_median":[new_data.gx.median()],"gy_median":[new_data.gy.median()],"gz_median":[new_data.gz.median()],
                             "ax_min":[new_data.ax.min()],"ay_min":[new_data.ay.min()],"az_min":[new_data.az.min()],
                             "gx_min":[new_data.gx.min()],"gy_min":[new_data.gy.min()],"gz_min":[new_data.gz.min()],
                             "ax_max":[new_data.ax.max()],"ay_max":[new_data.ay.max()],"az_max":[new_data.az.max()],
                             "gx_max":[new_data.gx.max()],"gy_max":[new_data.gy.max()],"gz_max":[new_data.gz.max()]}
                    new_data3 = pd.DataFrame(dict1)
                    new_data3["count"] = len(new_data)                                           
                    new_data3["step"] = numberOfStep[step]
                    new_data3["activity"] = nameOfActivity[activity]
                    frames = [new_data4,new_data3]
                    new_data4 = pd.concat(frames)
                    new_data4.to_csv("C:\\Users\\halil\\Desktop\\Tez\\smart-sneakers\\data\\cleaning-datas\\concat-data\\md-data.csv",
                    encoding='utf-8')
 #%%
                   
new_data4 = pd.DataFrame()
for activity in range(0, len(nameOfActivity)):
    for step in range(0,len(numberOfStep)):
        for i in range(1,11):  
            name = "{}{}step-{}.csv".format(nameOfActivity[activity],numberOfStep[step],i)
            for filename in filenames:   
                if(name == filename):
                    new_data= pd.read_csv("C:\\Users\\halil\\Desktop\\Tez\\smart-sneakers\\data\\cleaning-datas\\resize-data\\{}".format(name))
                    dict1 = {"ax_mean":[new_data.ax.mean()],"ay_mean":[new_data.ay.mean()],"az_mean":[new_data.az.mean()],"gx_mean":[new_data.gx.mean()],"gy_mean":[new_data.gy.mean()],"gz_mean":[new_data.gz.mean()],
                             "ax_std":[new_data.ax.std()],"ay_std":[new_data.ay.std()],"az_std":[new_data.az.std()],"gx_std":[new_data.gx.std()],"gy_std":[new_data.gy.std()],"gz_std":[new_data.gz.std()],
                             "ax_median":[new_data.ax.median()],"ay_median":[new_data.ay.median()],"az_median":[new_data.az.median()],"gx_median":[new_data.gx.median()],"gy_median":[new_data.gy.median()],"gz_median":[new_data.gz.median()],
                             "ax_min":[new_data.ax.min()],"ay_min":[new_data.ay.min()],"az_min":[new_data.az.min()],"gx_min":[new_data.gx.min()],"gy_min":[new_data.gy.min()],"gz_min":[new_data.gz.min()],
                             "ax_max":[new_data.ax.max()],"ay_max":[new_data.ay.max()],"az_max":[new_data.az.max()],"gx_max":[new_data.gx.max()],"gy_max":[new_data.gy.max()],"gz_max":[new_data.gz.max()]}
                    new_data3 = pd.DataFrame(dict1)
                    new_data3["count"] = len(new_data)                                           
                    new_data3["step"] = numberOfStep[step]
                    new_data3["activity"] = nameOfActivity[activity]
                    frames = [new_data4,new_data3]
                    new_data4 = pd.concat(frames)
                    new_data4.to_csv("C:\\Users\\halil\\Desktop\\Tez\\smart-sneakers\\data\\cleaning-datas\\concat-data\\md-data.csv",encoding='utf-8')                  
#%%
# Adım sutunu ekleme                   

for activity in range(0, len(nameOfActivity)):
    for step in range(0,len(numberOfStep)):
        for i in range(1,11):  
            name = "{}{}step-{}.csv".format(nameOfActivity[activity],numberOfStep[step],i)
            for filename in filenames:   
                if(name == filename):
                    new_data= pd.read_csv("C:\\Users\\halil\\Desktop\\Tez\\smart-sneakers\\data\\cleaning-datas\\resize-data\\{}".format(name))
                    new_data["step"] = numberOfStep[step]
                    new_data.to_csv("C:\\Users\\halil\\Desktop\\Tez\\smart-sneakers\\data\\cleaning-datas\\step-data\\{}".format(name),encoding='utf-8')     
                    
#%%
downData = pd.DataFrame()
upData = pd.DataFrame()
walkData = pd.DataFrame()
runData = pd.DataFrame()

#%%
# Aynı aktiviteye sahip verileri birleştirme
                                     
numberOfStep = [1,3,5,11]
nameOfActivity = "run"

old_data = pd.DataFrame()
for step in numberOfStep:
    for i in range(1,11):  
        name = "{}{}step-{}.csv".format(nameOfActivity,step,i)
        for filename in filenames:   
            if(name == filename):
                new_data= pd.read_csv("C:\\Users\\halil\\Desktop\\Tez\\smart-sneakers\\data\\cleaning-datas\\step-data\\{}".format(name))
                frames = [runData,new_data]
                runData = pd.concat(frames)

#%%
#Aktivite sutunu ekleme
downData["activity"] = "downstairs"
upData["activity"] = "upstairs"
walkData["activity"] = "walk"
runData["activity"] = "run"

#%% verileri birleştirme
data = pd.concat([downData, upData, walkData, runData])

data.to_csv('C:\\Users\\halil\\Desktop\\Tez\\smart-sneakers\\data\\cleaning-datas\\concat-data\\data7.csv',encoding='utf-8')

#%% time etiketi düzenleme
all_data = pd.read_csv('C:\\Users\\halil\\Desktop\\Tez\\smart-sneakers\\data\\cleaning-datas\\concat-data\\data8.csv')

def t(n):
    return n*100

all_data.time = all_data.time.apply(t)

all_data.to_csv('C:\\Users\\halil\\Desktop\\Tez\\smart-sneakers\\data\\cleaning-datas\\concat-data\\data9.csv',encoding='utf-8')