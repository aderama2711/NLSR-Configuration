sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.6
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-Batam .conf