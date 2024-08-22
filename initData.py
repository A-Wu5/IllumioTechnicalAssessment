from protocols import protocols

def initMaps(lookupTable):
    """
    Takes an open Lookup-table file object and parses the data into three hashmaps 

    Pre-condition: Lookup Table file object (opened)
    Post-condition: Reads file object and returns a dictionaries
                    (1) Key: Tuple(dstport, protocol), Value: Tag : String
                    (2) Key: Tuple(dstport, protocol), Value: Count : Integer
                    (3) Key: Tag : String, Value : Count : Integer
    """
    tagMap = dict()
    tagCount = dict()
    comboCount = dict()
    for line in lookupTable:
        # Convert str line into a list of elements using ',' as the delimiter
        mapData = line.strip().split(',')
        # Skips line if it is not in valid format
        if len(mapData) != 3:
            continue
        # Split data into appropriate elements
        dstport = mapData[0]
        protocol = mapData[1].upper()
        tag = mapData[2].upper()

        # Initialize dictionaries
        tagMap[(dstport, protocol)] = tag
        comboCount[(dstport, protocol)] = 0
        tagCount[tag] = 0

    return (tagMap, comboCount, tagCount)

def parseLogs(flowLog, tagMap, comboCount, tagCount):
    """
    Updates dictionaries based on flowLog data

    Pre-condition: flowLog file object, dictionary that maps key to tag, dictionary 
    that maps key combinations to the count of the combinations, dictionary that counts
    the frequency of the tags
    Post-condition: tagMap, comboCount map, and tagCount map are updated based on the 
    flowLog file
    """
    for line in flowLog:
        flowData = line.strip().split()

        # dstport is at index 6
        dstport = flowData[6]

        # Protocol is at index 7
        protocolNumber = flowData[7]
        protocol = protocols[protocolNumber]
        key = (dstport, protocol)
        if key in tagMap:
            tag = tagMap[(dstport, protocol)]
            comboCount[(dstport, protocol)] += 1
            tagCount[tag] += 1
        else:
            tagCount["Untagged"] = tagCount.get("Untagged", 0) + 1

def logOutput(outputFile, comboCount, tagCount):
    """
    Takes output file object and writes data from initialized maps to it
    """
    outputFile.write("Tag Counts: \n")
    outputFile.write("Tag,Count \n")
    for k, v in tagCount.items():
        outputFile.write(k + "," + str(v) + "\n")
    outputFile.write("\nPort/Protocol Combination Counts: \n")
    outputFile.write("Port,Protocol,Count \n")
    for k, v in comboCount.items():
        dstPort = k[0]
        protocol = k[1]
        outputFile.write(dstPort + "," + protocol + "," + str(v) + "\n")

