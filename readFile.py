#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/24 10:08
import sys
def processFile(filename):
    '''Open, read, and print a file.'''
    input_file = open(filename, 'r')
    for line in input_file:
        line = line.strip()
        print(line)
    input_file.close()

if __name__ == "__main__":
    processFile(sys.argv[1])