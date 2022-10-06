import vim

# get file vim.eval("expand('%:p')")
# get directory vim.eval("expand('%:p:h')")

class Klasse:

    def initPython(self) -> None:
        print("Es hat funktionier")
        print(vim.eval("expand('%:p')"))
        return True
    
    def buildJava(self) -> None:
        pass
        
