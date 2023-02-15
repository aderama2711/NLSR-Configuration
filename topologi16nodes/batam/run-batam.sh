sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.1
nfdc face create udp://192.168.1.10
nfdc face create udp://192.168.1.14
nfdc face create udp://192.168.1.18
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-batam.conf