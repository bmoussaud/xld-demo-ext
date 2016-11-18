def databases():
    return filter(lambda ci: str(ci.type) == 'sql.MySqlClient', deployedApplication.environment.members)

deployedApplication = specification.deployedOrPreviousApplication
if deployedApplication.backupDatabase is True:
    for database in databases():
        print "processing %s " % database
        filename = "%s/backup_%s_%s_%s_%s.sql" % ( deployedApplication.environment.backupDirectory, deployedApplication.version.application.name, deployedApplication.version.name,deployedApplication.environment.name, database.getProperty("databaseName"))
        context.addStep(steps.os_script(
            description="Backup database %s" % database.name,
            order=20,
            script="backup/execute-backup",
            freemarker_context={'container': database, "backupFilename" : filename },
            target_host=database.host)
        )



