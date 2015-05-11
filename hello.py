# file location: 
# Copyright notation:
# License notation:
# Author: Douglas Hagerman 

""" This is a rough starting point for processing transit files.
    
    Run this program from the command line like this:
    $python3 hello.py stopsShortened.txt

    Output is:
    Main
    Program arguments: ['hello.py', 'stopsShortened.txt']
    followed by a list of latitudes, longitudes, and stop names
"""

import sys
import re
#import /Users/douglashagerman/Library/Python/2.7/lib/python/site-packages/transitfeed


# Main function that prints header and loops through list of bus stops.
def main():

  print ('Main')
  print ('Program arguments:', sys.argv)

  file_name = sys.argv[1]
  fp = open(file_name)
  for line in fp:
    
    lat, b, c, lon, e, f, g, h, stopname, j, k = line.split (',')
    print (lat, lon, stopname)

    # Process the info from the line
    # ...
    
  fp.close()


# Call the main() function.
if __name__ == '__main__':
  main()
