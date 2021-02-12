FROM python:3.9
# Adds Pipfile and Pipefile.lock into the image in the /app folder.
COPY Pipfile* /app/
# Set the initial working directory for the image to the /app folder
WORKDIR /app
# In conjuction with copying the Pipfile & Pipefile.lock above
# this will install the pipenv tool, and then install all of the
# defined dependencies for this application as part of the image.
RUN pip install --upgrade pip pipenv && \
    pipenv lock -v --keep-outdated --requirements > requirements.txt && \
    pip install -r requirements.txt && \
    spacy download en_core_web_md

# RUN pip install --upgrade pip pipenv && \
#     pipenv install --deploy && \
#     spacy download en_core_web_md
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
ENTRYPOINT ["/app/entrypoint.sh"]
# Advertise to the end user & Docker, that this image will listen on
# port 8050.  This doesn't explicitly open the port up, but it's more
# of a suggestion to people on how to use the image.
EXPOSE 80