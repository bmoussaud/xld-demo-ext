echo "Removing webserver ${deployed.id}"
echo "azure site delete -q ${deployed.fqdn}"
azure site delete -q ${deployed.fqdn}



