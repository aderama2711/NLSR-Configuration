sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.85
nfdc face create udp://192.168.1.93
nfdc face create udp://192.168.1.98
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-manado.conf