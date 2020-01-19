from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time
from datetime import datetime


def getPendingMessageDetails():
    datetimenow=datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
    parentFolderPath = "F:/Parent Folder/" #Parent Folder Path
    errorFolderPath="F:/Parent Folder/ErrorFiles"  #Error or Pending file final output folder path

    folder_list=os.listdir(parentFolderPath)
    subfolder_list=[]
    subfolder_list.append("SubFolder1") #SubFolder1
    subfolder_list.append("SubFolder2") #SubFolder1
    subfolder_list.append("SubFolder3") #SubFolder3 .............SubFolderN   so on..

    isparentfolderdone = False
    for item in subfolder_list:
        for subfolderlist in os.listdir(parentFolderPath+item):
            try:
                if 'ErrorFiles' !=subfolderlist:
                    if "." in subfolderlist:
                        if isparentfolderdone ==True:
                            raise ValueError('Represents a hidden bug, do not catch this')
                        else:
                            dir_path=parentFolderPath
                            isparentfolderdone=True
                    else:
                        dir_path = parentFolderPath +item+'/'+ subfolderlist

                    # all entries in the directory w/ stats
                    data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
                    data = ((os.stat(path), path) for path in data)

                    # regular files, insert creation date
                    data = ((stat[ST_CTIME], path)
                            for stat, path in data if S_ISREG(stat[ST_MODE]))
                    filecount=0
                    for cdate, path in sorted(data):
                        filecount=filecount+1
                        a = datetime.now()
                        b = datetime.fromtimestamp(cdate)
                        c = a - b
                        data = open(errorFolderPath+'/'+datetimenow + ".txt", "a")  # open file in append mode
                        filedeatils=" Folder Path: "+dir_path+", Create File: "+time.ctime(cdate)+", Pending File Time(Minutes): "+ str(c)+", File Name: "+ os.path.basename(path)
                        data.write(filedeatils + '\n')  # separator in file
                        data.close()
                    data1 = open(errorFolderPath + '/' + datetimenow + ".txt", "a")  # open file in append mode
                    data1.write('Pending File or Messages in folder ('+dir_path+') :'+str(filecount) +'\n')  # separator in file
                    data1.close()
                    print('Pending File or Messages in folder ('+dir_path+') :'+str(filecount))
            except Exception as error:
               pass

    for subfolderlist in subfolder_list:
        try:
            if 'ErrorFiles' != subfolderlist:
                dir_path = parentFolderPath + subfolderlist

                # all entries in the directory w/ stats
                data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
                data = ((os.stat(path), path) for path in data)

                # regular files, insert creation date
                data = ((stat[ST_CTIME], path)
                        for stat, path in data if S_ISREG(stat[ST_MODE]))
                filecount = 0
                for cdate, path in sorted(data):
                    filecount = filecount + 1
                    a = datetime.now()
                    b = datetime.fromtimestamp(cdate)
                    c = a - b
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
        except Exception as error:
            pass


if __name__ == '__main__':
    getPendingMessageDetails()