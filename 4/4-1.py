#Обработать строку NAT таким образом, чтобы в имени интерфейса вместо FastEthernet было GigabitEthernet.


#NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"

nat="ip nat inside source list ACL interface FastEthernet0/1 overload"
nat1=nat.replace('Fast', 'Gigabit')

print(nat1)