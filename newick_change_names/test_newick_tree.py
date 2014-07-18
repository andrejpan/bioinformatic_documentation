import sys
from Bio import Phylo

if len(sys.argv) == 2:
    #open newick tree
    try:
        nwk_file = open(sys.argv[1])
    except IOError:
        print 'cannot open:', sys.argv[1]
        sys.exit(1)

else:
    print "Please use this script: python " + sys.argv[0] + " *.nwk"
    sys.exit(1)

tree = Phylo.read(sys.argv[1], "newick")
tree.rooted = True
Phylo.draw(tree)

print "This tree is ok!"
