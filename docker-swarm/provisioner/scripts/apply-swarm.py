import com.xebialabs.deployit.provision.host.LazyHost as LazyHost

def to_host(deployed,p):
    host = wrap(LazyHost())
    host.setHostTemplate(p.deployable.hostTemplate)
    host.setProvisionedBlueprint(deployedApplication)
    host.setSourceProvisioned(deployed)
    return host

def swarm_manager_step(deployed,p):
    context.addStep(steps.os_script(
        description="Configure {0} as a Swarm Manager".format(deployed.container.name),
        order=80,
        script="docker-swarm/configure_manager",
        freemarker_context={'name': deployed.name, 
            'target': deployed.container,
            'token':context.getAttribute('PROVISIONER').managerToken,
            'manager':context.getAttribute('FIRST')},
        target_host=to_host(deployed,p)))

def swarm_first_manager_step(deployed,p):
    context.addStep(steps.os_script(
        description="(First) Configure {0} as a Swarm Manager".format(deployed.container.name),
        order=79,
        script="docker-swarm/configure_firt_manager",
        freemarker_context={'name': deployed.name, 'target': deployed.container},
        target_host=to_host(deployed,p)))

def swarm_worker_step(deployed,p):
    context.addStep(steps.os_script(
        description="Configure {0} as a Swarm Worker".format(deployed.container.name),
        order=82,
        script="docker-swarm/configure_worker",
        freemarker_context={'name': deployed.name,
            'target': deployed.container,
            'token':context.getAttribute('PROVISIONER').workerToken,
            'manager':context.getAttribute('FIRST')},
        target_host=to_host(deployed,p)))

def is_first(ci,p):
    if context.getAttribute('FIRST') is None:
        context.setAttribute('FIRST',ci)
        context.setAttribute('PROVISIONER',p)
        return True
    else:
        return False

swarm_provisioners = filter(lambda provisioner: provisioner.type == "docker.provisioner.AppliedSwarm", deployed.provisioners)
for p in swarm_provisioners:
    if p.manager:
        if is_first(deployed,p):
            swarm_first_manager_step(deployed,p)
        else:
            swarm_manager_step(deployed,p)
    else:
        swarm_worker_step(deployed,p)

