if !has('python3')
    echomsg ':python3 is not available, initialisierung will not be loaded.'
    finish
endif

python3 import nilspolek.initPlk
python3 test = nilspolek.initPlk.Klasse()


command! Build python3 test.Build()
command! Rub python3 test.Run()
command! Pythoninit python3 test.initPython()
