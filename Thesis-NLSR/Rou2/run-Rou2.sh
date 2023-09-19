sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.5
nfdc face create udp://192.168.1.17
echo NLSR Started >> ~/timedate.log
echo $(date) >> ~/timedate.log
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-Rou2.conf