sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.5.5
nfdc face create udp://192.168.5.10
nfdc face create udp://192.168.5.14
nfdc face create udp://192.168.5.26
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-bandung.conf