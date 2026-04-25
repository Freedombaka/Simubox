from datetime import datetime
import runpy
now = datetime.now()


print("The game started on", now)
time.sleep(1)
runpy.run_path(path_name="script/renderer.py")