import random


print('permainan Batu Gunting Kertas')
pemain = str(input('Batu / Gunting / Kertas?'))
comp = str (random.choice(['Batu', 'Gunting', 'Kertas']))
print('Pemain memilih: ', pemain)
print('Komputer memilih: ', comp)



if pemain == str('Batu') or pemain == str('Kertas') or pemain == str('Gunting') :
    print('input Valid')
else :
    print('Input tidak valid')
    

skor_P = 0
skor_C = 0
if pemain == comp:
    skor_P= 0
    print('Seri!')
elif pemain == 'Batu' and comp == 'Gunting':
    skor_P += 1
    print('Pemain menang!')
elif pemain == 'Gunting' and comp == 'Kertas' :
    skor_P += 1
    print('Pemain Menang')
elif pemain == 'Kertas' and comp == 'Batu':
    skor_P += 1
    print('Pemain Menang')
else :
    skor_C += 1
    print('Pemain Kalah')
    

    
print('Skor Pemain: ', skor_P)
print('Skor Computer: ', skor_C)
    