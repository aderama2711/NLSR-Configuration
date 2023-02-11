sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.35
nfdc face create udp://192.168.1.39
nfdc face create udp://192.168.1.46
nfdc face create udp://192.168.1.48
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-makassar.conf