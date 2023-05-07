def find_closest(filename):
    datafile = open(filename, "r")
    datafile.readline()
    quantitydict = {}
    line = datafile.readline()
    linelist1 = line.split(",")
    quantitydict[linelist1[0]] = linelist1[1]
    for line in datafile:
        linelist = line.split(",")
        quantitydict[linelist[0]] = linelist[1]
    closestsofar = abs(float(linelist[1])-float(linelist1[1]))
    returnlist = [linelist[0],(linelist1[0])]
    for key1 in quantitydict:
        for key2 in quantitydict:
            if key1!=key2:
                if closestsofar > abs(float(quantitydict[key1])-float(quantitydict[key2])):
                    closestsofar = abs(float(quantitydict[key1])-float(quantitydict[key2]))
                    returnlist = [key1, key2]

    print(returnlist)
    return returnlist
if __name__ == '__main__':
    find_closest("bank1.csv")
