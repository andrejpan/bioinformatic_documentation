Splitting multi fasta file
==========================

For example if you have [amilaze_multi.fasta](amilaze_multi.fasta) and you want to have separate [*.fasta](https://github.com/andrejpan/bioinformatic_documentation/tree/master/split_multiple_fasta_file/amilaze_aa) files.

Use: python split.py amilaze_multi.fasta

and you will get separate files like they are inside amilaze_aa folder

Splitting multi fasta file to smaller peaces
============================================

For example look 80_slovenia_jame_izolacija.fasta and 80_slovenia_jame_izolacija directory

Use: python multi_split.py80_slovenia_jame_izolacija.fasta output_directory
