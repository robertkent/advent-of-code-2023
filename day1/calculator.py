import re

f = open("puzzleInput.txt", "r")
numWords = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
regEx = r'(\d+)|(?=(' + '|'.join(numWords) + '))'

class Calculate: 

    def reformatNumbers(nums):
        newNumbers = []
        for x in nums:
            newNumbers.append(str(numWords.index(x) + 1)) if x in numWords else newNumbers.append(x)
        
        return newNumbers

    def getCalibration(line):
        nums = re.findall(regEx, line)
        result = [match[0] or match[1] for match in nums if any(match)]
        numString = ''.join(Calculate.reformatNumbers(result))
        calibration = numString[0] + numString[-1]
        return int(calibration)

    def getCalibrationForAll():
        calibrationNumbers = []
        for x in f:
            calibrationNumbers.append(Calculate.getCalibration(x))

        return sum(calibrationNumbers)
    
    def printCalibration():
        print(Calculate.getCalibrationForAll())
        f.close()

if __name__ == '__main__':
    Calculate.printCalibration()