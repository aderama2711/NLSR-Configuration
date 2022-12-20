sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.69
nfdc face create udp://192.168.1.126
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-pontianak.conf