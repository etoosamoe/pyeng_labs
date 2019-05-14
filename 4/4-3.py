#Получить из строки CONFIG список VLANов вида: ['1', '3', '10', '20', '30', '100']


config = 'switchport trunk allowed vlan 1,3,10,20,30,100'

commands=config.strip().split()
print(commands)
vlans=commands[-1].split(',')
print('\n',vlans)