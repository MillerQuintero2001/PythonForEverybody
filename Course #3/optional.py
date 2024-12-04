import re
file = open('regex_sum_2113593.txt')
print( sum( [ int(i) for i in re.findall('[0-9]+',file.read()) ] ) )