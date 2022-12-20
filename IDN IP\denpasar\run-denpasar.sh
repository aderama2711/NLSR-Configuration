sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.109
nfdc face create udp://192.168.1.121
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-denpasar.conf