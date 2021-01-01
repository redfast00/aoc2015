cities = set()
distances = {}

with open('input') as infile:
    for line in infile:
        first, _, second, _, distance_str = line.strip().split()
        cities.add(first)
        cities.add(second)
        distances[frozenset((first, second))] = int(distance_str)


def tsp(cities_to_do, current_city):
    if not cities_to_do:
        return 0, [current_city]
    min_dist_found = float('inf')
    chosen_path = None
    for city in cities_to_do:
        distance, nextcities = tsp(cities_to_do - {city}, city)
        total_distance = distance + distances[frozenset((city, current_city))]
        if total_distance < min_dist_found:
            min_dist_found = total_distance
            chosen_path = nextcities
    return min_dist_found, [current_city] + chosen_path


def tspstart():
    min_dist_found = float('inf')
    chosen_path = None
    for startcity in cities:
        distance, nextcities = tsp(cities - {startcity}, startcity)
        if distance < min_dist_found:
            min_dist_found = distance
            chosen_path = nextcities
    return min_dist_found, chosen_path


d, _ = tspstart()
print(d)

distances = {k: -v for k, v in distances.items()}
d, _ = tspstart()
print(-d)
