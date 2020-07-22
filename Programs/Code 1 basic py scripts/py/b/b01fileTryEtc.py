try:
    fHandle = open('b01inputFile.txt')
    getAline = fHandle.readline()
    getAnInteger = int(getAline.strip())
    print ("Got integer ... " , getAnInteger)
except IOError as fileError:
    print (fileError)
except ValueError:
    print("Not a valid integer ")
except:
    print("Unexpected error:", sys.exc_info()[0])

