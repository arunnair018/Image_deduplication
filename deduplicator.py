from PIL import Image
import math,os,shutil,numpy

# extension to be checked
ext=['.jpg','.png','.bmp','.gif','.tga','.thm','.tif','tiff','.jpeg'];
ret='false'


# function to move image if no duplicate
def msgnmov(ret,cwd,server_flder):
    if ret=='true':
        print('visiualy similar file already there...')
    else :
        shutil.move(cwd,server_flder)
        print('Uploaded...')


# function to calculate correlation factor 
def corrcoef(a,b):
    a = a - numpy.mean(a)
    b = b - numpy.mean(b)
    r = (a*b).sum() / math.sqrt((a*a).sum() * (b*b).sum());
    return r      


# function to check correlation factor of images      
def check(cwd,server_flder,image_selected,ls):
    for files in ls:
        if files.endswith(tuple(ext)):
            # open and process the image
            image_ls=Image.open(server_flder+'\\'+files).resize((128,128),Image.ANTIALIAS)
            # calculate the correlation factor            
            rel=corrcoef(image_selected,image_ls)
            if rel > 0.90:
                return 'true'
                break
            else:
                continue


# function to get files from specified folder
def getfile():
    server_flder=raw_input('Enter the server_folder: ')
    while True:
        cwd=raw_input('file(to upload) path: ')
        # open and process the image 
        image_selected=Image.open(cwd).resize((128,128),Image.ANTIALIAS)
        # list file from server_folder        
        ls=os.listdir(server_flder)
        # check for dup in the files
        ret=check(cwd,server_flder,image_selected,ls)
        # upload the image        
        msgnmov(ret,cwd,server_flder)

        
# start of the program
if __name__=="__main__":
    getfile()
