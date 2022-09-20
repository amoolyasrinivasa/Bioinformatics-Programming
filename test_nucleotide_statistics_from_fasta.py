import pytest
list_headers = [">EU521893 A/Arequipa/FLU3833/2006 2006// 4 (HA)"]
list_seqs =["AACAGCACGG"]
from nucleotide_statistics_from_fasta import get_fh, _get_accession, _get_nt_occurence, print_sequence_stats

def test_get_fh():
    with pytest.raises(IOError):
        get_fh("does_not_exist.txt", "r")

def test__get_accession():
    assert _get_accession(list_headers[0]) == "EU521893"

def test__get_nt_occurence():
    assert _get_nt_occurence('A', list_seqs[0]) == 4





