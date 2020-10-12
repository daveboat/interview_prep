import math

# given a list of N (x, y) points, find clusters of points, where a cluster is a set of points where all points are at
# least a distance k apart from another point in the set

# let's assume the points, and k, are normalized so that they are between 0 and 1 (this is always possible by dividing
# both x, y and k by the largest single value, x or y, in the original points list, so we can assume this without loss
# of generality)

# the brute force method is to start with an arbitrary point (seed point), remove that from the unassigned group, and
# add it to the first cluster group, then check the rest of the points for k-nearness to that point, removing from
# unassigned, adding to current cluster group. Repeat for each new point added to the cluster group, and then repeat the
# whole process for the next seed point, until no more seed points are available.

# we'll also assume there are no exactly identical points in the unassigned list

# can we improve this algorithm, which is O(N^2) time complexity and O(N) in space complexity?

# for an algorithm that's more efficient, perhaps, if the points are dense and evenly distributed, and k is "relatively
# large", we could divide the space into k by k squares, and pre-sort the points into one of the squares. Everything in
# the same square must be a cluster by definition, so you start with N^2/k^2 seed clusters, and then you check points
# for k-nearness between points in adjacent clusters. As soon as one pair is k-near, both clusters can be joined

# other checks we could so is to see if the points have some kind of structure, e.g. PCA to see if most of the variation
# is along a single axis. If so, we could approximate this process by only using the axis with most variation

# even further, if you knew something about the points, like they were definitely in a number of discrete clusters, you
# could first run k-means or something to find the clusters


def euclidian_distance(p1, p2, k):
    # a helper function to check if the euclidian distance for two tuples is less than k
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) < k


# first, let's generate a list of tuples, and define our k
p_ = [(0.1, 0.1), (0.15, 0.1), (0.1, 0.15), (0.9, 0.9), (0.8, 0.9), (0.9, 0.8)]
k_ = 0.25

# next, let's write our function to do the clustering
def cluster(unassigned_points, k):
    # create our list of point groups
    point_groups = [[]]
    point_group_index = 0

    # iterate through the points backwards by popping seed points
    while len(unassigned_points) > 0:
        p = unassigned_points.pop()
        checked_points_index = 0
        # add the current point to the current point group, and remove it from the unassigned points
        point_groups[point_group_index].append(p)

        # now, iterate through the unassigned points and add all points with distance to p less than k, while removing
        # them from the unassigned points group
        while checked_points_index < len(point_groups[point_group_index]):
            if len(unassigned_points) == 0:
                break

            for pp in reversed(unassigned_points):
                if euclidian_distance(point_groups[point_group_index][checked_points_index], pp, k):
                    point_groups[point_group_index].append(pp)
                    unassigned_points.remove(pp)

            checked_points_index += 1

        if len(unassigned_points) == 0:
            break

        point_groups.append([])
        point_group_index += 1

    return point_groups

# run our algorithm!
print(cluster(p_, k_))