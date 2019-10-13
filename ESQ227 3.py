def EggsIntoBoxes(NumberOfEggs):
    NumberOfBoxes=NumberOfEggs//6
    EggLeftOver=NumberOfEggs%6
    return NumberOfBoxes,EggLeftOver
print(EggsIntoBoxes(27))
