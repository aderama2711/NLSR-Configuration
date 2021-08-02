
nfd-start
nfdc face create udp://192.168.1.137
nfdc face create udp://192.168.1.141
nfdc face create udp://192.168.1.150
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-palu.conf