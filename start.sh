#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset


python /project/manage.py migrate
python /project/manage.py /runserver 0.0.0.0:8000
