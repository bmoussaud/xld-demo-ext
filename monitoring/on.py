
def new_instance(ci_type, ci_id):
    return metadataService.findDescriptor(Type.valueOf(ci_type)).newInstance(ci_id)

def new_host():
    ci = new_instance('overthere.LocalHost','Infrastructure/LocalHostForMonitoring')
    ci.os = "UNIX"
    return ci

deployedApplication = specification.deployedOrPreviousApplication
env = deployedApplication.environment
if env.enableMonitoring is True:
    context.addStep(steps.os_script(
        description="Enable monitoring (%s)" % env.monitoringURL,
        order=25,
        script="monitoring/on",
        freemarker_context={'env': env,'appname': deployedApplication.version.application.name},
        target_host=new_host(),
        ))
