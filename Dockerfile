FROM python:3.9

WORKDIR /kenny

COPY . .

RUN pip install -r requirements.txt

CMD ["python","dockermain.py"]