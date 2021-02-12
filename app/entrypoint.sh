#!/bin/sh

# This finds where on the disk this script is located
# with the assumption that the app.py file is right next
# to it. Allowing for execution of this script from any
# location on the disk within the context of the app directory.
# This allows for using relative paths within our Python application
# that should always resolve without needing to `cd` manually first.
ENTRYPOINT_PATH="$( cd "$(dirname "$0")"; pwd -P )"
cd "$ENTRYPOINT_PATH"

# pipenv run python app.py "$@"
pipenv run python app.py "$@"
