# Запросить	у	пользователя	ввод	IP-сети	в	формате:	10.1.1.0/24
# Затем	вывести	информацию	о	сети	и	маске	в	таком	формате:

# Проверить	работу	скрипта	на	разных	комбинациях	сеть/маска.


#Доп. задание: подстроить работу скрипта в случае если пользователь введет не адрес сети, а адрес хоста, к примеру 192.168.89.15/23 (адрес сети 192.168.88.0)
#Доп. задание 2: Преобразовать	скрипт	из	задания	5.1a	таким	образом,	чтобы	сеть/маска	не запрашивались	у	пользователя,	а	передавались	как	аргумент	скрипту.

ip_inp = input('Введите адрес, маску через слэш: ')
print('Введенные данные: ' + ip_inp)
ip_mask = ip_inp.split('/') # отделаем адрес сети от префикса маски
ip = ip_mask[0]
mask = ip_mask[1]
print('Адрес сети: ' + ip)
print('Маска: ' + mask)
ip_norm=ip.split('.') #делим айпишник на куски
ip_norm[3]='0' #заменяем последний кусок адреса на ноль, в задании не сказано было про 23-и маски, пока будет сложновато это сделать.

ip_template = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
zeros=32-int(mask) #ищем нужное количество нулей
mask_bits=str('1')*int(mask)+str('0')*int(zeros) #создаем строку с единицами и нулями
#print(mask_bits)
mask_list=[mask_bits[i:i+8] for i in range(0,32,8)] #создаем список единиц\нулей разделенный по восемь символов
#print(mask_list)
mask_int=[int(mask_list[i],2) for i in range(0,4)] # переводим этот список в десятичный вид
#print(mask_int)

mask_template = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''

print(ip_template.format(int(ip_norm[0]),int(ip_norm[1]),int(ip_norm[2]),int(ip_norm[3])))
print(mask_template.format(int(mask_int[0]),int(mask_int[1]),int(mask_int[2]),int(mask_int[3])))