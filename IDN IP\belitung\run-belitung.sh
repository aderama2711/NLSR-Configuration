sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.53
nfdc face create udp://192.168.1.66
nfdc face create udp://192.168.1.70
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-belitung.conf