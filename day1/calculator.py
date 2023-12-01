import re
f = open("puzzleInput.txt", "r")
fo = open("puzzleOutput.txt", "w")
numWords = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
regEx = r'(\d+)|(?=(' + '|'.join(numWords) + '))'

print(regEx);

def reformatNumbers(nums):
    newNumbers = []
    for x in nums:
        if x in numWords:
            newNumbers.append(str(numWords.index(x) + 1))
        else:
            newNumbers.append(x)
    
    return newNumbers

def getCalibration():
    calibrationNumbers = []
    for index, x in enumerate(f):
        nums = re.findall(regEx, x, re.DOTALL)
        result = [match[0] or match[1] for match in nums if any(match)]
        reformattedNumbers = reformatNumbers(result)
        numString = ''.join(reformattedNumbers)
        calibration = numString[0] + numString[-1]
        calibrationNumbers.append(int(calibration))
        fo.write(f'{x}={calibration}\n')

    return sum(calibrationNumbers)

print(getCalibration())

f.close()
fo.close()