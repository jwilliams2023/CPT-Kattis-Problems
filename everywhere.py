test_cases = int(input())

for _ in range(test_cases):
    cities = set()
    num_cities = int(input())

    for _ in range(num_cities):
        cities.add(input())

    print(len(cities))