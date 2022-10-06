import vim, subprocess

# get file vim.eval("expand('%:p')")
# get directory vim.eval("expand('%:p:h')")

class Klasse:

    def getDir(self) -> str:
        return vim.eval("expand('%:p:h')")

    def getFileDir(self) -> str:
        return vim.eval("expand('%:p')")
    
    def getFileType(self) -> str:
        return vim.eval("&filetype")

    def initPython(self) -> None:
        print("Es hat funktionier")
        print(vim.eval("expand('%:p')"))
        return True
    
    def Build(self) -> None:
        if getFileType() == "java":
            subprocess.run(f"javac {getFileDir()}")
            return True
        print("Filetype not supported")
        return True
    
    def Run(self) -> None:
        if getFileType() == "java":
            subprocess.run(f"javac {getFileDir()}")
            subprocess.run(f"java {getDir()}")

        
