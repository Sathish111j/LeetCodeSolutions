class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        def mergeSort(heights, names):
            if len(heights) > 1:
                mid = len(heights) // 2

                leftHalf = heights[:mid]
                rightHalf = heights[mid:]

                namesLeft = names[:mid]
                namesRight = names[mid:]

                mergeSort(leftHalf, namesLeft)
                mergeSort(rightHalf, namesRight)
                
                i = j = k = 0

                while i < len(leftHalf) and j < len(rightHalf):
                    if leftHalf[i] > rightHalf[j]: 
                        heights[k] = leftHalf[i]
                        names[k] = namesLeft[i]
                        i += 1
                    else:
                        heights[k] = rightHalf[j]
                        names[k] = namesRight[j]
                        j += 1
                    k += 1

                while i < len(leftHalf):
                    heights[k] = leftHalf[i]
                    names[k] = namesLeft[i]
                    i += 1
                    k += 1
                
                while j < len(rightHalf):
                    heights[k] = rightHalf[j]
                    names[k] = namesRight[j]
                    j += 1
                    k += 1

        mergeSort(heights, names)
        
        return names

        # heightToName = dict(zip(heights, names))
        # sortedHeights = sorted(heightToName.keys(), reverse=True)
        # sortedNames = [heightToName[height] for height in sortedHeights]
        # return sortedNames