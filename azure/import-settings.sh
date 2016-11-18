echo "Importing credential settings"
echo '${container.credentialsPublishSettings}'  > ./credentials.publishsettings
cat ./credentials.publishsettings
azure account import ./credentials.publishsettings
sleep 60




