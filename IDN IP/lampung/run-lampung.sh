sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.37
nfdc face create udp://192.168.1.57
nfdc face create udp://192.168.1.62
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-lampung.conf