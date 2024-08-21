from initData import *

if __name__ == "__main__":
    # print("Enter flow log file name: ")
    # fileName = input()

    lookupTable = open("./LookupTables/testLookup.csv", "r")
    flowLog = open("./FlowLogs/testinput.txt", "r")
    
    tagMap, comboCount, tagCount = initMaps(lookupTable)

    lookupTable.close()
    flowLog.close()