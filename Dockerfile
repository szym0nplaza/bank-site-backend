FROM python:3.9
WORKDIR /src
COPY ./requirements/ ./
RUN pip install -r base.txt
COPY . .
CMD [ "python", "src/main.py" ]
RUN bash ./scripts/setup.sh