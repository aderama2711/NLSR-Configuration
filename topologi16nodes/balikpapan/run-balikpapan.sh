sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.81
nfdc face create udp://192.168.1.94
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-balikpapan.conf