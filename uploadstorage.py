import os
from posixpath import relpath
from dropbox.files import WriteMode 
import dropbox

class TransferData :
    def __init__(self,access_token) :
        self.access_token = access_token

    def upload(self,forrm, too) :
        dbx = dropbox.Dropbox(self.access_token)
        for root,dir,files in os.walk(forrm) :
            for i in files :
                localpath = os.path.join(root,i)
                rlpath = os.path.relpath(localpath,forrm)
                dbpath = os.path.join(too,rlpath)        
                with open(localpath,"rb")as f :
                    dbx.files_upload(f.read(),dbpath,mode = WriteMode('overwrite'))

def main() :
    access_token = "AM9FI4pN-MoAAAAAAAAAARONzJAz1fDZ1kz1MTbClpItVrYuO6296MfZzINTSblB"
    td = TransferData(access_token)
    filefrom = input("Enter file source :")
    filetoo = input("Enter DropBox location :")
    td.upload(filefrom,filetoo)
    print("File Moved")

main()