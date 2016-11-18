def databases():
    return filter(lambda ci: str(ci.type) == 'sql.MySqlClient', deployedApplication.environment.members)

if specification.deployedOrPreviousApplication.cleanUpBackup is True:
    for database in databases():
        print "processing %s " % database
        filename = "%s/backup_%s_%s_%s_%s.sql" % ( deployedApplication.environment.backupDirectory, deployedApplication.version.application.name, deployedApplication.version.name,deployedApplication.environment.name, database.getProperty("databaseName"))
        #filename = "%s/backup_%s_%s_%s_%s.sql" % ( deployedApplication.environment.backupDirectory, deployedApplication.version.application.name, deployedApplication.version.name,deployedApplication.environment.name, database.databaseName)
        context.addStep(steps.delete(description="Delete backup file %s" % filename,
                target_path = filename,
                target_host = database.host
                )
            )


