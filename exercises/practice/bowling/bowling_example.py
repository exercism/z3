from z3 import*

def bowlingScore(pins_per_roll):
    numOfRolls = len(pins_per_roll)
    score = 0
    lastStrikeRoll = 99 #Initialize to a high variable that it'll never reach
    firstThrowInFrame = True
    previousFrameSpare = False

    s = Solver()
    totalScore = Real('score')

    for i in range(numOfRolls):
        if (pins_per_roll[i] == 10):
            if (firstThrowInFrame): #Strike
                score = score + 10

                if ((lastStrikeRoll == (i-1)) and notTenthFrame(i, numOfRolls)):
                    score = score + 10

                    if (pins_per_roll[i-2] == 10): #Multiple strikes back to back
                        score = score + 10

                lastStrikeRoll = i
                
            else: #Spare
                score = score + pins_per_roll[i]
                previousFrameSpare = True

                if (lastStrikeRoll == (i-2) and (i != numOfRolls-1)):   #Spare after a strike
                    score = score + 10

            firstThrowInFrame = True #Goes to first throw in next frame

        else:
            if (previousFrameSpare):
                if (i != numOfRolls-1):
                    score = score + pins_per_roll[i]
                    previousFrameSpare = False  #Only add number the first roll of the frame

            elif ((lastStrikeRoll == (i-1)) or (lastStrikeRoll == (i-2))):
                if (notTenthFrame(i, numOfRolls) and (lastStrikeRoll == (i-1))):
                    score = score + pins_per_roll[i]

                    if (pins_per_roll[i-2] == 10): #Multiple strikes back to back
                        score = score + pins_per_roll[i]

                elif (notTenthFrame(i, numOfRolls) and (lastStrikeRoll == (i-2))):
                    score = score + pins_per_roll[i]

            if (not firstThrowInFrame):
                if (pins_per_roll[i] + pins_per_roll[i-1] == 10): #Spare
                    previousFrameSpare = True

            score = score + pins_per_roll[i]
            firstThrowInFrame = not firstThrowInFrame

    s.add(totalScore == score)
    s.check()
    return(s.model().eval(totalScore))

def notTenthFrame(index, numOfRolls):
        if ((index>0) and (index != numOfRolls-1) and (index != numOfRolls-2)):
            return True
        else:
            return False