sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.17
nfdc face create udp://192.168.1.74
nfdc face create udp://192.168.1.78
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-jakarta.conf