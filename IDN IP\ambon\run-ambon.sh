sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.153
nfdc face create udp://192.168.1.145
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-ambon.conf