import vim, subprocess

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
        print(vim.eval("expand('%:p')"))
        return True
    
    def build(self) -> None:
        if getFileType() == "java":
            subprocess.run(f"javac {getFileDir()}")
            return True
        print("Filetype not supported")
        return True
    
    def run(self) -> None:
        if getFileType() == "java":
            subprocess.run(f"javac {getFileDir()}")
            subprocess.run(f"java {getDir()}")

        
