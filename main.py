from initData import *

if __name__ == "__main__":
    try:
        lookupFile = "./LookupTables/testLookup.csv"
        logFile = "./FlowLogs/testInput.txt"
        
        lookupTable = open(lookupFile, "r")
        flowLog = open(logFile, "r")
        print("Files opened successfully")

        # Initialize dictionaries with the lookup table values
        tagMap, comboCount, tagCount = initMaps(lookupTable)
        # Update dictionaries with the flowlog data
        parseLogs(flowLog, tagMap, comboCount, tagCount)

        output = open("./output.txt", "w")
        logOutput(output, comboCount, tagCount)

        # print("------TagMap-----")
        # for t in tagMap:
        #     print(t, tagMap[t])
        # print("-----comboCount-----")
        # for c in comboCount:
        #     print(c, comboCount[c])
        # print("-----tagCount-----")
        # for tc in tagCount:
        #     print(tc, tagCount[tc])

        output.close()
        lookupTable.close()
        flowLog.close()
    except Exception as e:
        print("Error")
        print(e)

    
        