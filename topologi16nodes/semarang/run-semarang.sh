sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.45
nfdc face create udp://192.168.1.53
nfdc face create udp://192.168.1.62
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-semarang.conf