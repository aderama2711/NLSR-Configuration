sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.15
nfdc face create udp://192.168.1.24
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-cirebon.conf