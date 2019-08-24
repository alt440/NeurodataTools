import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
#import seaborn as sns; sns.set()
#import pandas as pd
from mgcpy.independence_tests.mgc import MGC
from mgcpy.benchmarks import simulations as sims

from random import randrange

# so MGC takes two distance matrices: X and Y.
# a distance matrix determines the distance between each data point.For example, say
# we have three points. Numbers indicate distances
# A --9--> B --20--> C
# This would generate this matrix:
#    A   B   C
# A  0   9   29
# B  9   0   20
# C  29  20  0
# A has a distance of 0 with itself. Thats why position (A, A) has a value of 0.
# C has a distance of 29 with A. Thats why position (A, C) and (C, A) have a value of 29.

# the mgc_plot method will return the data points graph, and another weird diagram with colors (firstTestMGC2.png).
# depending on the weird diagram's structure, it will indicate a different relation. You can look
# in relationMGCSuggesting.png and associate your diagram to that of one in the relationMGCSuggesting.png image.

# Multiscale Graph Correlation (Also known as MaGiC) is useful for graphs of many dimensions. This means it is useful
# for some "nuages de points", having multiple Y values for a single X.


def compute_mgc(X, Y):
    mgc = MGC()
    mgc_statistic, independence_test_metadata = mgc.test_statistic(X, Y)
    p_value, metadata = mgc.p_value(X, Y)

    # mgc_statistic determines the correlation between the variables.
    # so, if the variable is closer to -1 or 1, and not extremely close to
    # 0, then there might be a correlation. If the p-value (the uncertainty,
    # from the way I see it) is lower than 0.05 or 5%, then there might be a
    # correlation. Make sure you are running the unbiased version of the method,
    # otherwise you might be lead to false results.
    print("MGC test statistic:", mgc_statistic)
    print("P Value:", p_value)
    #print("Optimal Scale:", independence_test_metadata["optimal_scale"])
    return mgc_statistic, p_value, independence_test_metadata


def mgc_plot(X, Y, simulation_name, name_data_points, name_graph, only_viz=False, only_mgc=False):
    # plt.clf()

    if not only_mgc:
        # simulation
        fig = plt.figure(figsize=(8, 8))
        plt.title(simulation_name + " Simulation", fontsize=17)
        plt.scatter(X[:, 0], Y[:, 0])
        plt.xlabel('X', fontsize=15)
        plt.ylabel('Y', fontsize=15)
        plt.axis('equal')
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)
        plt.savefig(name_data_points, bbox_inches='tight')

    if not only_viz:
        # run MGC
        mgc_statistic, p_value, independence_test_metadata = compute_mgc(X, Y)

        # local correlation map
        fig = plt.figure(figsize=(8, 8))
        local_corr = independence_test_metadata["local_correlation_matrix"]

        # define two rows for subplots
        ax = plt.gca()

        # draw heatmap
        plt.title("Local Correlation Map", fontsize=17)
        im = ax.imshow(local_corr, cmap='YlGnBu')

        # colorbar
        cbar = ax.figure.colorbar(im, ax=ax)
        cbar.ax.set_ylabel("", rotation=-90, va="bottom")
        # fig.colorbar(ax.get_children()[0], cax=cax, orientation="vertical")
        ax.invert_yaxis()

        # Turn spines off and create white grid.
        for edge, spine in ax.spines.items():
            spine.set_visible(False)

        # optimal scale
        optimal_scale = independence_test_metadata["optimal_scale"]
        ax.scatter(optimal_scale[0], optimal_scale[1], marker='X', s=200, color='red')

        # other formatting
        ax.tick_params(bottom="off", left="off")
        ax.set_xlabel('#Neighbors for X', fontsize=15)
        ax.set_ylabel('#Neighbors for Y', fontsize=15)
        ax.set_xlim(0, 60)
        ax.set_ylim(0, 60)

        plt.savefig(name_graph, bbox_inches='tight')


# here I generate some random X and Y values (1D graph: only one Y for each X)
x, y = sims.linear_sim(num_samp=100, num_dim=1, noise=0.1)

mgc_plot(x, y, "MGC Test", "firstTestMGC.png", "firstTestMGC2.png")
