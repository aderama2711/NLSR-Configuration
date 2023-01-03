sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.97
nfdc face create udp://192.168.1.101
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-surabaya.conf