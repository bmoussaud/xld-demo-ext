import sys
import redis
import json
from urlparse import urlparse

# docker run -it --link cache:redis --rm redis:2.6 sh -c 'exec redis-cli -h "$REDIS_PORT_6379_TCP_ADDR" -p "$REDIS_PORT_6379_TCP_PORT"'
# SET 'Infrastructure/vault/vaulted-host-dev' '{"username":"ubuntu","password":"ubuntu","privateKeyFile":"","passphrase":"" }'

print "Fetch credential for '%s' using '%s' vault " % (host, host.vault)
print "Connection to %s.... " % (host.vault.url)
reason = "Deploying '%s/%s' on '%s' environment using XL Deploy" % (deployedApp.version.application.name, deployedApp.version.name, deployedApp.environment.name)
print "Reason : %s" % reason
netloc = urlparse(host.vault.url).netloc.split(':')
r = redis.StrictRedis(host=netloc[0], port=netloc[1], db=0)
json_info = r.get('Infrastructure/vault/vaulted-host-dev')
info = json.loads(json_info)
print info
host.username = info['username']
host.password = info['password']
host.privateKeyFile = info['privateKeyFile']
host.passphrase = info['passphrase']

