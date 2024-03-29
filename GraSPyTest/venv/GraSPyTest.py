
import numpy as np
from graspy.datasets import load_drosophila_right
from graspy.plot import heatmap
from graspy.utils import binarize, symmetrize
from graspy.models import EREstimator
from graspy.models import DCEREstimator
from graspy.models import SBMEstimator
from graspy.models import DCSBMEstimator
from graspy.models import RDPGEstimator
import matplotlib.pyplot as plt
# % matplotlib inline --> to counter, just add plt.savefig after the heatmaps to display.

# Essentially, all you need to do here is to have an adjacency matrix describing your nodes and their relations.
# With only that, you can design all the graphs you want, except RDPG because it uses some latent positions (see notes),
# and that can only be generated by ASE.

adj, labels = load_drosophila_right(return_labels=True)
# makes the adjacency matrix contain only 0 and 1 as float values
adj = binarize(adj)

info = heatmap(adj,
        inner_hier_labels=labels,
        title='Drosophila right MB',
        font_scale=1.5,
        sort_nodes=True);

plt.savefig("DrosophilaRightMB", bbox_inches='tight')

er = EREstimator(directed=True,loops=False)
er.fit(adj)
print(f"ER \"p\" parameter: {er.p_}")
heatmap(er.p_mat_,
        inner_hier_labels=labels,
        font_scale=1.5,
        title="ER probability matrix",
        vmin=0, vmax=1,
        sort_nodes=True)

plt.savefig("ERProbabilityMatrix", bbox_inches='tight')

heatmap(er.sample()[0],
        inner_hier_labels=labels,
        font_scale=1.5,
        title="ER sample",
        sort_nodes=True);

plt.savefig("ERSample", bbox_inches='tight')

dcer = DCEREstimator(directed=True,loops=False)
dcer.fit(adj)
print(f"DCER \"p\" parameter: {dcer.p_}")
heatmap(dcer.p_mat_,
        inner_hier_labels=labels,
        vmin=0,
        vmax=1,
        font_scale=1.5,
        title="DCER probability matrix",
        sort_nodes=True)

plt.savefig("DCERProbabilityMatrix", bbox_inches='tight')

heatmap(dcer.sample()[0],
        inner_hier_labels=labels,
        font_scale=1.5,
        title="DCER sample",
        sort_nodes=True)

plt.savefig("DCERSample", bbox_inches='tight')

sbme = SBMEstimator(directed=True,loops=False)
sbme.fit(adj, y=labels)
print("SBM \"B\" matrix:")
print(sbme.block_p_)
heatmap(sbme.p_mat_,
        inner_hier_labels=labels,
        vmin=0,
        vmax=1,
        font_scale=1.5,
        title="SBM probability matrix",
        sort_nodes=True)

plt.savefig("SBMProbabilityMatrix", bbox_inches='tight')

heatmap(sbme.sample()[0],
        inner_hier_labels=labels,
        font_scale=1.5,
        title="SBM sample",
        sort_nodes=True)

plt.savefig("SBMSample", bbox_inches='tight')

dcsbme = DCSBMEstimator(directed=True,loops=False)
dcsbme.fit(adj, y=labels)
print("DCSBM \"B\" matrix:")
print(dcsbme.block_p_)
heatmap(dcsbme.p_mat_,
        inner_hier_labels=labels,
        font_scale=1.5,
        title="DCSBM probability matrix",
        vmin=0,
        vmax=1,
        sort_nodes=True)

plt.savefig("DCSBMProbabilityMatrix", bbox_inches='tight')

heatmap(dcsbme.sample()[0],
        inner_hier_labels=labels,
        title="DCSBM sample",
        font_scale=1.5,
        sort_nodes=True)

plt.savefig("DCSBMSample", bbox_inches='tight')

rdpge = RDPGEstimator(loops=False)
rdpge.fit(adj, y=labels)
heatmap(rdpge.p_mat_,
        inner_hier_labels=labels,
        vmin=0,
        vmax=1,
        font_scale=1.5,
        title="RDPG probability matrix",
        sort_nodes=True
       )

plt.savefig("RDPGProbabilityMatrix", bbox_inches='tight')

heatmap(rdpge.sample()[0],
        inner_hier_labels=labels,
        font_scale=1.5,
        title="RDPG sample",
        sort_nodes=True)

plt.savefig("RDPGSample", bbox_inches='tight')