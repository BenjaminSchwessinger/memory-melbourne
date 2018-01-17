#!/usr/bin/python3
import sys
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
plt.style.use('ggplot')
matplotlib.rcParams['font.size'] = 12


plt.figure(figsize=(8.5, 7.5))
plts = []
for fname in sys.argv[1:]:
    labels, bads, goods = [], [], []
    with open(fname, 'r') as fh:
        for line in fh:
            label, bad, good = line.split()
            bads.append(float(bad))
            goods.append(float(good))
            labels.append(label)

    #p1, = plt.plot(range(len(bads)), bads, 'o')
    p, = plt.plot(range(len(bads)), np.divide(bads, goods), 'o')
    plts.append(p)
    #p2, = plt.plot(range(len(goods)), goods, 'o')

counts = []
for fname in sys.argv[1:]:
    _, count, _ = fname.split('_')
    counts.append(int(count))

plt.ylabel('slowdown')
plt.xlabel('size')
plt.xticks(range(len(bads)), labels, rotation=60)
# draw caches
miny, maxy = min(np.divide(bads, goods)), max(np.divide(bads, goods))
# L1
l1 = labels.index('64K')
plt.plot((l1, l1), (miny, maxy), color='darkblue', alpha=0.4)
plt.text(l1-1, (miny+maxy)/2, 'L1\n⟵', color='darkblue', verticalalignment='top')
# L2
l1 = labels.index('512K')
plt.plot((l1, l1), (miny, maxy), color='darkblue', alpha=0.4)
plt.text(l1-1, (miny+maxy)/2, 'L2\n⟵', color='darkblue', verticalalignment='top')
# L3
l1 = labels.index('4M')
plt.plot((l1-0.5, l1-0.5), (miny, maxy), color='darkblue', alpha=0.4)
plt.text(l1-1.5, (miny+maxy)/2, 'L3\n⟵', color='darkblue', verticalalignment='top')

plt.show()
