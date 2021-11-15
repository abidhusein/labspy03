n = 0
while True:
    a = int(input('Masukan Nilai : '))
    if n < a:
        n = a
    if a == 0 : 
        break
print ('Bilangan Terbesar', n)