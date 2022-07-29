FROM python:3.8-slim-buster

# Set environment variables
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y --no-install-recommends \
        libgdal-dev \
        g++ \
        gcc && \
pip install numpy==1.18.1 && \
pip install gdal==2.4.0 && \
        apt remove -y gcc g++ && \
        rm -rf /var/lib/apt/lists/*

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Install dependencies.
# Set work directory.


# Copy project code.
COPY . /code/

EXPOSE 8080

CMD ["uwsgi", "--http", ":8080", "--ini", "./uwsgi/uwsgi.ini"]