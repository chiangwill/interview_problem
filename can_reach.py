'''
Given an origin airport, destination airport, and series of flights determine whether it is possible for a package at the origin to reach the destination. A flight is represented as departure airport, arrival airport, departure time, and arrival time.
During the transportation, the time that the package leaves the airport needs to be greater than or equal to the time it arrives at the airport. Please determine whether it is possible for a package transfer from s to t. The package arrived at s at time 0.

E.g. 1
Origin: "NYC"
Destination: "SFO"
Flights: NYC → LAX, Departure: 0, Arrival: 4
LAX - SFO, Departure: 5, Arrival: 7
Output: True

E.g 2
Origin: "NYC" Destination: "SFO"
Flights: NYC →> LAX, Departure: 0, Arrival: 4
LAX -> SFO, Departure: 3, Arrival: 5
Output: False
'''


def can_reach(flights, source, target):

    import heapq

    flight_schedule = {}

    # TC: O(n) n is length of flights
    for departure, arrival, departure_time, arrival_time in flights:
        if departure not in flight_schedule:
            flight_schedule[departure] = []

        flight_schedule[departure].append((arrival, departure_time, arrival_time))

    pq = [(0, source)]
    visited = {source: 0}

    while pq:
        reach_time, airport = heapq.heappop(pq)  # TC: O(logn)

        if airport == target:
            return True

        if reach_time > visited.get(airport, float('inf')):
            continue

        if airport in flight_schedule:
            #  TC: O(E) E is numbers of airport
            for arrival, departure_time, arrival_time in flight_schedule[airport]:
                if reach_time <= departure_time:
                    if arrival not in visited or visited[arrival] > arrival_time:
                        visited[arrival] = arrival_time
                        heapq.heappush(pq, (arrival_time, arrival))  # TC: O(logV) V is numbers of flights

    return False


print(can_reach([('NYC', 'TPE', 0, 15), ('TPE', 'SYN', 16, 24)], "NYC", "SYN"))
print(
    can_reach([("JFK", "LAX", 0, 5), ("JFK", "LHR", 1, 8), ("LAX", "SFO", 6, 8), ("LHR", "DXB", 9, 14), ("SFO", "HNL", 10, 14), ("DXB", "SIN", 15, 20), ("HNL", "SYD", 15, 22), ("SIN", "SYD", 21, 24)],
              "JFK", "SYD"))
print(
    can_reach([("JFK", "LAX", 0, 5), ("LAX", "NRT", 6, 14), ("NRT", "PEK", 10, 13), ("JFK", "LHR", 2, 8), ("LHR", "CDG", 9, 10), ("CDG", "IST", 11, 14), ("IST", "DEL", 15, 20), ("DEL", "BKK", 22, 24),
               ("BKK", "PEK", 18, 21)], "JFK", "PEK"))
