def isInitialDeployment():
    for delta in deltas.deltas:
        if delta.operation != "CREATE":
            return False
    return True

print "-------------- INITIAL DEPLOYMENT %s " % isInitialDeployment()

if isInitialDeployment():
    context.addStep(steps.manual(
        description = "Send mails",
        order = 50,
        message_template = "templates/email.txt.ftl",
        mail_server = deployedApplication.environment.smtpServer,
        mail_to = ["jdoe@operations.example.com","manager@operations.example.com"],
        mail_from = "noreply@deployment.example.com",
        subject = "Deploying...",
        freemarker_context = {"buttonColour": "green"}
    ))
