import sys
import pstats
from pstats import SortKey

p = pstats.Stats(sys.argv[1])
p.strip_dirs().sort_stats(SortKey.TIME).print_stats(100)