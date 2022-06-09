FROM python:3.9

WORKDIR /kenny

COPY . .

RUN pip install -r requirements.txt
RUN echo 1 | sudo tee /proc/sys/vm/overcommit_memory
CMD ["python","dockermain.py"]