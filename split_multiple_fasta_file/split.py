import sys
# split multiple fasta files(divided with blank lines) in to single separate fasta files

if len(sys.argv) == 1:
    print "Please call: python " + sys.argv[0] + " *.fasta"
    sys.exit(1)

not_open = True
counter = 0

with open(sys.argv[1], 'r') as f:
    for line in f:
        if not_open and  len(line.rstrip('\n')) > 1:
            f = open(sys.argv[1][:-4] + str(counter), "w")
            f.write(line)
            not_open = False
            continue
        if len(line.rstrip('\n')) == 1:
            f.close()
            not_open = True
            counter += 1
            continue
        if len(line.rstrip('\n')) > 1:
            f.write(line)
            continue
        else:
            print "Something is wrong with fasta file"
            f.close()
            sys.exit(1)
f.close()
