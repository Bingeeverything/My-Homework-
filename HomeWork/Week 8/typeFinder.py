thing = input('enter')
try:
    yo = int(thing)
    print('int')
except ValueError:
    try:
        yo = float(thing)
        print('float') 
    except ValueError:
        print('str')
