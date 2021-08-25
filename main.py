import xlrd
loc = "dokum.xls"

inputworkbook = xlrd.open_workbook(loc)
inputworksheet = inputworkbook.sheet_by_index(0)
toplamislem = (inputworksheet.nrows - 1)
toplamlong = 0
toplamshort = 0
toplamlongkar = 0
toplamshortkar = 0
basarililong = 0
basarisizlong = 0
basarilishort = 0
basarisizshort = 0
long1= "l"

for y in range (1, inputworksheet.nrows):
    longshortbakim = inputworksheet.cell_value(y,2)
    if longshortbakim == "l":
        toplamlong = toplamlong + 1
    else :
        toplamshort = toplamshort + 1





for y in range (1, inputworksheet.nrows):
    longshortbakim = inputworksheet.cell_value(y,2)
    if longshortbakim == "l":
        toplamlongkar = float(toplamlongkar) + float((inputworksheet.cell_value(y,5)))
        if float(inputworksheet.cell_value(y,5)) > 0:
            basarililong = basarililong + 1
        else:
            basarisizlong = basarisizlong + 1

for y in range (1, inputworksheet.nrows):
    longshortbakim = inputworksheet.cell_value(y,2)
    if longshortbakim == "s":
        toplamshortkar = float(toplamshortkar) + float((inputworksheet.cell_value(y,5)))
        if float(inputworksheet.cell_value(y,5)) > 0:
            basarilishort = basarilishort + 1
        else:
            basarisizshort = basarisizshort + 1

print("Toplam işlem sayısı : ", toplamislem)
print("Toplam Long işlem sayısı : ", toplamlong)
print("Toplam Short işlem sayısı : ", toplamshort)
print("Başarılı long işlem sayisi", basarililong)
print("Başarısız long işlem sayisi", basarisizlong)
print("Başarılı short işlem sayisi", basarilishort)
print("Başarısız short işlem sayisi", basarisizshort)
print("Long İşlemlerden gelen toplam kar :", toplamlongkar)
print("Short İşlemlerden gelen toplam kar :", toplamshortkar)
