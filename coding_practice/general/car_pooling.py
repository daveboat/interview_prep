"""
LC1094 - Car pooling

You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives
east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th
trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The
locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips.

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false

Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true

Example 3:

Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true

Example 4:

Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output: true

Constraints:

    trips.length <= 1000
    trips[i].length == 3
    1 <= trips[i][0] <= 100
    0 <= trips[i][1] < trips[i][2] <= 1000
    1 <= capacity <= 100000
"""


class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        # I don't think we can get around doing this in O(N). let's sort by start location, then end location, and
        # keep track of previous end locations while going through the list

        # sort trips
        trips.sort(key=lambda x: (x[1], x[2]))

        # our data structure for holding previous end locations and how many passengers get off there
        dropoffs = []  # list of [dropoff location, # of passengers to drop off]
        i = 0  # index for dropoffs

        # number of passengers
        passengers = 0

        # main loop
        for trip in trips:
            # drop people off whose dropoff location is less than the current starting location
            for i in range(len(dropoffs)):
                if dropoffs[i][0] <= trip[1]:
                    passengers -= dropoffs[i][1]
                    dropoffs[i][1] = 0

            # process the current pickup
            passengers += trip[0]
            if passengers > capacity: return False

            # the current dropoff needs to be inserted in order
            dropoffs.append([trip[2], trip[0]])

        return True
