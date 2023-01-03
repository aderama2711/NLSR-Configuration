sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.33
nfdc face create udp://192.168.1.45
nfdc face create udp://192.168.1.58
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-palembang.conf