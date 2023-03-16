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
    a=a.split()
    with open(f_p,"a") as f:
      f.write(f"{datetime.datetime.now()}\t{a[29]}\t{a[35]}\n")
  e=time.time()
  time.sleep(max(DURATION_SEC-(e-s),0))