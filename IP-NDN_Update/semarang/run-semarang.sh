sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.5.17
nfdc face create udp://192.168.5.22
nfdc face create udp://192.168.5.33
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-semarang.conf