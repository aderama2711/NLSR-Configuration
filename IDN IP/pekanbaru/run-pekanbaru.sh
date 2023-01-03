sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.17
nfdc face create udp://192.168.1.26
nfdc face create udp://192.168.1.30
nfdc face create udp://192.168.1.34
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-pekanbaru.conf