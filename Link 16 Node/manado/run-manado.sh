sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.43
nfdc face create udp://192.168.1.45
nfdc face create udp://192.168.1.50
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-manado.conf