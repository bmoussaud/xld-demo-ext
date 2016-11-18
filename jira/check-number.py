deployedApplication = specification.deployedOrPreviousApplication
version = deployedApplication.version
env = deployedApplication.environment

if env.requiresChangeTicketNumber == True :
    context.addStep(steps.jython(
        description="Check if the [%s] Ticket is valid" % (version.satisfiesChangeTicketNumber),
        order=10,
        script_path="jira/do-check-number.py",
        jython_context = {"jira": version.satisfiesChangeTicketNumber}
        )
    )



