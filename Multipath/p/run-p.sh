sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.29
nfdc face create udp://192.168.1.33
nfdc face create udp://192.168.1.37
nfdc face create udp://192.168.1.41
nfdc face create udp://192.168.1.45
nfdc face create udp://192.168.1.49
nfdc face create udp://192.168.1.53
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-p.conf