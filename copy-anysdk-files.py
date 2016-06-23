import os
import os.path
import shutil
import sys

libdir = ""

def copyfile(file):
    global libdir
    global count

    if not os.path.exists(file):
        print "file not exists: " + file
    else:
        if os.path.isfile(file):
            sourceDir = os.path.dirname(file)
            targetDir = libdir + sourceDir

            if not os.path.exists(targetDir): 
                os.makedirs(targetDir)

            shutil.copyfile(file, libdir + file)
            # print "copy file: " + file
        elif os.path.isdir(file):
            # shutil.copytree(file, libdir + file)
            # print "copy dir: " + file
            for root, dirs, files in os.walk(file):
                for dir in  dirs:
                    # print(os.path.join(root,dir))
                    copyfile(os.path.join(root,dir));   
                for f in files:
                    # print(os.path.join(root,f))
                    copyfile(os.path.join(root,f))
       
    return

cccprojdir = sys.argv[1]

if not os.path.exists(cccprojdir):
    print "ccc proj dir not exists: " + cccprojdir
    sys.exit()
else:
	print "ccc proj dir: " + cccprojdir

androidprojdir = cccprojdir + "/build/jsb-default/frameworks/runtime-src/proj.android/"
if not os.path.exists(androidprojdir):
    print "android proj dir not exists: " + androidprojdir
    sys.exit()

libdir = cccprojdir + "/"

copyfile("./build/")

print "--------------------"
print "copy all anysdk files finished"

