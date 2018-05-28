# include the routines so we can access the chip data
from gpiozero import MCP3008

# we want to delay processing so need this library too
import time

# do forever
while (1):

	#read the value from channel 0 (you can use any or all of the channels, 0 to 7)
    adc= MCP3008(channel=0, device=0)
	
	# print the output in a formatted manner, without decimal places
	# the original line was:
	# print(adc.value * 1023)
    print('{:.0f}'.format(adc.value * 1023))
	
	# delay for half a second
    time.sleep(0.5)

# End of program