###########
# BUILDER #
###########

FROM python:3.11.4-slim-buster as builder
WORKDIR /home/django

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

# lint
RUN pip install --upgrade pip
RUN pip install flake8==6.0.0
COPY . /usr/src/app/
RUN flake8 --ignore=E501,F401 .

COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt



#########
# FINAL #
#########

# pull official base image
FROM python:3.11.4-slim-buster

# create directory for the app user
RUN mkdir -p /home/django

# create the app user
RUN addgroup --system django && adduser --system --group django

# create the appropriate directories
ENV APP_HOME=/home/django
# RUN mkdir $APP_HOME
WORKDIR $APP_HOME
RUN mkdir $APP_HOME/staticfiles

# install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends netcat-traditional
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g'  $APP_HOME/entrypoint.sh
RUN chmod +x  $APP_HOME/entrypoint.sh

# copy project
# COPY ./saloncrm $APP_HOME/saloncrm
# COPY ./manage.py $APP_HOME
# COPY ./saloncrm-apps $APP_HOME


# chown all the files to the app user
RUN chown -R django:django $APP_HOME

# change to the app user
# USER django


# run entrypoint.sh
ENTRYPOINT ["/home/django/entrypoint.sh"]