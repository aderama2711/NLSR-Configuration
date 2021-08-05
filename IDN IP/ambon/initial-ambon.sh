
ndnsec-key-gen /ndn/ambon > site.key
ndnsec-cert-gen -s /ndn/ site.key > site.cert
ndnsec-cert-install -f site.cert

ndnsec-key-gen /ndn/ambon/%C1.Operator/op > operator.key 
ndnsec-cert-gen -s /ndn/ambon operator.key > operator.cert 
ndnsec-cert-install -f operator.cert

ndnsec-key-gen /ndn/ambon/%C1.Router/router > router.key 
ndnsec-cert-gen -s /ndn/ambon/%C1.Operator/op router.key > router.cert 
ndnsec-cert-install -f router.cert
sudo cp /usr/local/etc/ndn/nfd.conf.sample /usr/local/etc/ndn/nfd.conf