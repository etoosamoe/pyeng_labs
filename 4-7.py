#Преобразовать MAC-адрес в двоичную строку (без двоеточий).

mac = '000B:820C:52D8'

mac = mac.replace(':','')
mac_int=int(mac, 16)
mac_bin=bin(mac_int)
print(mac)
print('int: ',mac_int)
print('bin: ',mac_bin)