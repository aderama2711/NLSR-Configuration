sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.16
nfdc face create udp://192.168.1.20
nfdc face create udp://192.168.1.24
nfdc face create udp://192.168.1.28
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-p.conf