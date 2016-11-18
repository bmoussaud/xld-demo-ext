echo "# Processing backup ${container.name} file is  ${backupFilename}"
${container.mySqlHome}/bin/mysqldump -u ${container.username} -p${container.password} ${container.databaseName} > ${backupFilename}

