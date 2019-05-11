#Преобразовать строку MAC из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX

mac = 'AAAA:BBBB:CCCC'

mac1 = mac.replace(':','.')
print(mac1)