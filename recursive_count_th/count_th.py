'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    count = {}
    if 'th' in count:
        count['th'] += 1
    else:
        count['th'] = 1

    for key in count:
        if count[key] > 1:
            print (key, count[key])

# count = 0
# def count_th(word):
#     for i in word: 
#         if i == 'th': 
#             count = count + 1