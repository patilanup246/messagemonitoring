# messagemonitoring

Phanindra Ch 2:23 PM
The parameters should be stored in a config file such as xxx.ini and passed to the script.

The folder to be monitored should be passed in as one of these parameters, such as c:\evgm\ob\APERAK

For just getting the files under a folder (excluding subfolders), you can try the sample codes mentioned in this web page (skip the item if it is os.path.isdir())

https://thispointer.com/python-how-to-get-list-of-files-in-directory-and-sub-directories/

And referring to the sample script (cdob.py), you can use below statement to skip the files with “.” in front. Only check if it is a file.

if not obf.name.startswith('.') and obf.is_file():

Use something like below to check the file age.

if obf.stat().st_mtime < now - int(fileage):

please note above comments

Anup Patil 2:25 PM
Its new task or exiting?

(edited)
Okay, I will.

PC
Phanindra Ch 1/16/20 2:23 PM
please note above comments

But, I have already do many changes in exiting scrip.

PC
Phanindra Ch 2:29 PM
existing only

this is last change

Anup Patil 2:30 PM
Okay sir

PC
Phanindra Ch 2:31 PM
and the has to check two IB and OB parent folders

Anup Patil 2:32 PM
Can please send me folder structure

In zip files

Please send me a folders in zip with proper structure

Anup Patil 5:48 PM
Hello sir

PC
Phanindra Ch 8:05 PM
sure
ill send the code format how my supervisor poking me for

tomorrow

Friday, January 17, 2020
PC
Phanindra Ch 6:03 PM
 folderstructure.zip 9.63 MB
Anup Patil 6:04 PM
Thanks sir
I will check and update the script.

Can you send me this one as well.

PC
Phanindra Ch 1/16/20 8:05 PM
sure
ill send the code format how my supervisor poking me for

Saturday
PC
Phanindra Ch 4:15 PM
which one

Anup Patil 1/17/20 6:05 PM
Can you send me this one as well.

in that folder script folderwill be there you can find the code

Anup Patil 4:23 PM
okay

Yesterday
PC
Phanindra Ch 6:26 AM
any update on this

Anup Patil 10:32 AM
I am working on it

PC
Phanindra Ch 10:35 AM
ok


 
