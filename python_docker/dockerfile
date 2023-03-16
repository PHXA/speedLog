FROM python

RUN apt update
RUN pip install --upgrade pip
RUN pip install requests
RUN apt install speedtest-cli -y

COPY m.py .

CMD python m.py