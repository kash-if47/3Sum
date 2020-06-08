
class ThreeSum:
    def __init__(self, numlist):
        self.numList = numlist

    def find(self):
        if len(self.numList) < 3:
            return []
        sortedList = sorted(self.numList)
        # print(sortedList)
        solution = []
        for i in range(len(sortedList) - 1):
            high = len(sortedList) - 1
            low = i + 1
            while(high > low):
                lowNum = sortedList[low]
                highNum = sortedList[high]
                sum = sortedList[low] + sortedList[high]
                # if (sum + sortedList[i]) == 0:
                #     solution.append([sortedList[i], sortedList[low], sortedList[high]])
                #     low = low + 1
                #     high = high - 1
                # elif (sum + sortedList[i]) > 0:
                #     high = high - 1
                # else:
                #     low = low + 1
                if (low - 1 > i and sortedList[low] == sortedList[low - 1]) or (sum + sortedList[i]) < 0:
                    low = low + 1
                elif (high + 1 < len(sortedList) and sortedList[high] == sortedList[high - 1]) or (sum + sortedList[i]) > 0:
                    high = high - 1
                elif (sum + sortedList[i]) == 0:
                    solution.append([sortedList[i], sortedList[low], sortedList[high]])
                    low = low + 1
                    high = high - 1
        # print(solution)
        return solution




