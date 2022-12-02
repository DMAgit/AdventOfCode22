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
print(f"Elves {carriedCal.index(carriedCalSorted[0])}, {carriedCal.index(carriedCalSorted[1])}, "
      f"and {carriedCal.index(carriedCalSorted[2])} are carrying the most calories - {carriedCalSorted[0]}, "
      f"{carriedCalSorted[1]}, and {carriedCalSorted[2]} respectively. That's a total of "
      f"{carriedCalSorted[0] + carriedCalSorted[1] + carriedCalSorted[2]}")
