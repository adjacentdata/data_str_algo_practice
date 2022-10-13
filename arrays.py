# Arrays (Following Neetcodes Questions)

#Example of an Array
arr = [1,2,3,4]


# CONTAINS DUPLICATE
def contains_duplicate(nums):
    """
    Contains duplicate: set up hashmap or hash set; Iterate over the values and add to list if it is not present. 
    """
    hash_map = {} #or hashset set()
    for i in nums:
        if i in hash_map:
            return True
        else:
            hash_map[i] = i # hashset.add(n)
    return False

# TWO SUM 
Time: O(n)
Space: O(n) 
def twoSum(nums, target):
    """
    Process
        The first step is to create a space in memory with a hash table.
        Then iterate over it and if the target - array value is not in the table
        then add the diff into the table.
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hashed = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hashed:
            return [i, hashed[diff]]
        hashed[nums[i]] = i
    return -1

print(twoSum(nums,target))


# isAnagram
# O(n^2)

s = "anagram"
t = "nagaram"

def isAnagram_brute(s,t):
     """
        create two hash sets to store the counts of each string.
        When looping, add the letter and add 1 + hash.get(value if exists, or it becomes 0)
        Then compare the hash sets     
    :param s: string
    :param t: string
    :return:  Boolean
    """
    hash_s = {}
    hash_t = {}
    for i in range(len(s)):
        hash_s[s[i]] = 1 + hash_s.get(s[i], 0)
        hash_t[t[i]] = 1 + hash_t.get(t[i], 0)
    print(hash_t)
    print(hash_s)
    return hash_s == hash_t

print(isAnagram_brute(s,t))

# REPLACE MAX IN LIST

def replace_max_element(arr):
    """
    Iterate backwards. len(arr)-1, -1,-1
        Create a new max but start the ending array with a -1.
        then start the iteration finding the new max
        replace element with the current max all the way to the end
    :param arr: list of elements
    :return:
    """
    rightMax = -1 
    for i in range(len(arr)-1,-1,-1):
        newMax = max(rightMax, arr[i])
        arr[i] = rightMax
        rightMax = newMax
    return arr

# iS IT A SUBSEQUENCE

def isSubsequence(s,t):
    """
    using a while loop to iterate over s and t. If i == the length of s then it should return complete
    O(n) is the right way to do it. 

    :param s: sub
    :param t: full string
    :return: 
    """
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i+=1
        j+=1
    return i == len(s)

#LENGTH OF LAST WORD 

def length_of_last_word(strings):
    return len(strings.split()[-1])

def len_of_last(s):
    lt = s.split(" ")
    n = len(lt) - 1
    while n >= 0:
        if lt[n] == "":
            n -= 1
        else:
            return len(lt[n])

print(len_of_last(please))

# LONGEST COMMON PREFIX
def longestCommonPrefix(strs):
    """
    Build a string containing prefix. n^2 when looping each string.
    Reduction method might be the best way.
    set the prefix = flower and loop through the array
    run a while loop
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return(strs[0])
    pref = strs[0]
    plen = len(pref)

    for s in strs[1:]:
        while pref != s[0:plen]:
            pref = pref[0:(plen-1)]
            plen-= 1
        if plen == 0:
            return("")
    return pref
