sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.7
nfdc face create udp://192.168.1.13
nfdc face create udp://192.168.1.20
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-pontianak.conf