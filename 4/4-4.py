#Из строк command1 и command2 получить список VLANов, которые есть и в команде command1
# и в команде command2.
#Для данного примера, результатом должен быть список: [1, 3, 100]
# Этот список содержит подсказку по типу итоговых данных.

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

com1splitted=command1.split()
com2splitted=command2.split()

print(com1splitted)
print(com2splitted)

vlans1=com1splitted[-1].split(',')
vlans2=com2splitted[-1].split(',')

vlans1.extend(vlans2)
vlan=sorted(vlans1)
print(vlan)

