if !has('python3')
    echomsg ':python3 is not available, initialisierung will not be loaded.'
    finish
endif

python3 import initialisierungPlug.initialisierungPlug
python3 initialierer = initialisierungPlug.initialisierungPlug.InitialisierungPlug()

command! Pythoninit python3 finder.initPython()
