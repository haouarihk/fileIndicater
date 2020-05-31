from os import listdir
from os.path import isfile, join

folderPath = 'test' # the folder path
extension = 'mp4' # the extention that you're looking for ( '*' if you want all files)

joinWith = ', ' # how do you want to join the names of the files
nameWithExtention = True # Will it has the extention with the name

def getAllFile(path):
    arrayOfFiles=[f for f in listdir(path) if isfile(join(path, f))]
    arrayOfFilesInFolders = [getAllFile(path+'/'+f) for f in listdir(path) if isfile(join(path, f))==False]
    return arrayOfFiles + arrayOfFilesInFolders

def filterList(array,globalfiles):
    files = [f for f in array if type(f)!=list]
    globalfiles += files
    files += [filterList(f,globalfiles) for f in array if type(f)==list]
    return  files

def getProps(path):
    name = '.'.join(path.split(".")[:-1])
    extension = path.split(".")[-1]
    return [name, extension]

def getOnlyWithExtension(filterExtentionFiles, extensionGoal):
    if (extension != '*'):
        return [('.'.join(f) if nameWithExtention else f[0])for f in filterExtentionFiles if f[1] == extensionGoal]
        
    return [('.'.join(f) if nameWithExtention else f[0])for f in filterExtentionFiles]


def main():
    globalfiles=[]
    filterList(getAllFile(folderPath), globalfiles)
    extendedFilteringExtention = [getProps(f) for f in globalfiles]
    files = getOnlyWithExtension(extendedFilteringExtention, extension)
    joinedFiles = ', '.join(files)
    print(joinedFiles)

main()