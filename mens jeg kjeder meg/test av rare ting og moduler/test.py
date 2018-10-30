# make 2 ditionary's outside function to save time.
# since the actual numbers comes in groups of 1 or 2, we make one for each
dict0to9 = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9,
}

dict10to90 = {
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
    "eighteen": 18, "nineteen": 19,

    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
    "seventy": 70, "eighty": 80, "ninety": 90
}


def parse_int(string):
    number, res = string.split()[::-1], 0
    # make the "number" into a list of its pieces and make a resoult value
    # The number list is backwards so we can start from the back
    # and iterate forwards in the number
    temp, h, t, m = 0, 1, 1, 1
    # make the variables for temporary usage and hundreds, thousands, millions
    for i in number:
        temp = 0
        # reset temp

        # check if this part of the number is between 10 and 99
        # and adding either the value between 10 and 19 or just
        # just the 10's (20,30,40)
        for j in dict10to90:
            if j in i:
                temp += dict10to90[j]
                break

        # adding the single digit at the end if it is between
        # 0-9 or >=20, (so if temp is 40, find out if it has a
        # single digit number and add that)
        if temp == 0 or temp > 19:
            for j in dict0to9:
                if " " + j + " " in " " + i + " " or "-" + j + " " in i + " ":
                    # the " " and "-" is just to avoid false possitives
                    temp += dict0to9[j]
                    break
        # adding to resoult with multiplier
        res += temp * h * t * m

        # when we pass a "hundred", "thousand", "million" we increase the multiplier when adding numbers to res
        if i == "hundred":
            h = 100
            continue
        elif i == "thousand":
            t = 1000
            h = 1
            continue
        elif i == "million":
            m = 1000000
            h = 1
            t = 1
            continue
    return res