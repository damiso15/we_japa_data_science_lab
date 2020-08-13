def readable_timedelta(days):
    # insert your docstring here
	'''
	The function should take one argument, an integer days, and return a string that says how many 
	weeks and days that is.
	weeks is a variable that divides the argument days by a constant 7 and returns only the Whole 
	number.
	remainder is a variable that divides the argument days by a constant 7 and returns only the 
	remainder.
	'''

    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)