sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.1
nfdc face create udp://192.168.1.13
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-Rou1.conf