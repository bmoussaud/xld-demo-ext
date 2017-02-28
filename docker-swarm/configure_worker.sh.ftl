echo "configure '${deployed.id}' worker  using the '${manager.id} manager"
docker swarm join --token ${token} ${manager.docker_host_address}:2377
