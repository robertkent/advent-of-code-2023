import re
from itertools import groupby

class Schematic:
    def __init__(self, text: str, gearSymbol = False):
        self.text = text
        self.gearSymbol = gearSymbol
        self.data = []
        self.symbols = []
        self.numbers = []
        self.parts = []
        self.symbolCoords = []
        self.partNumbers = []
        self.setup()
        self.doSumOfPartNumbers()

    def doSumOfPartNumbers(self):
        return sum(self.partNumbers)
    
    def doSumOfGears(self):
        gears = []
        for part in self.parts:
            row,col = part[1]
            if self.data[row][col] == '*':
                gears.append(part)

        prods = {}

        for partNumber, symbolCoord in gears:
            if symbolCoord in prods:
                prods[symbolCoord] *= partNumber
            else:
                prods[symbolCoord] = partNumber

        filtered = {symbol: product for symbol, product in prods.items() if list(map(lambda x: x[1], gears)).count(symbol) > 1}
        result = [[prods[coords], coords] for coords in filtered]

        sum = 0
        for res in result:
            sum += res[0]

        return sum
            

    def setup(self):
        self.getAllData()
        self.extractSymbols() 
        self.getFullNumbersFromCoords()

    def createElementsWithBoundaries(self):

        neighbors = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        numbersThatAreAdjacent = []
        
        for row in range(len(self.data)):
            for col in range(len(self.data[0])):
                if self.data[row][col].isdigit():
                    for dr, dc in neighbors:
                        r, c = row + dr, col + dc
                        if 0 <= r < len(self.data) and 0 <= c < len(self.data[0]) and self.data[r][c] in self.symbols:                            
                            idx = col
                            idxCount = -1
                            checkForTuples = []
                            while idx >= 0 and self.data[row][idx].isdigit():
                                idxCount += 1
                                idx -= 1
                                checkForTuples.append((row, col - idxCount))

                            if len(set(numbersThatAreAdjacent).intersection(set(checkForTuples))) == 0:
                                numbersThatAreAdjacent.append((row,col))
                                self.parts.append([(row,col), (r,c)])

        return numbersThatAreAdjacent        
        

    def getFullNumbersFromCoords(self):
        coords = self.createElementsWithBoundaries()
        numbers = []
        i = 0
        for row, col in coords:
            rowData = self.data[row]

            result = ""
            idx = col

            while idx >= 0 and rowData[idx].isdigit():
                result = rowData[idx] + result
                idx -= 1

            idx = col + 1

            while idx < len(rowData) and rowData[idx].isdigit():
                result += rowData[idx]
                idx += 1

            numbers.append(int(result))

            self.parts[i][0] = int(result)
            i += 1

        self.partNumbers = numbers

    def extractNumbers(self):
        self.numbers = re.findall(r'\d+', self.text)

    def extractSymbols(self):
        self.symbols = set(re.findall(r'[^0-9.\n]', self.text))

    def getAllData(self):
        self.data = self.text.split('\n')
    

