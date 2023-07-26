try:
    f = open('errors.txt','w')
    f.write('This is the simple text file.')
except IOError:
    print('ERROR : COULD NOT FIND THE FILE OR READ THE DATA!')
finally:
    print('FILE UPDATED SUCCESSFULLY!')
    f.close()