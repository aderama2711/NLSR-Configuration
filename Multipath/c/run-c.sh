sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.2
nfdc face create udp://192.168.1.6
nfdc face create udp://192.168.1.10
nfdc face create udp://192.168.1.14
nfdc face create udp://192.168.1.18
nfdc face create udp://192.168.1.22
nfdc face create udp://192.168.1.26
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-c.conf