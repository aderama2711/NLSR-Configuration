sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.23
nfdc face create udp://192.168.1.27
nfdc face create udp://192.168.1.32
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-semarang.conf