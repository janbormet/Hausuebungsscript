import os
import shutil
from zipfile import ZipFile
from tkinter import *
from tkinter import filedialog as fd

def do():
    root = Tk()
    root.withdraw()
    
    ## Getting path to zip download
    downloadedFile = fd.askopenfilename(title = "Select downloaded zip-file", filetypes = [("zip files", "*.zip")])
    if downloadedFile == "":
        return
    ## Getting path to empty folder
    targetDirectory = fd.askdirectory(title = "Select Target Directory")
    if(len(os.listdir(targetDirectory)) != 0):
        print("Please select an EMPTY Folder as target directory!!!")
        return
    
    ## Getting paths to testbenches
    testbenches = []
    testbenchesLeft = True
    while testbenchesLeft:
        pathOfTestbench = fd.askopenfilename(title = "Select Testbench",filetypes = [("java files", "*.java")])
        if(pathOfTestbench != ""):
            testbenches.append(pathOfTestbench)
        else:
            testbenchesLeft = False
    
#    print(testbenches)
        
    folders = []
    files = []
    try:
        with ZipFile(downloadedFile, 'r') as zipDownload:
            zipDownload.extractall(targetDirectory)
    except:
        print("Could not unzip Download")
        return
    
    ##
    print("Finding files")
    for d in os.listdir(targetDirectory):
        folders.append(os.path.join(targetDirectory, d)) # memorize paths to all folders which contain the zipped projects
    
    for f in folders:
        files.append(os.path.join(f, os.listdir(f)[0])) # memorize paths to all the zipped projects
    print("\t", len(files), "files found")

    print("\nUnzipping")
    a = 0
    for f in files: # unzip all projects into target directory
        try:
            with ZipFile(f, 'r') as zp:
                zp.extractall(targetDirectory)
            shutil.rmtree(folders[a])
        except:
            print("\tunzipping failed for file", f)
        a +=1

    print("\nCopy Testbenches into Projects")

    for d in os.listdir(targetDirectory):    # copy all the testbenches into all the Projects
        try:
            s = os.path.join(targetDirectory, d, "src")
            try:
                os.mkdir(s)
            except:
                pass
            for tb in testbenches:
                if tb.endswith("FibComp.java") or tb.endswith("FibonacciTest.java"):
                    shutil.copy(tb, os.path.join(s, "h1"))
                elif tb.endswith("BasicGehege.java") or tb.endswith("ZooTest.java"):
                    shutil.copy(tb, os.path.join(s, "h2"))
        except:
            print("\tfailed for file ", d)

do()
input("")
quit()
