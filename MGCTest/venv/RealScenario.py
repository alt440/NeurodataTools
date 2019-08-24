from random import randrange
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from mgcpy.independence_tests.mgc import MGC

# in this case, I will create multiple data points
x = []
y = []

# my number of data points
dataPoints = 100
maxIntVal = 1000
# you can read some data from a file from here, but I will go at random.
for i in range(dataPoints):
    x.append(randrange(maxIntVal)*1.0)
    y.append(randrange(maxIntVal)*1.0)

# now that you have your graph, you must make the X and Y distance matrices.
# the meaning of a distance matrix is explained in the FirstTestMGC.py file.
def designDistanceMatrix(list):
    # distance matrix is list.length by list.length
    distanceMatrix = [[0.0 for y in range(len(list))] for x in range(len(list))]

    # this is the slowest way. Could use symmetry to just replicate the data from one side to the other
    for i in range(len(list)):
        for j in range(len(list)):
            distanceMatrix[i][j] = list[i] - list[j]
            if distanceMatrix[i][j] < 0:
                distanceMatrix[i][j] *= -1

    return distanceMatrix


distanceMatrixX = designDistanceMatrix(x)
distanceMatrixY = designDistanceMatrix(y)


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


def mgc_plot(X, Y, dataX, dataY, simulation_name, name_data_points, name_graph, only_viz=False, only_mgc=False):
    # plt.clf()

    if not only_mgc:
        # simulation
        fig = plt.figure(figsize=(8, 8))
        plt.title(simulation_name + " Simulation", fontsize=17)
        plt.scatter(dataX, dataY)
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


mgc_plot(np.array(distanceMatrixX), np.array(distanceMatrixY), x, y, "Real Scenario", "realScenario.png", "realScenario2.png")
