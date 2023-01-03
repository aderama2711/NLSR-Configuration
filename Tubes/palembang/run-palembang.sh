sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.9
nfdc face create udp://192.168.1.13
nfdc face create udp://192.168.1.18
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-palembang.conf