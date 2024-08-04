"""
Find the minimum cost to connect all network cables using a heap.
"""

import heapq

def min_cost_to_connect_cables(cables):
    """
    Find the minimum cost to connect all network cables.
    """
    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        combined_length = first + second
        total_cost += combined_length

        heapq.heappush(cables, combined_length)

    return total_cost


def main():
    """
    Main function.
    """
    cable_lengths = [4, 3, 2, 6]
    result = min_cost_to_connect_cables(cable_lengths)
    print(f"The minimum cost to connect all cables is: {result}")

if __name__ == "__main__":
    main()
