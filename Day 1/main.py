with open("input.txt", "r") as inp:
    tempSum = 0
    carriedCal = []  # stores the calories carried by each elf
    while True:
        line = inp.readline()
        if not line:  # if line is empty, end of file
            break  # close file

        if line == "\n":
            carriedCal.append(tempSum)
            tempSum = 0
        else:
            tempSum += int(line)

maxCal = max(carriedCal)
print(f"Elf {carriedCal.index(maxCal)} is holding the most calories, {maxCal}.")

# -- end of part 1 -- #

carriedCalSorted = sorted(carriedCal, reverse=True)

top1Carried = carriedCalSorted[0]
top2Carried = carriedCalSorted[1]
top3Carried = carriedCalSorted[2]

print(f"Elves {carriedCal.index(top1Carried)}, {carriedCal.index(top2Carried)}, and {carriedCal.index(top3Carried)} "
      f"are carrying the most calories - {top1Carried}, {top2Carried}, and {top3Carried} respectively. "
      f"That's a total of {top1Carried + top2Carried + top3Carried}")
