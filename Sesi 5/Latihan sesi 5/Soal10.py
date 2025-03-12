import random 

def main():
    print('Batu Gunting Kertas Anjay')
    
    skor_P = 0 
    skor_C = 0 
    continue_game = True
    
    while continue_game:
        pemain = input('Batu / Gunting / Kertas ? ').capitalize()
        komputer = random.choice(['Batu', 'Gunting', 'Kertas'])
        print ('Pemain Memilih :', pemain)
        print("Komputer Memilih :", komputer)
        
        if pemain not in ['Batu', 'Gunting', 'Kertas'] :
            print('Input Tidak Valid. Permainan Berakhir')
            break
        
        if pemain == komputer:
            print('Seri Boss')
        elif pemain == 'Batu' and komputer == 'Gunting' or pemain == 'Gunting' and komputer == 'Kertas' or pemain == 'Kertas' and komputer == 'Batu' :
            skor_P += 1
            print('Pemain Menang')
        else:
            skor_C += 1 
            print('Pemain Kalah !')
            
        print('Skor Pemain :', skor_P)
        print('Skor Komputer :', skor_C)
        
        lanjut = input('Apakah Anda ingin Melanjutkan Permainan?? (Y/N)').lower()
        if lanjut != 'y':
            continue_game = False
            
    print('Skor Akhir Pemain :' , skor_P)
    print('Skor Akhir Komputer: ', skor_C)
    
 
if __name__ == "__main__" :
    main()