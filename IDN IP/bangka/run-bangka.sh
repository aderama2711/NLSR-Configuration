sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.41
nfdc face create udp://192.168.1.46
nfdc face create udp://192.168.1.50
nfdc face create udp://192.168.1.54
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-bangka.conf