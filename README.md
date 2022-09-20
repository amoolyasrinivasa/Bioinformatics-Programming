# Bioinformatics-Programming

# pdb_fasta_splitter.py
This python program takes in a file and generates two files one for sequence and one for secondary structure sequences and checks the size of list of headers and list of sequences.

### Description
The program which will open this file and generate two files. One which is the protein sequence (pdb_protein.fasta), and the other which is the secondary structures (pdb_ss.fasta). get_fh() gets the file handle to sequences in the fasta file, get_header_and_sequence_lists() stores the header and sequences in two seperate lists, and _check_size_of_lists() checks if the length of sequences and headers are same.

### Getting started
Dependencies
Runs on linux or any other CLI

### Installing
The programs can be found on the programming6200/assignment3 directory on defiance

### Executing programs
$ python3 pdb_fasta_splitter.py --infile ss.txt $ python3 pdb_fasta_splitter.py -h $ python3 pdb_fasta_splitter.py $ python3 pdb_fasta_splitter.py --infile ss_designed2Fail.txt # This file can be downloaded below



### Author
Amoolya Srinivasa
