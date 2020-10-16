import serial
import csv

unsavedData = []
data = []
datas = []

# Kalman Filtresi Değişkenleri
kalman_old = [0,0,0,0,0,0,0]
cov_old = [0,0,0,0,0,0,0]
kalman_new = [0,0,0,0,0,0,0]
cov_new = [0,0,0,0,0,0,0]
kalman_gain = [0,0,0,0,0,0,0]
kalman_calculated = [0,0,0,0,0,0,0]
kalman_old[0] = 0
cov_old[0] = 0

#Verileri oku.
def dataRead(loopCount):
    print("Veriler okunuyor...")
    for i in range(0,loopCount):
        data = ser.readline().decode("utf-8").split(" ")#Gelen verileri "utf-8" formatına dönüştürüp parçalıyoruz.
        if(i>0):#ilk veri eksik geliyor. O yüzden if ile ilk veriyi atlıyoruz.
            datas.append(data)#Parçalanan veriler diziye aktarılıyor.          
    print("Veri okuma bitti.")

#Verileri hareket ettiğimde oku durduğumda okumayı durdur.
def dataReadMovePause():
    print("Veriler okunuyor...")
    i=0
    while(True):
        unsavedData = ser.readline().decode("utf-8").split(" ")#Gelen verileri "utf-8" formatına dönüştürüp parçalıyoruz.
        if(i>0):#ilk veri eksik geliyor. O yüzden if ile ilk veriyi atlıyoruz.
            #Hareket edip etmediğini kontrol ediyor.
            if(((int(unsavedData[4])<-3000) or (int(unsavedData[4])>3000)) and 
            ((int(unsavedData[5])<-3000) or (int(unsavedData[5])>-3000)) and 
            ((int(unsavedData[6])<-3000) or (int(unsavedData[6])>3000))):
                print("Veriler alınmaya başlandı.")
                k = 0 
                r = 0 
                j = 0
                while(True):
                    data = ser.readline().decode("utf-8").split(" ")#Gelen verileri "utf-8" formatına dönüştürüp parçalıyoruz.
                    if(((int(data[4])>-3000) and (int(data[4])<3000)) and ((int(data[5])>-3000) and 
                    (int(data[5])<3000)) and ((int(data[6])>-3000) and (int(data[6])<3000))):
                        if(r != (j-1)):
                            k=0
                        r=j
                        k+=1
                        if(k > 30):                  
                            print("Veri alma durduruldu.")
                            break
                    datas.append(data)#Parçalanan veriler diziye aktarılıyor. 
                    j = j + 1   
                break
        i = i + 1   
    print("Veri okuma bitti.")     

#süreyi sıfırdan başlatır ve son iki değeri yuvarlar
def timeSync():
    firstTime = int(datas[0][0])
    for i in range (0,len(datas)-31):
        time = int(datas[i][0]) - firstTime
        datas[i][0] = str(round(time,-2))

#Kalman filtresi
def kalman_filter (Q=0.50,R=0.9):  
  
    for i in range(0,len(datas)-31):
        for j in range(0,6):
            kalman_new[j] = kalman_old[j] #eski değer alınır.
            
            cov_new[j] = cov_old[j] + Q #yeni kovaryans değeri belirlenir. Q=0.50 alınmıştır.
        
            kalman_gain[j] = cov_new[j] / (cov_new[j] + R) #kalman kazancı hesaplanır. R=0.9 alınmıştır
            kalman_calculated[j] = kalman_new[j] + (kalman_gain[j] * (int(datas[i][j]) - kalman_new[j])) #kalman değeri hesaplanır
        
            cov_new[j] = (1 - kalman_gain[j]) * cov_old[j] #yeni kovaryans değeri hesaplanır
            cov_old[j] = cov_new[j] #yeni değerler bir sonraki döngüde kullanılmak üzere kaydedilir
        
            kalman_old[j] = kalman_calculated[j]

            datas[i][j] = str(kalman_calculated[j]) #hesaplanan kalman değeri çıktı olarak verilir

#Csv formatında kaydet.
def saveCSV():
    print("Veriler kaydediliyor...")
    with open("Desktop\\tez\\smart_sneakers_ardunio\\my-datas\\upstairs11step-10.csv", "w", newline="", encoding="utf-8") as f:
        yazici = csv.writer(f)
        yazici.writerow(["time","ax","ay","az","gx","gy","gz"])
        for i in range(0,len(datas)-31):
            yazici.writerow([
            datas[i][0],
            datas[i][1],
            datas[i][2],
            datas[i][3],
            datas[i][4],
            datas[i][5],
            datas[i][6]])   
    f.close()
    print("Veriler kaydedildi.")

#Verileri ekrana yazdır.
def displayWrite():
     for i in range(0,len(datas)-31): 
        print(datas[i][0],
            datas[i][1],
            datas[i][2],
            datas[i][3],
            datas[i][4],
            datas[i][5],
            datas[i][6])  

#İşlemler
try: 
    print("Bluetooth bağlantısı kuruluyor..")
    ser = serial.Serial('COM4' , 9600)
    
    dataReadMovePause()
    timeSync()
    kalman_filter()
    saveCSV()
except EnvironmentError as identifier:
    print("Cihazın açık olduğundan emin olunuz.", identifier)
