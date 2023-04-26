sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.12
nfdc face create udp://192.168.1.29
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-r4.conf