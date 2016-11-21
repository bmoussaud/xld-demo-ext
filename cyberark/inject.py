
def mappings():
    mapping = {}
    mapping['was.ManagedServer']=(lambda c: c.node.cell)
    mapping['was.NodeAgent']=(lambda c: c.cell)
    mapping['was.DeploymentManager']=(lambda c: c)
    return mapping

def to_host(delta):
    container = delta.deployedOrPrevious.container
    if container.hasProperty('host'):
        return container.host
    else:
        return mappings()[str(container.type)](container)

def hosts(candidate_filter):
    return set(map(to_host, filter(candidate_filter, specification.deltas)))

def secured_hosts():
    return hosts(lambda delta : to_host(delta).type == "cyber-ark.SshHost")

def deployedApp():
    if specification.operation == 'DESTROY':
        return previousDeployedApplication
    else:
        return deployedApplication

def generate_steps(host):
    context.addStep(steps.jython(
        description="Inject credential information '%s' using the '%s' vault server" % (host.name, host.vault.name),
        order=20,
        script_path="cyberark/fetch_credentials.py",
        jython_context={'host': host, 'deployedApp': deployedApp()})
    )


#map(generate_steps, secured_hosts())

