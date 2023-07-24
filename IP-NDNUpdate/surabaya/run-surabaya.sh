sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.5.25
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-surabaya.conf