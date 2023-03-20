
import plotly.graph_objects as go
import glob
import numpy as np
import datetime
from pytz import timezone
from dateutil import parser

tags=[int(i.split(":")[-1].split(".")[0]) for i in glob.glob("./result/*")]
tag=max(tags)

SM = 2

f_p=f"./result/speed:{tag}.tsv"

fig=go.Figure()

with open(f_p,"r") as f:
  next(f)
  date=[]
  download=[]
  upload=[]
  for i in f:
    d,dow,up = i.split("\t")
    d = datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S.%f')
    j_d=d+datetime.timedelta(hours=9) # to jst
    if (not dow=="none") and (not up == "none"):
      date.append(j_d)
      download.append(float(dow))
      upload.append(float(up))

def smooth(i):
  a=[]
  for j in range(len(i)):
    if j-SM>=0:
      lf=j-SM
    else:
      lf=0
    a.append(np.mean(i[lf:j+SM]))
  return a

download=smooth(download)
upload=smooth(upload)

fig.add_trace(
  go.Scatter(
    x=date,
    y=download,
    mode="lines+markers",
    name="Download"
  )
)

fig.add_trace(
  go.Scatter(
    x=date,
    y=upload,
    mode="lines+markers",
    name="Upload"
  )
)

fig.show()