sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.5.38
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-Bogor .conf