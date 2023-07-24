sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.5.30
nfdc face create udp://192.168.5.34
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-gateway2.conf