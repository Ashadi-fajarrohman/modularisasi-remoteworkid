#program menhitung luas segitiga
print('menghitung luas segitiga')
alas = 10
tinggi = 6
luas = alas * tinggi /2
print(f'segitiga dengan alas = {alas} dan tinggi = {tinggi} memiliki luas {luas}')

alas = 18
tinggi = 2
luas = alas * tinggi /2
print(f'segitiga dengan alas = {alas} dan tinggi = {tinggi} memiliki luas {luas}')

print('membuat fungsi luas segitiga')
def hitung_luas_segitiga(alas, tinggi):
    luas = alas * tinggi / 2
    return luas
print(f'menghitung segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(10,6)}')
print(f'menghitung segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(100,52)}')
print(f'menghitung segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(392,222)}')


