# the function takes in desired_s and desired_p
# and then: for each entry in our database, i don't know what exactly is in the database but lets say it's something life this:
# entry_1: [comapany name, some_other_para1, some_other_para2, sustainability_index, profitability_index]
# we will take the sustainability_index and profitability_index columns. for simplisity I will call them (company_s, company_p)
# then for each company, I will calculate the following
# similarity = sqrt((desired_s - company_s)^2+(desired_p - company_p)^2)
# then we can add this "similarity column" to the database / send to front end
# in the code, it will be like this

import math


def cal_similarity(desired_s, desired_p):
    for i in range(len(database)):
        company_entry = database[i]
        comapny_s = company_entry.sustainability_index
        company_p = company_entry.profitability_index

        company_similarity = math.sqrt(
            (desired_s-comapny_s)**2+(desired_p-company_p)**2)

        # append company_similarity to another column in the database
        # the code may be wrong, but see whatever is the syntax for batabase language
        database.append(company_similarity)


# call cal_similarity
cal_similarity(desired_s, desired_p)

# sort database in terms of "company similarity" column
