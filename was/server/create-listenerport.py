# Create Listener Port
containerId = validateNotEmpty(AdminConfig.getid(deployed.container.containmentPath), "Cannot locate container at path %s " %(deployed.container.containmentPath))
# Returns the id of the MessageListenerService of the Server
mlsId = AdminConfig.list('MessageListenerService', containerId)
print "Listener Service [", mlsId,"]"
args = toAdminConfigArgs(deployed.getExposedProperties(True))
print "Creating Listener Port in %s with args %s " % (containerId, args)
newListenerPortId = AdminConfig.create(deployed.wasType, mlsId, args)
if deployed.initialStateStarted == True:
    AdminConfig.create('StateManageable', newListenerPortId, [['initialState', 'START']])
else:
    AdminConfig.create('StateManageable', newListenerPortId, [['initialState', 'STOP']])

