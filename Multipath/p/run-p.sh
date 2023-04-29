sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.32
nfdc face create udp://192.168.1.36
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-p.conf