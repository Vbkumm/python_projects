with open('newfile.txt', mode='w') as f:
    f.write('I created this file!!!')
with open('newfile.txt', mode='r') as f:
    print(f.read())
