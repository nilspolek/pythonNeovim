import vim

class Klasse:

    def initPython(self) -> None:
        print("Es hat funktionier")
        print(vim.eval("expand(%:t:r)"))
        return True
    
    def buildJava(self) -> None:
        pass
        
