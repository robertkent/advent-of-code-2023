import re
f = open("puzzleInput.txt", "r")
numWords = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
regEx = r'(\d+)|(?=(' + '|'.join(numWords) + '))'

def reformatNumbers(nums):
    newNumbers = []
    for x in nums:
        newNumbers.append(str(numWords.index(x) + 1)) if x in numWords else newNumbers.append(x)
    
    return newNumbers

def getCalibration():
    calibrationNumbers = []
    for x in f:
        nums = re.findall(regEx, x)
        result = [match[0] or match[1] for match in nums if any(match)]
        numString = ''.join(reformatNumbers(result))
        calibration = numString[0] + numString[-1]
        calibrationNumbers.append(int(calibration))

    return sum(calibrationNumbers)

print(getCalibration())

f.close()