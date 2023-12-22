# print triangle

# for row in range(6):
#     for col in range(row):
#         print("*",end='')
#     print("\n")


# # print number triangle

# count = 0

# for row in range(6):
#     for col in range(row):
#         print(count,end='')
#     print("\n")
# count +=1


# print alpha bet A
# for row in range(6):
#     for col in range(5):
#         if col == 0 and row != 0:
#             print("*", end=' ')
#         elif col == 1 and (row == 0 or row == 3):
#             print("*", end=' ')
#         elif col == 2 and (row == 0 or row == 3):
#             print("*", end=' ')
#         elif col == 3 and (row == 0 or row == 3):
#             print("*", end=' ')
#         elif col == 4 and row != 0:
#             print("*", end=' ')
#         else:
#             print(end="  ")
#     print("\n")


# print alpha bet B
# for row in range(5):
#     for col in range(18):
#         if col == 0 and row != 0:
#             print("*", end=' ')
#         elif(col == 1 and (row == 1 or row == 2 or row == 3 or row == 5)):
#             print('*',end =' ')
#         elif(col == 2 and (row == 1 or row == 3 or row == 4 or row == 5)):
#             print('*',end =' ')
#         else:
#             print(end="  ")
#     print("\n")

# print alphabet S
# print alphabet S and U
for row in range(6):
    for col in range(16):
        # for letter S
        if col < 4 and (row == 0 or row == 3 or row == 5):
            print("*", end=' ')
        elif (row == 1 or row == 2) and col == 0:
            print("*", end=' ')
        elif row == 4 and col == 4:
            print("*", end=' ')
        elif col == 6 :
            print("*", end=' ')
        elif col == 7 and (row == 5 ):
            print("*", end=' ')
        elif col == 8 and (row == 5 ):
            print("*", end=' ')
        elif col == 9 and (row == 5 ):
            print("*", end=' ')
        elif col == 10 :
            print("*", end=' ')

        elif col == 12 and (row == 1 or row == 0 or row == 2):
            print("*", end=' ')
        elif (row == 0 or row == 3 and row == 4 and row == 5 and row == 6) and col == 13:
            print("*", end=' ')
        elif (row == 0 or row == 3 and row == 4 and row == 5  and row == 6) and col == 14:
            print("*", end=' ')
        elif  (row == 4 or  row == 5) and col == 15:
            print("*", end=' ')


        # elif col==6:
        #     print("*", end=' ')
        # elif col==7 and (row==1):
        #     print("*", end=' ')
        # elif col==8 and (row==2):
        #     print("*", end=' ')
        # elif col==9 and (row==3):
        #     print("*", end=' ')
        # elif col==10 and (row==4):
        #     print("*", end=' ')
        # elif col==11:
        #     print("*", end=' ')
        else:
            print(end="  ")

        # # for letter U
        # if col > 4 and col < 8 and (row == 0 or row == 1 or row == 3 or row == 4):
        #     print("*", end=" ")
        # elif col >= 8 and col < 12 and (row == 0 or row == 5):
        #     print("*", end=" ")
        # elif col == 12 and (row == 1 or row == 3 or row == 4):
        #     print("*", end=" ")
        # else:
        #     print(end=' ')

    print("\n")
