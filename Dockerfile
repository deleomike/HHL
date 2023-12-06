FROM python:3.8

WORKDIR app

RUN pip install --upgrade pip setuptools wheel

RUN apt-get update -y && \
    apt-get install -y libhdf5-serial-dev libhdf5-dev

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY HHL.ipynb ./

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8000", "--allow-root"]