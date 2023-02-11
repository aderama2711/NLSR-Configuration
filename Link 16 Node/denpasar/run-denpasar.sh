sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.29
nfdc face create udp://192.168.1.41
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-denpasar.conf