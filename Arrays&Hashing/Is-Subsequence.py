class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # last_index=0
        # count=0

        # for char in s :
        #     for i in range(last_index,len(t)):   // instead of taking from  s and check in t
        #         if char == t[i]:
        #             count+=1
        #             last_index=i+1
        #             break

        # return count==len(s)

        i = 0
        for let in t:
            if i==len(s):    # take each character from t aand check in s using a single for loop and increment each index when the letter is found
                return True
            if s[i]==let:
                i += 1
        return i==len(s)

        