sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.2.1
nfdc face create udp://192.168.2.5
nfdc face create udp://192.168.2.9
nfdc face create udp://192.168.2.13
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-controller.conf