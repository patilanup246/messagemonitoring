from datetime import datetime
import os, sys, io, time, configparser
from configparser import ConfigParser


def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles


def getPendingMessageDetails():
    datetimenow = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
    configur = ConfigParser()
    configur.read('app.ini')
    parentdir = configur.get('MAIN', 'PARENTDIR')
    errpath = configur.get('MAIN', 'ERRDIR')
    skipdir = configur.get('MAIN', 'SKIPDIR')

    filecount = 0;
    listOfFiles = getListOfFiles(parentdir)
    isfirstdic = ''
    boolfirstdic = True;
    for path in listOfFiles:
        isskip = False
        filepathdir = os.path.dirname(path)
        for i in skipdir.split(','):
            if i in filepathdir:
                isskip = True
        if isskip == True:
            continue
        import glob

        if filepathdir == isfirstdic:
            boolfirstdic = False
        else:
            boolfirstdic = True

        if boolfirstdic == True:
            isfirstdic = filepathdir
            tifCounter = len(glob.glob1(filepathdir, "*.*"))
            data = open(errpath + '/' + datetimenow + ".txt", "a")  # open file in append mode
            filedeatils = " Total file pending Folder Path: " + filepathdir + " , Total file pending : " + str(
                tifCounter)
            data.write(filedeatils + '\n')  # separator in file
            data.close()

            print(filedeatils)

        cdate = os.stat(path).st_ctime
        a = datetime.now()
        b = datetime.fromtimestamp(cdate)
        c = a - b
        dir_path = '\\'.join(path.split('\\')[0:-1])
        data = open(errpath + '/' + datetimenow + ".txt", "a")  # open file in append mode
        filedeatils = " Folder Path: " + dir_path + ", Create File: " + time.ctime(
            cdate) + ", Pending File Time(Minutes): " + str(c) + ", File Name: " + os.path.basename(path)
        data.write(filedeatils + '\n')  # separator in file
        data.close()


if __name__ == '__main__':
    getPendingMessageDetails()
