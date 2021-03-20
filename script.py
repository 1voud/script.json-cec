import xbmc
import sys
import time

try:
    xbmc.log(str(sys.argv[1]), 2)
except:
    xbmc.log("Failed", 2)
        
if sys.argv[1] == 'command=activate':
    xbmc.executebuiltin('CECActivateSource')

elif sys.argv[1] == 'command=toggle':
    xbmc.executebuiltin('CECToggleState')

elif sys.argv[1] == 'command=standby':
    xbmc.executebuiltin('CECStandby')

elif sys.argv[1] == 'command=stop_and_standby':
    if xbmc.Player().isPlaying():
        xbmc.executebuiltin("PlayerControl(Stop)")
        time.sleep(3)
    xbmc.executebuiltin('CECStandby')
