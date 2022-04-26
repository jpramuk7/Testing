import os
import glob
import zipfile
from zipfile import ZipFile

folder = r"E:\API_creation\upload"

try:
#iterate through files in a folder
    gdbfiles = []
    shpfiles = []
    csvfiles = []
    jsonfiles = []
    zipfiles = []
    
    for root, dirs, files in os.walk (folder):
        for file in files:
            if file.endswith(".zip"):
                zipfiles.append(os.path.join(root, file))
            elif file.endswith(".csv"):
                csvfiles.append(os.path.join(root, file))
            elif file.endswith(".json"):
                jsonfiles.append(os.path.join(root, file))
            else:
                pass

    #find zipped gdb files
    gdb_dirs = []  
    for i in zipfiles:
        zip_f = ZipFile(i)
        #print(zip_f)
        for f in zip_f.namelist():
            zinfo = zip_f.getinfo(f)
            #print(zinfo)
            if zinfo.is_dir():
                r_dir = f.split('/')
                r_dir = r_dir[0]
                if r_dir not in gdb_dirs:
                    gdb_dirs.append(os.path.join(root, r_dir))
                    #gdb_dirs.append(r_dir)
    print(gdb_dirs)
    
    for i in gdb_dirs:
        if i.endswith(".gdb"):
            #gdbfiles.append(os.path.join(root, i))
            docx_zip = zipfile.ZipFile(i)
            print(docx_zip)
        else:
            pass

    for i in zipfiles:
        if i not in gdb_dirs:
            shpfiles.append(os.path.join(root, i))
        else:
            pass
    #print(gdbfiles)
    #print(shpfiles)
    #print(gdb_dirs)

except Exception as e:
    print(e)