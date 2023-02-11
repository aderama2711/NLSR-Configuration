sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.31
nfdc face create udp://192.168.1.33
nfdc face create udp://192.168.1.40
nfdc face create udp://192.168.1.42
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-surabaya.conf