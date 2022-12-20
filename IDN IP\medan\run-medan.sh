sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.5
nfdc face create udp://192.168.1.9
nfdc face create udp://192.168.1.14
nfdc face create udp://192.168.1.18
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-medan.conf