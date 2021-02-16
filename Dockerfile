FROM python:3.9-buster
# Adds Pipfile and Pipefile.lock into the image in the /app folder.

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Set the initial working directory for the image to the /app folder
ENV APP_HOME /app
WORKDIR $APP_HOME

COPY Pipfile* /app/

# In conjuction with copying the Pipfile & Pipefile.lock above
# this will install the pipenv tool, and then install all of the
# defined dependencies for this application as part of the image.
RUN pip install --upgrade pip pipenv && \
    pipenv lock -v --keep-outdated --requirements > requirements.txt && \
    pip install -r requirements.txt && \
    python -c "import nltk;nltk.download('stopwords');nltk.download('wordnet')"

# RUN pip install --upgrade pip pipenv && \
#     pipenv install --deploy

# The app folder is copied towards the end of the image creation
# since it tends to change more often than the previous steps,
# and therefore we can take advantage of Docker's caching to speed
# up subsequent builds which leads to a faster build/rebuild cycle.
COPY app /app

# When Docker starts the image instance (as a container) it will look at
# either the ENTRYPOINT or CMD directives and run those applications.
# Their usage is nuanced and situational dependent, but for now
# ENTRYPOINT is sufficient.
# Read this https://forums.docker.com/t/docker-run-cannot-be-killed-with-ctrl-c/13108/2 
# to know why a single string is included in an array
# ENTRYPOINT ["/app/entrypoint.sh"]


# Advertise to the end user & Docker, that this image will listen on
# port 8050.  This doesn't explicitly open the port up, but it's more
# of a suggestion to people on how to use the image.
# EXPOSE 8080

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app