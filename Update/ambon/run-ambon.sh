sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.5.1
nfdc face create udp://192.168.5.6
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-ambon.conf