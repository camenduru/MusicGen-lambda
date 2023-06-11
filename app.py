import os
os.system(f"git lfs install")
os.system(f"git clone -b dev https://github.com/camenduru/audiocraft /home/demo/source/audiocraft")
os.chdir(f"/home/demo/source/audiocraft")
os.system(f"pip install -r requirements.txt")
os.system(f"python app.py --port 8266")