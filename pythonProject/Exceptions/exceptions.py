# cart = 2
#
# if cart !=2:
#     pass
#
#
# assert(cart == 2)


#try , catch == except

try:
    with open('wow', 'r') as reader:
        list = reader.readlines()
        for line in list:
            print(line)


except Exception as e: #will show the python message stored in e variable
    print('Error, file does not exist and python throws this error:', e)


finally: #will run if it either fails or pass
    print('Cleaning up resources')
