sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.2
nfdc face create udp://192.168.1.6
nfdc face create udp://192.168.1.10
echo NLSR Started >> ~/timedate.log
echo $(date) >> ~/timedate.log
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-cons.conf