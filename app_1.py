from datetime import datetime
import os,sys,io,time,configparser


parentdir = ''
errpath = ''
logdir = ''

def load_config(config_file):
    config = configparser.ConfigParser()
    config.read(sys.argv[1])
    global parentdir,errpath,logdir

    if 'PARENTDIR' in config['MAIN']:
      parentdir=config['MAIN']['PARENTDIR']
    else:
        sys.exit("PARENTDIR is not defined\n")

    if 'ERRDIR' in config['MAIN']:
        errpath=config['MAIN']['ERRDIR']
    else:
        sys.exit("ERRDIR is not defined\n")

    if 'LOGDIR' in config['MAIN']:
      logdir=config['MAIN']['LOGDIR']
    else:
        sys.exit("LOGDIR is not defined\n")





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
    parentFolderPath = "C:/Users/A716833/PycharmProjects/folderstructure/EVGM"  # Parent Folder Path
    errorFolderPath = "F:/Parent Folder/ErrorFiles"  # Error or Pending file final output folder path

    folder_list = os.listdir(parentFolderPath)
    # Get the list of all files in directory tree at given path
    filecount=0;
    listOfFiles = getListOfFiles(parentFolderPath)
    for path in listOfFiles:
        cdate = os.stat(path).st_ctime
        # filecount = filecount + 1
        a = datetime.now()
        b = datetime.fromtimestamp(cdate)
        c = a - b
        dir_path = '\\'.join(path.split('\\')[0:-1])
        data = open(errorFolderPath + '/' + datetimenow + ".txt", "a")  # open file in append mode
        filedeatils = " Folder Path: " + dir_path + ", Create File: " + time.ctime(
            cdate) + ", Pending File Time(Minutes): " + str(c) + ", File Name: " + os.path.basename(path)
        data.write(filedeatils + '\n')  # separator in file
        data.close()

    data1 = open(errorFolderPath + '/' + datetimenow + ".txt", "a")  # open file in append mode
    data1.write('Pending File or Messages in folder (' + dir_path + ') :' + str(
        filecount) + '\n')  # separator in file
    data1.close()
    print('Pending File or Messages in folder (' + dir_path + ') :' + str(filecount))


if __name__ == '__main__':
    try:
        load_config(sys.argv[1])
    except SystemExit as e:
        ef = io.open(errpath, 'a')
        ef.write(str(e))
        ef.close()
        os._exit(1)
    getPendingMessageDetails()
