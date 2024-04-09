# pip install eel

import eel

eel.init('UI')

@eel.expose
def App():
    print('Application Running Sucessfully')
  
App()

eel.start('index.html')
