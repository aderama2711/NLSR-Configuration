sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.1
nfdc face create udp://192.168.1.13
echo NLSR Started >> ~/timedate.log
echo $(date) >> ~/timedate.log
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-r1.conf