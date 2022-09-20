"""
File:  nucleotide_statistics_from_fasta.py

This program  takes in a file and stores the data in two lists
and for each sequence and header. It calculates the number of
A's, T's, G's, C's, and N's(any other nucleotide) in the sequence.
It also calculates the length of the sequence and also
the %GC content of the entire sequence.

Sample command for executing the program:
python3 nucleotide_statistics_from_fasta.py
--infile influenza.fasta --outfile influenza.stats.txt
"""
import argparse
import sys
import re


def main():
    """ Business Logic
    The main function where all other functions are invoked
    """
    args = get_cli_args()
    infile, mode1 = args.infile, 'r'
    outfile, mode2 = args.outfile, 'w'
    fh_in = get_fh(infile, mode1)
    fh_out = get_fh(outfile, mode2)
    list_headers, list_seqs = get_header_and_sequence_lists(fh_in)
    print_sequence_stats(list_headers, list_seqs, fh_out)


def get_fh(infile, mode):
    """
    Takes in two arguements - the input file and the mode -
    opens the file and validates it
    to check if it the correct type of input and opening mode.
    @param infile: Input file to open and read
    @param mode: Specification of the opening mode
    @return: The file handle with the data to be read
    """

    try:
        file_handle = open(infile, mode=mode)
        return file_handle
    except IOError as error:
        print('Unable to open the input file. Please recheck!', infile)
        raise error
    except ValueError as error:
        print('Wrong argument passed for the opening mode', mode)
        raise error


def get_header_and_sequence_lists(fh_in):
    """
    Takes in one argument which is the input file handle, and splits into
    a list of headers and list of sequences.
    @param fh_in: Input file handle
    @return: list of headers, list of sequences
    """
    list_headers = []
    list_seqs = []
    filelines = fh_in.readlines()
    for j, line in enumerate(filelines):
        line = line.rstrip()
        if line.startswith('>'):
            list_headers.append(line)
            j = j + 1
            sequence = ''
            while j < len(filelines) and not filelines[j].startswith('>'):
                sequence += filelines[j].replace("\n", "")
                j += 1
            if sequence != '':
                list_seqs.append(sequence)
            else:
                continue
    return list_headers, list_seqs


def print_sequence_stats(headers_fh, sequence_fh, fh_out):
    """
    Takes in three arguments - header filehandle, sequence filehandle
    and the file to write the output- and calculates the numbers
    of occurences of each of the bases - A, T, C and G- as well as any
    other nucleotides, N. Also calculates the GC% and sequence length.
    @param headers_fh: Header filhandle
    @param sequence_fh: Sequence filehandle
    @param fh_out: File to write the statistics into
    @return: NoneType
    """
    fh_out.write("Number" + "\t" + "Accession" + "\t" + "A's" + "\t" +
                 "G's" + "\t" + "C's" + "\t" +
                 "T's" + "\t" + "N's" + "\t" + "Length" + "\t" "GC%" + "\n")
    sl_number = 0
    for headers, sequence in zip(headers_fh, sequence_fh):
        sl_number += 1
        accession_string = _get_accession(headers)
        a_nt = _get_nt_occurence('A', sequence)
        t_nt = _get_nt_occurence('T', sequence)
        c_nt = _get_nt_occurence('C', sequence)
        g_nt = _get_nt_occurence('G', sequence)
        n_nt = _get_nt_occurence('N', sequence)
        total = a_nt + t_nt + g_nt + c_nt + n_nt
        percentage_gc = ((g_nt + c_nt) / total) * 100
        fh_out.write((str(sl_number) + "\t" + str(accession_string) + "\t" +
                      str(a_nt) +
                      "\t" + str(g_nt) + "\t" + str(c_nt) + "\t"
                      + str(t_nt) + "\t" + str(n_nt) + "\t" + str(total) +
                      "\t" + str(round(percentage_gc, 1)) + "\n"))


def _get_nt_occurence(character, sequence):
    """
    Takes in two arguments - the character of which the occurence is to be
    determined and the sequence- and calculates the number of times each of
    the bases A, T, C, G or N occurs.
    @param character: The base of which the occurence is to be determined
    @param sequence: The sequence from which it is to be determined
    @return: The counts of occurence of each base
    """
    counts = 0
    base = ['A', 'T', 'C', 'G', 'N']
    if character in base:
        for i in sequence:
            if character == i:
                counts += 1
    else:
        sys.exit("Did not code this condition")
    return counts


def _get_accession(header_string):
    """
    Takes in one argument - The header string - an returns the accession number
    of the sequence.
    @param header_string: The header
    @return: The accession number
    """
    accession = header_string.split(' ')
    accession = accession[0]
    accession = re.sub('>', '', accession)
    return accession


def get_cli_args():
    """
    Just get the command line options using argparse
    @return: Instance of argparse arguments
    """
    parser = argparse.ArgumentParser(description='Give the fasta '
                                                 'sequence file name '
                                                 'to do the splitting')
    parser.add_argument('-i', '--infile', dest='infile',
                        type=str, help='Path to the file to open',
                        required=True)
    parser.add_argument('-o', '--outfile', dest='outfile',
                        type=str, help='Path to the file to write',
                        required=True)
    return parser.parse_args()


if __name__ == '__main__':
    main()
