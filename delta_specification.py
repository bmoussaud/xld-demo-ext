from com.xebialabs.deployit.plugin.api.deployment.specification import Operation

def dump_modified_delta(delta):
    print "DUMP %s " % delta
    ci_type = delta.deployed.type
    print ci_type
    ci_descriptor = metadataService.findDescriptor(Type.valueOf(str(ci_type)))
    print ci_descriptor
    for pd in ci_descriptor.getPropertyDescriptors():
        print "-- %s %s %s" % (pd, pd.get(delta.deployed), pd.get(delta.previous))


print "-------------------------------------------------------------------------------------"
print "------------  DELTA SPECIFICATION ---------------------------------------------------"
print "-------------------------------------------------------------------------------------"
for _delta in deltas.deltas:
    print "[%s] " % (_delta)
    if _delta.getOperation() == Operation.MODIFY:
        dump_modified_delta(_delta)
print "-------------------------------------------------------------------------------------"

