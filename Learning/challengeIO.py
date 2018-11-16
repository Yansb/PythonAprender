# Write a program to append the times tables to our jabberwocky poem
# in sample.txt. We want the tables from 2 to 12 (similar to the output
# from the For loops part 2 lecture in section 6).
#
# The first column of numbers should be right justified. As an example,
# the 2 times table should look like this:
#   1 times 2 is 2
#   2 times 2 is 4
#   3 times 2 is 6
#   4 times 2 is 8
#   5 times 2 is 10
#   6 times 2 is 12
#   7 times 2 is 14
#   8 times 2 is 16
#   9 times 2 is 18
#  10 times 2 is 20
#  11 times 2 is 22
#  12 times 2 is 24
# --------------------

# for inner in range(0,12):
#     inner +=1
#     for outer in range(0,13):
#         result = inner * outer
#         with open("D:\Python file\sample.txt",'a') as times_table:
#             times_table.write("_"*40)
#             times_table.write("\n")
#             times_table.write("{} times {} equals {}\n".format(inner, outer, result))
#
#
#     print("_"*40)

# outra possivel resposta:
with open("D:\Python file\sample.txt", 'a') as tables:
    for i in range(2,13):
        for j in range(1,13):
            print("{1:>2} times {0} is {2}".format(i, j, i*j), file=tables)
        print("_"*20, file= tables)