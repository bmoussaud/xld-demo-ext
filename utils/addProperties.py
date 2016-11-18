import sys

print "=================================================================="
print "Copy new file contents with replaced placeholders from below here"
print "=================================================================="
properties = [value.strip() for value in params.text.split("\n")]
rep = thisCi._delegate
for prop in properties:
    if  prop.find("#") !=0 and len(prop) != 0:
        keyVal = prop.partition("=")
        rep.entries[keyVal[0]] = keyVal[2]
        print keyVal[0] + "={{" + keyVal[0] + "}}"
    else:
        print prop
repositoryService.update(thisCi.id,thisCi)
