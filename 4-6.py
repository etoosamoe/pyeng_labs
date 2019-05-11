#Обработать	строку	ospf_route	и	вывести	информацию	на
# стандартный	поток	вывода	в виде:

#Protocol:
# OSPF Prefix:																	10.0.24.0/24 AD/Metric:														110/41 Next-Hop:															10.0.13.3 Last	update:												3d18h Outbound	Interface:					FastEthernet0/0


ospf_route	=	'OSPF								10.0.24.0/24	[110/41]	via	10.0.13.3,	3d18h,	FastEthernet0/0'
ospf_route=ospf_route.split()

#dict={
#    'protocol':ospf_route(1),
#}
protocol=ospf_route[0]
prefix=ospf_route[1]
metric=ospf_route[2]
nexthop=ospf_route[4]
update=ospf_route[5]
out_iface=ospf_route[6]


print(ospf_route)

template = '''
Protocol: {:>15}
Prefix: {:>25}
Metric: {:>21}
Nexthop: {:>21}
Last update: {:>13}
Outboud interface: {:>17}
'''

print(template.format(protocol,prefix,metric,nexthop.strip(','),update.strip(','),out_iface))
#print(dict)