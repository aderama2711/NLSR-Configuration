sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.21
nfdc face create udp://192.168.1.50
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-r6.conf