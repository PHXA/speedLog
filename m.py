import subprocess
import time, datetime

DURATION_SEC=10*60

f_p = "/result/speed.tsv"
with open(f_p,"w") as f:
  f.write("time\tdownload[Mbit/s]\tupload[Mbit/s]\n")

while 1:
  s=time.time()
  a=subprocess.run("speedtest", capture_output=True, text=True).stdout
  if not "ERROR" in a:
    a=a.split("\n")
    Download="none"
    Upload="none"
    for i in a:
      if "Download:" in i:
        Download = i.split(" ")[1]
      if "Upload:" in i:
        Upload = i.split(" ")[1]
    with open(f_p,"a") as f:
      f.write(f"{datetime.datetime.now()}\t{Download}\t{Upload}\n")
  e=time.time()
  time.sleep(max(DURATION_SEC-(e-s),0))