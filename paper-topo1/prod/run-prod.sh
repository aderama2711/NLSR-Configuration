sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.14
nfdc face create udp://192.168.1.18
nfdc face create udp://192.168.1.22
echo NLSR Started >> ~/timedate.log
echo $(date) >> ~/timedate.log
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-prod.conf