if !has('python3')
    echomsg ':python3 is not available, initialisierung will not be loaded.'
    finish
endif

python3 import nilspolek.initPlk
python3 init = nilspolek.initPlk.InitPlk()

command! Pythoninit python3 init.initPython()
