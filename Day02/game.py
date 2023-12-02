import re

cubeLimits = {
    "red": 12,
    "green": 13,
    "blue": 14
}

class GameEvaluator:

    def calculatePowers(draws):
        maxCubes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for draw in draws:
            for attr,value in draw['colors'].items():
                if maxCubes[attr] < value:
                    maxCubes[attr] = value 

        result = 1
        for attr,value in maxCubes.items():
            result = result * value

        return result

    def isGamePossibleWithLimits(colours):
        for attr,value in colours.items():
            if value > cubeLimits[attr]:
                return False
        
        return True

    def parseAndCountColours(draw):
        colours = draw.split(',')
        colourObj = {}

        for colour in colours:
            colourSplit = colour.strip().split(' ')
            colourObj[colourSplit[1]] = int(colourSplit[0])

        return colourObj

    def parseLine(line):
        gameParts = re.split(':', line)
        gameNumber = gameParts[0].strip().split(' ')[1]
        gameDraws = gameParts[1].strip().split(';')
        parsedDraws = []
        for draw in gameDraws:
            drawObj = {}
            colours = GameEvaluator.parseAndCountColours(draw)
            drawObj["colors"] = colours
            drawObj["possible"] = GameEvaluator.isGamePossibleWithLimits(colours)
            parsedDraws.append(drawObj)

        return {
            "game": int(gameNumber),
            "draws": parsedDraws,
            "power": GameEvaluator.calculatePowers(parsedDraws)
        }
        
    def individualDrawsPossible(games):
        possibleGames = []
        for game in games:
            gamePossible = True
            for draw in game['draws']:
                if draw['possible'] == False:
                    gamePossible = False
                    break
            
            if gamePossible == True:
                possibleGames.append(game['game'])
        
        return sum(possibleGames)

    def totalProductsOfCubes(games):
        products = []
        for game in games:
            products.append(game['power'])

        return sum(products)
    
    def runGames():
        games = []
        f = open("puzzleInput.txt", "r")
        for x in f:
            games.append(GameEvaluator.parseLine(x))
        f.close()

        return {
            "sumOfPossibleGames": GameEvaluator.individualDrawsPossible(games),
            "sumOfPowers": GameEvaluator.totalProductsOfCubes(games)
        }

if __name__ == '__main__':
    GameEvaluator.runGames();