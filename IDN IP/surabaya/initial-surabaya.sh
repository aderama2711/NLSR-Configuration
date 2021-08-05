
ndnsec-key-gen /ndn/surabaya > site.key
ndnsec-cert-gen -s /ndn/ site.key > site.cert
ndnsec-cert-install -f site.cert

ndnsec-key-gen /ndn/surabaya/%C1.Operator/op > operator.key 
ndnsec-cert-gen -s /ndn/surabaya operator.key > operator.cert 
ndnsec-cert-install -f operator.cert

ndnsec-key-gen /ndn/surabaya/%C1.Router/router > router.key 
ndnsec-cert-gen -s /ndn/surabaya/%C1.Operator/op router.key > router.cert 
ndnsec-cert-install -f router.cert
sudo cp /usr/local/etc/ndn/nfd.conf.sample /usr/local/etc/ndn/nfd.conf