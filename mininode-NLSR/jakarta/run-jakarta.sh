sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.2
nfdc face create udp://192.168.1.6
nfdc face create udp://192.168.2.2
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-jakarta.conf