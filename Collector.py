import tbapy
from  openpyxl import * # excell kütüphanesi import
tba = tbapy.TBA('cdzX6vxq3ege20z22fUMoLA7ABcsvIceWOQrAh4ppZCqiW6y59qZlSFIFfmyZbpg') # api keyimiz"
turkishteams = ['2905',
'3390','3646','4191','4972','5655','5665','5773',
'5993','6014','6025','6038','6064','6228',
'6232','6380','6388','6402','6415',
'6429','6430','6431','6435','6436','6459','6697',
'6838','6874','6948','6985','6988','6989','6999','7010','7035','7050','7070','7071',
'7086','7108','7134','7228','7292',
'7293','7296','7298','7439','7444','7458','7465','7466','7469','7478','7481','7536',
'7544','7552','7569','7575',
'7576','7585','7600','7611','7613',
'7637','7672','7682','7683','7684','7729','7742','7748','7758',
'7761','7792','7828','7830','7831','7839','7840','7841'] ## türk takımları

kitap = Workbook() # excell olustur

for i in range(len(turkishteams)):
    t= turkishteams[i] # seçili türk takımı nosu
    odul = tba.team_awards('frc'+ t) # tbadan takımın aldığı ödülü çek
    kitap.create_sheet(t) # excellde bu takım adında bi sheet olustur
    yaz = kitap.get_sheet_by_name(t) #  takım adında olusturulan sheete gir
    yaz.append(['Öduller','Event' , 'Ödül Yılı' , 'Takım Adı']) # sütun adı takım numarası

    
    for item in odul:
    	team= item['name'] # ödülleri pars et
    	event= item['event_key']
    	year= item['year']

    	print(team, event, year ) # pars edilen ödülleri ekrana yazdır
    	yaz.append([team, event, year]) # excelle ödülleri yazdır
kitap.save("dosya.xlsx") # exceli kaydet
kitap.close() #excelli kapat
