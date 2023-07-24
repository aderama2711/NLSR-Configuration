sudo mkdir /var/lib/nlsr

nfdc face create udp://192.165.5.37
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-Bandung.conf