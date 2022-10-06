import vim, subprocess, os

# get file vim.eval("expand('%:p')")
# get directory vim.eval("expand('%:p:h')")

def getDir():
    return vim.eval("expand('%:p:h')")

def getFileDir():
    return vim.eval("expand('%:p')")

def getFileType():
    return vim.eval("&filetype")

class Klasse:

    def initPython(self) -> None:
        print("Es hat funktionier")
        print(getFileDir())
        return True
    
    def build(self) -> None:
        if getFileType() == "java":
            subprocess.run("javac {}".format(getFileDir()))
            return True
        print("Filetype not supported")
        return True
    
    def run(self) -> None:
        if getFileType() == "java":
            subprocess.run("javac {}".format(getFileDir()))
            fileWithoutEnd = os.path.splitext(getFileDir())[0]
            subprocess.run("java {}".format(fileWithoutEnd))
        
        if getFileType() == "Python":
            subprocess.run("python {}".format(getFileDir()))
        
