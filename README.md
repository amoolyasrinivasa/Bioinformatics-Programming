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

# nucleotide_statistics_from_fasta.py
This python program takes in a file and calculates the number of times the bases A,T,C,G and N occur in the sequence and also calculates the GC% in addition to the length of the sequence.

### Description
The program which will open this file and generate two files. One which is the protein sequence (pdb_protein.fasta), and the other which is the secondary structures (pdb_ss.fasta). 
get_fh() gets the file handle to sequences in the fasta file, get_header_and_sequence_lists() stores the header and sequences in two seperate lists, and _get_nt_occurence() calculates the occurences of the bases, _get_accession() returns the accession number of the header line and print_sequence_stats() prints the statistics into the output file.

### Dependencies

Runs on linux or any other CLI

### Installing

The programs can be found on the programming6200/assignment3 directory on defiance

### Executing programs

$ python3 nucleotide_statistics_from_fasta.py --infile influenza.fasta --outfile influenza.stats.txt
$ python3 nucleotide_statistics_from_fasta.py -h
$ python3 nucleotide_statistics_from_fasta.py 
$ python3 nucleotide_statistics_from_fasta.py --infile influenza.fasta

### my_io.py
Module that has been used in categoris.py, intersection.py and chr21_gene_names.py
This is a python module that contains one function get_fh() which is used in all the three programs above. Anytime a file needs to be opened for reading or writing in your programs in this assignment, the program calls on this module's function get_fh() function. It can be imported using:
  
  from assignment4 import my_io or  from assignment4.my_io import get_fh
The module's get_fh() function can be called by: 
  fh_in = my_io.get_fh(infile1, "r")

# chr21_gene_names.py
This python program takes in the input file containing genes of human chromosome 21. For each gene, the file gives the gene symbol, description and category. The fields are separated by tabs. The program asks the user to enter a gene symbol and then prints the description for that gene based on data from the chr21_genes.txt file. The program gives an error message if the entered symbol is not found in the table.
### Description
The chr21_genes.txt file lists genes from human chromosome 21, in their order along the chromosome. 
The function get_description_dictionary(fh_in) Takes in the input file, reads it and returns a dictionary of descriptions corresponding to each category. 
### Getting started

### Dependencies
Runs on linux or any other CLI

### Installing
The programs can be found on the programming6200/assignment4 directory on defiance

### Executing programs
python3 chr21_gene_names.py -h
python3 chr21_gene_names.py -i chr21_genes.txt

# categories.py
This program counts how many genes are in each category based on data from the chr21_genes.txt file. The program prints the results so that categories are arranged in ascending order to an output file to the output file OUTPUT/categories.txt 

### Description
The chr21_genes.txt file lists genes from human chromosome 21, in their order along the chromosome and the HUGO_genes.txt file lists all human genes having official symbol approved by the HUGO gene nomenclature committee.
The function get_description_dictionary(fh_in) Takes in the input file, reads it and returns a dictionary of descriptions corresponding to each category. 

### Getting started

### Dependencies
Runs on linux or any other CLI

### Author
Amoolya Srinivasa
