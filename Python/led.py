import pyfirmata
import time
board=pyfirmata.Arduino('COM5')
Iter = pyfirmata.util.Iterator(board)

Iter.start()

x = board.get_pin('d:13:o')

while True:
	 x.write(1)
	 time.sleep(0.05)
	 x.write(0)
	 time.sleep(1)
	 