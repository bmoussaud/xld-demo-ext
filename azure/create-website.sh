echo "Creating webserver ${deployed.name}/${deployed.fqdn}"

azure site create --location "${deployed.location}" ${deployed.fqdn} --github --githubusername ${deployed.githubUsername}  --githubpassword ${deployed.githubPassword} --githubrepository ${deployed.githubRepository}

