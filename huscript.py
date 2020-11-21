import os, sys
import os.path
from os import path
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
    print(str(os.listdir(targetDirectory)))
    if(len(os.listdir(targetDirectory)) != 0 and not(len(os.listdir(targetDirectory)) == 1 and os.path.exists(os.path.join(targetDirectory, "temp")))):
        print("Please select an EMPTY Folder as target directory!!!")
        answer=(input("\n do you want to clear the Folder?(y/n)"))
        if answer == "y" or answer == "yes" or answer == "j":
            rmFolderContents(targetDirectory)
        else:
            return
    
    ## Getting paths to testbenches
    testbenches = []
    while True:
        pathOfTestbench = fd.askopenfilename(title = "Select Testbench",filetypes = [("java files", "*.java")])
        if(pathOfTestbench):
            testbenches.append(pathOfTestbench)
        else:
            break
        
    folders = []
    files = []
    print("\n Preparing...")
    ## Create Temp folder
    tempdir = os.path.join(targetDirectory, "temp")
    if os.path.exists(tempdir):
        answer = input("Im Zielverzeichnis existiert bereits ein Ordner namens \"temp\".\n Soll dieser überschriben werden? (y/n)")
        if answer=="y" or answer == "yes" or answer == "j":
            rmFolderContents(tempdir) # Verzeichnis leeren
        else:
            return
    else:
        os.mkdir(tempdir) # Verzeichnis erstellen
    ##
    try:
        with ZipFile(downloadedFile, 'r') as zipDownload:
            zipDownload.extractall(targetDirectory)
    except:
        print("Could not unzip Download")
        return
    
    ##
    print("Finding files")
    for d in os.listdir(targetDirectory):
        if(d != "temp"):
            folders.append(os.path.join(targetDirectory, d)) # memorize paths to all folders which contain the zipped projects
    
    for f in folders:
        files.append(os.path.join(f, os.listdir(f)[0])) # memorize paths to all the zipped projects
    print("\t", len(files), "files found")

    nonFaultyProjects=[]
    print("\nUnzipping")
    a = 0
    for f in files: # unzip all projects into target directory
        try:
            with ZipFile(f, 'r') as zp:
                rmFolderContents(tempdir) # Temp Verzeichnis leeren
                zp.extractall(tempdir) # Erstmal ins Tempdir extracten, um Anforderungen zu prüfen
                ## Check Subfolder requirements
                if len(os.listdir(tempdir)) == 0:
                    print("leere Abgabe: ", f)
                    a +=1
                    continue
                elif len(os.listdir(tempdir)) > 1:
                    print("Falsches Abgabeformat: ", f)
                    a +=1
                    continue
                else:
                    projectName=os.listdir(tempdir)[0]
                    if("NACHNAME_VORNAME" in projectName):
                        print("Abgabename unverändert: %s für Verzeichnis: %s" % (projectName, f))
                        a +=1
                        continue
                    shutil.move(os.path.join(tempdir, projectName), targetDirectory) #Move out of temp folder
                    shutil.rmtree(folders[a])
                    nonFaultyProjects.append(projectName)
        except Exception as e:
            print("\tunzipping failed for file %s with exception %s" % (f,e))
        a +=1
    print("\nCopy Testbenches into Projects")
    print("Benches:",testbenches)
    for d in nonFaultyProjects:    # copy all the testbenches into all the Projects
        try:
            s = os.path.join(targetDirectory, d, "src", "h01")
            for tb in testbenches:
                shutil.copy(tb, s)
        except Exception as e:
            print("\ttestbench copy failed for file %s. Reason %s" % (d, e))
    print("\nCleanup...")
    shutil.rmtree(tempdir) # Remove temp folder
    print("\nAll done :)")
def rmFolderContents(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
do()
quit()
