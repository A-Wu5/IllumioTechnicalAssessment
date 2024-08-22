# Illumio Technical Assessment

## Assumptions

- Input file and tag mappings file are plain text (ascii)
- Flow log file size is up to 10 MB
- Lookup file can have up to 10000 mappings
- Tags can map to more than one port, protocol combinations
- Matches are case insensitive

- Flow log is in default log format and version 2
- Lookup table rows will always be in the correct `dstport,protocol,tag` format and in that order only
- Protocol numbers in flow log range from 0-143

## How to run this program

- After downloading the files you can add/replace the flow log file in the 'FlowLogs' folder or the lookup table file in the 'LookupTables' folder
- Update 'lookupFile' and 'logFile' on lines 5 and 6 and make sure the paths are set correctly
- Run the program by going to the location of main.py and typing `python3 main.py` in the terminal
- The program should generate or update 'output.txt' with the count of matches or output an error message if an error occurred.

## Analysis

The time complexities of all the functions in `initData.py` are all linear O(n), since the functions go through each lines n once and performs O(1) operations on them.

The space complexity is also linear O(m + k), since at most the program stores all of the combination pairs m and tags k once in each program start.

## Testing

This program was tested using different FlowLog files and Lookup table files for different cases.
Edge cases:

1. Empty flowLog file and empty lookup table file:
   a. The output file would only contain 'Tag Counts:', the tag formatting, 'Port/Protocol Combination Counts:', and combination formatting. There would be no data in the output file.
2. Empty table lookup file:
   a. Each line in the flow log file would be labeled as untagged
3. Empty flowlog file:
   a. All the tag counts are 0
4. Flowlog contains version 3 data:
   a. The program skips over data that is not version 2
5. Flow log is not in default formatting:
   a. The program outputs an error
