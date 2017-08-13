#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 16:35:57 2014

@author: Stuart Maitland
"""
from Bio import SeqIO
import re
import binascii

def dnatoascii(location):
    """Creates a .txt file of any text represented by a DNA sequence FASTA file
    where A/C=1 and G/T =0.
    location - string - path to DNA file"""
    # import dependencies

    record = SeqIO.read(location, "fasta")  # convert FASTA file to Seq object

    ascstring = str(record.seq) + str(record.seq.reverse_complement())
    ascstring = re.sub('[AC]', '0', ascstring)
    ascstring = re.sub('[TG]', '1', ascstring)  # substitute characters of DNA with binary

    f = open('myfile.txt', 'w')
    for frame in range(8):  # for each possible reading frame in ASCII
        # convert the length of binary that is a multiple of 8 into binary integer.
        binint = int(ascstring[frame:(len(ascstring) - (8 - frame))], 2)
        translated = binascii.unhexlify('%x' % binint)  # convert to hexadecimal string
        f.write(translated)
    f.close()


# Example use case

dnalocation = "id100228968.seq"  # Input DNA sequence
dnatoascii(dnalocation)