FROM python:3.6

# create and set working directory
RUN mkdir /app
WORKDIR /app

# install packages
COPY ./requirements/dev.txt /app/requirements/dev.txt
COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

# Add current directory code to working directory
ADD . /app
RUN chmod +x ./docker/dev/entrypoint.sh

EXPOSE 5000
ENTRYPOINT ["./docker/entrypoint.sh"]