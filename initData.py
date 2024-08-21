"""
Pre-condition: Lookup Table file object (opened)
Post-condition: Reads file object and returns a dictionaries
                (1) Key: Tuple(dstport, protocol), Value: Tag : String
                (2) Key: Tuple(dstport, protocol), Value: Count : Integer
                (3) Key: Tag : String, Value : Count : Integer
"""
def initMaps(lookupTable):
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
        dstport = mapData[0].lower()
        protocol = mapData[1].lower()
        tag = mapData[2]

        # Initialize dictionaries
        tagMap[(dstport, protocol)] = tag
        comboCount[(dstport, protocol)] = 0
        tagCount[tag] = 0

    return (tagMap, comboCount, tagCount)