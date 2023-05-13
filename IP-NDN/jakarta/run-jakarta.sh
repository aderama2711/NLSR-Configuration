sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.5.13
nfdc face create udp://192.168.5.21
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-jakarta.conf