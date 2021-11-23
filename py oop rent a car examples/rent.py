import datetime

class Arac():
    """
    Arac kiralama Parent sınıf
    """
    def __init__(self,stok):
        self.stok=stok
        self.now=0  #kiralama esnasındaki zamanı tutacagımız değişken
       
        
    
    def stokGoster(self):
        print("{} adet araç kiralanabilir".format(self.stok))
        return self.stok
    
    def gunlukKira(self,n):
        if n<=0:
            print("Araç sayısı 0 dan büyük olmalı")
            return None
        elif n>self.stok:
            print ("kiralanabilecek max araç sayısı= ",self.stok)
            return None
        else:
            self.now=datetime.datetime.now()
            print("{} adet araç {}  saatinde kiralandı".format(n,self.now.hour))
            self.stok -=n
            return self.now
            
    
    def saatlikKira(self,n):
        if n<=0:
            print("Araç sayısı 0 dan büyük olmalı")
            return None
        elif n>self.stok:
            print ("kiralanabilecek max araç sayısı= ",self.stok)
            return None
        else:
            self.now=datetime.datetime.now()
            print("{} adet araç {}  saatinde kiralandı".format(n,self.now.hour))
            self.stok -=n
            return self.now
            
    
    def iadeAl(self,aracTur,kiraOzet):
        oto_saat_ucreti=5
        oto_gun_ucreti=100
        bis_saat_ucreti=2
        bis_gun_ucreti=30
        
        kiraZamani,kiraTur,aracSayisi=kiraOzet #◘önemli *******
        fatura=0
        
        if aracTur=="araba":
            if kiraZamani and kiraTur and aracSayisi:
                self.stok+=aracSayisi
                now=datetime.datetime.now()
                fat_suresi=now-kiraZamani
        
            if kiraTur==1:  #saatlik kira 1 günlük 2
                fatura=fat_suresi.seconds/3600*oto_saat_ucreti*aracSayisi
                
            elif kiraTur==2:
                fatura=fat_suresi.seconds/(3600*24)*oto_gun_ucreti*aracSayisi
                
            if aracSayisi>3:
                print("araç sayısı 3 ten buyuk olduğu için %20 indirim kazandınız")
                fatura=fatura*0.8
                
            print("bizi tesrcih ettiğiniz için teşekkür ederiz")
            print("faturanız= {}".format(fatura))
            return fatura
        
        elif aracTur=="bisiklet":
            if kiraZamani and kiraTur and aracSayisi:
                self.stok+=aracSayisi
                now=datetime.datetime.now()
                fat_suresi=now-kiraZamani
        
            if kiraTur==1:  #saatlik kira 1 günlük 2
                fatura=fat_suresi.seconds/3600*bis_saat_ucreti*aracSayisi
                
            elif kiraTur==2:
                fatura=fat_suresi.seconds/(3600*24)*bis_gun_ucreti*aracSayisi
                
            if aracSayisi>3:
                print("araç sayısı 3 ten buyuk olduğu için %20 indirim kazandınız")
                fatura=fatura*0.8
                
            print("bizi tesrcih ettiğiniz için teşekkür ederiz")
            print("faturanız= {}".format(fatura))
            return fatura    
        
        else:
            print("Tanımlanmayan araç girişi yaptınız")
            return None
        

class oto(Arac):
    """
    Otomobil Kiralama sınıfı **child
    """
    def __init__(self,stok):
        super().__init__(stok)
        
    def indirim(self,ft):
        print("extra %30 indirim uygulandı")
        fatura=ft*0.7
        return fatura
    
        
class bisiklet(Arac):
    """
    Bisiklet Kiralama sınıfı **child
    """
    def __init__(self,stok):
        super().__init__(stok)
        

class Musteri():
    """
    Musteri Sınıfı   **parent
    """
    def __init__(self):
        self.bis=0
        self.kTur_b=0
        self.kZmn_b=0
                
        self.arc=0
        self.kTur_a=0
        self.kZmn_a=0
        
    def kirala(self,arcTur):
         if arcTur=="araba":
             arabalar=input("Kaç adet araba kiralamk istiyorsunuz= ")
             
             try:
                 arabalar=int(arabalar)
             except ValueError:
                print ("rakam girilmesi gerkeli !")
                return -1
            
             if(arabalar<1):
                print("Araba sayısı 0 dan büyük olmalı !")
                return -1
             else:
                self.arc=arabalar
                return self.arc
            
             
         elif arcTur=="bisiklet":
             bisikletler=input("Kaç adet bisiklet kiralamk istiyorsunuz= ")
             
             try:
                 bisikletler=int(bisikletler)
             except ValueError:
                print ("rakam girilmesi gerkeli !")
                return -1
            
             if(bisikletler<1):
                print("Bisiklet  sayısı 0 dan büyük olmalı !")
                return -1
             else:
                self.bis=bisikletler
                return self.bis
            
    def iadeEt(self,arcTur):
        
        if arcTur=="araba":
           if  self.arc and self.kTur_a and self.kZmn_a:
               return self.kZmn_a,self.kTur_a,self.arc
           else:
               return 0,0,0
            
        elif arcTur=="bisiklet":
            if  self.bis and self.kTur_b and self.kZmn_b:
               return self.kZmn_b,self.kTur_b,self.bis
            else:
               return 0,0,0
            
        else:
            print("Tanımsız araç türü")
            
             
        
             
        
        
        
        
        