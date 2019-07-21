
# try:
#     f = open('nofilehere.txt')
#     content = f.read()
#     f.close()
#
# #except OSError as error:
# except Exception as error:
#     print('Error occurred' + str(error))
#     print('Error occurred:', error.strerror)


try:
    with open("nofile.txt") as t:
        t.read()
except Exception as error:
    print(str(error))