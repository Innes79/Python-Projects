import time
import os
import sys
print('\x1b[?25l', end='')
while True:
    seconds = time.time()
    local_time = time.ctime(seconds)
    os.system("cls" if sys.platform=="win32" else "clear")
    print(f"\r{local_time}"+" UTC Timezone", end="", flush=True)
    time.sleep(1)
