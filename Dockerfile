FROM python:3.9

ADD . .

RUN pip install --upgrade pip

CMD ["python","-m", "unittest", "discover", "-s", "Tests"]