'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# def count_th(word):
#
#     # TBC
#     if word == "":
#         return 0
#
#     return (len(word.split('th')) - 1)

def count_th(word):

    # Base case, when length is less then 2 there is no possibility for 'th'
    if len(word) < 2:
        return 0

    # if the first 2 index of the list = 'th', one is added and function is called again with updated list(removed 'th')
    if word[0:2] == 'th':
        return 1 + count_th(word[2:])

    # function run again starting from the first index, we want to move by one to make sure we get all the 'th'
    else:
        return count_th(word[1:])


# count_th("abcthefthghith")
