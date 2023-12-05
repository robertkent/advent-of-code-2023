import re

class Almanac:
    def __init__(self, fileName: str, partTwo = False) -> None:
        self.input = self.getInput(fileName)
        self.partTwo = partTwo
        self.seeds = self.getSeeds()
        self.types = {
            'seedToSoil': self.getMap('seed-to-soil'),
            'soilToFertilizer': self.getMap('soil-to-fertilizer'),
            'fertilizerToWater': self.getMap('fertilizer-to-water'),
            'waterToLight': self.getMap('water-to-light'),
            'lightToTemperature': self.getMap('light-to-temperature'),
            'temperatureToHumidity': self.getMap('temperature-to-humidity'),
            'humidityToLocation': self.getMap('humidity-to-location'),
        }

    def getInput(self, fileName):
        input = []
        f = open(fileName, 'r')
        for x in f:
            input.append(x)
        f.close()

        return input
    
    def getSeeds(self):
        seeds = []
        for row in self.input:
            if 'seeds:' in row:
                seeds = list(map(int, row.split(':')[1].strip().split(' ')))
                break

        if self.partTwo:
            start = 0
            end = len(seeds)
            step = 2
            seedChunks = []
            for i in range(start, end, step): 
                x = i
                seedChunks.append(seeds[x:x+step])
            seeds = seedChunks
        
        return list(map(self.mapToObj, seeds))
    
    def mapToObj(self, seed):
        if isinstance(seed, list):
            return {
                "min": seed[0],
                "max": seed[0] + seed[1]
            }

        return {
            "min": seed,
            "max": seed
        }
            
    def getItemFromRange(self, items: str, match, isSeed = False):
        for item in self.types[items]:
            destinationRangeStart, sourceRangeStart, rangeLength = item

            if isSeed and isinstance(match, dict):
                match = match['min']
            else:
                if sourceRangeStart <= match <= sourceRangeStart + rangeLength:
                    return destinationRangeStart + (match - sourceRangeStart)

        return match

    def getItemFromRangeReversed(self, items: str, match):
        for item in self.types[items]:
            destinationRangeStart, sourceRangeStart, rangeLength = item
            if destinationRangeStart <= match <= destinationRangeStart + rangeLength:
                return sourceRangeStart + (match - destinationRangeStart)

        return match

    def getDataFromSeed(self, seed, dataType):
        lastItem = False
        for index, x in enumerate(self.types):
            if not lastItem == False:
                lastItem = self.getItemFromRange(x, lastItem)
            else:
                lastItem = self.getItemFromRange(x, seed, True)

            if dataType == x:
                return lastItem
            
    def getSeedFromLocation(self, seed, dataType):
        lastItem = False
        for index, x in enumerate(reversed(self.types)):
            if not lastItem == False:
                lastItem = self.getItemFromRangeReversed(x, lastItem)
            else:
                lastItem = self.getItemFromRangeReversed(x, seed)

            if dataType == x:
                return lastItem
            
    def getLowestLocationFromValidSeed(self):
        # 4917125 - WHYYY
        currentLocation = 0
        while currentLocation < 999999999:
            soil = self.getSeedFromLocation(currentLocation, 'seedToSoil')
            if self.isValidSeed(soil):
                return currentLocation
            currentLocation += 1
            
    def isValidSeed(self, s):
        for seed in self.seeds:
            if s in range(seed['min'], seed['max']):
                return True
    
    def getLowestLocationNumberFromSeeds(self, seeds):
        locations = []
        for seed in seeds:
            locations.append(self.getDataFromSeed(seed, 'humidityToLocation'))

        return min(locations)
    
    def getLowestLocationNumber(self):
        if self.partTwo:
            location = self.getLowestLocationFromValidSeed()
            return location
        
        location = self.getLowestLocationNumberFromSeeds(self.seeds)
        return location
            
    def getMap(self, match: str):
        getNums = False
        numbers = []
        for row in self.input:
            if match in row:
                getNums = True
                continue
            if getNums:
                n = re.findall(r'\d+', row)
                if n:
                    numbers.append(list(map(int, n)))
                else:
                    break

        return numbers
    

if __name__ == '__main__':
    print(Almanac('puzzleInput.txt', True).getLowestLocationNumber())