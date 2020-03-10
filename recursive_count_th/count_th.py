'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    if len(word) <= 1:
        return 0
    if word[0:2] == 'th':
        return count_th(word[1:]) + 1
    return count_th(word[1:])
print(count_th('asdbthaaiethignebdathasethasaabth')) #should print 5

#every time theres match then line 11 will add to the count
#if theres no matches at all then it will return 0
# 0(n) because the longer the word means the more times the function is called