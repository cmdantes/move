#Leetcode minimum of 5 everyday urgent
#1d array
def OneDArray():
    num1 = [1,2,3,4]
    for i in range(1, len(num1)):
        num1[i] += num1[i-1]
    print("1d array = ", num1)
# pair of 2 sum numbers
def TwoNumberPair():
    nums = [11,12,3,4,7]
    target = 18
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            sums = nums[i] + nums[j]
            if sums == target:
                print("sums of 2 pair", [nums[i], nums[j]])
#Removing Vowels from sentence
def RemoveVowelsFromSentence():
    sentence = "if ate is panget then koyz koyz is panget"
    vowels = ["a","i","e","o","u"]
    new_string = ""
    for i in range(len(sentence)): #check sentence lenght
        if sentence[i] not in vowels: #check sentence number and check if same from vowels a
            new_string += sentence[i]
    print(new_string)
#Integers with Good Pair
def GoodPair():
    nums = [1,2,3,1,1,3]
    good_pair = 0
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                good_pair +=1
    print(good_pair)
#Kids With the Greatest Number of Candies
def KidsWIthGreatesNumOfCandies():
    candies = [2,3,4,5,1,2]
    extraCandies = 3
    rist = list()
    for i in candies:
        if i + extraCandies >= extraCandies:
            rist.append("true")
        else:
            rist.append("false")
    print(rist)
