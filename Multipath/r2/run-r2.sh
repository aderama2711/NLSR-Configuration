sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.5
nfdc face create udp://192.168.1.34
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-r2.conf