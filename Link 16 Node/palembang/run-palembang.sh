sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.3
nfdc face create udp://192.168.1.5
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-palembang.conf