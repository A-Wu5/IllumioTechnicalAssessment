from initData import *

if __name__ == "__main__":
    try:
        lookupFile = "./LookupTables/testLookup.csv"
        logFile = "./FlowLogs/testInput.txt"
        
        lookupTable = open(lookupFile, "r")
        flowLog = open(logFile, "r")
    
        print("Files opened successfully")
        tagMap, comboCount, tagCount = initMaps(lookupTable)

        lookupTable.close()
        flowLog.close()
    except Exception as e:
        print(e)

    
        