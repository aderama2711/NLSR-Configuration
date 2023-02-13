sudo mkdir /var/lib/nlsr

nfdc face create udp://192.169.1.73
nfdc face create udp://192.168.1.77
nfdc face create udp://192.168.1.86
nfdc face create udp://192.168.1.90
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-makassar.conf