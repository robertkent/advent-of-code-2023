from schematic import Schematic

class Engine:
    def sumOfPartNumbers(schematic: Schematic):
        return schematic.doSumOfPartNumbers()
    
    
    def sumOfGears(schematic: Schematic):
        return schematic.doSumOfGears()

    def doCompleteSumOfParts():
        f = open('puzzleInput.txt', 'r')
        input = ""
        for x in f:
            input += x
        calculation = Engine.sumOfPartNumbers(Schematic(input))
        print(calculation)
        f.close()

    def doCompleteSumOfGears():
        f = open('puzzleInput.txt', 'r')
        input = ""
        for x in f:
            input += x
        calculation = Engine.sumOfGears(Schematic(input))
        print(f"Sum of gears: {calculation}")
        f.close()

if __name__ == '__main__':
    Engine.doCompleteSumOfParts()
    Engine.doCompleteSumOfGears()