def solution(cacheSize, cities):
    hit = 1
    miss = 5
    answer = 0
    cities = [city.lower() for city in cities]
    cache = [0] * cacheSize
    for city in cities:
        if city in cache:
            answer += hit
            cache.remove(city)
        else:
            answer += miss
        cache.append(city)
        if len(cache) > cacheSize:
            cache.pop(0)
    return answer


if __name__ == "__main__":
    print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
