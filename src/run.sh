#/bin/bash

set -o errexit
set -o pipefail

# Make sure that django's `collectstatic` has been run locally before pushing up to any environment,
# so that the styles and static assets to show up correctly on any environment.

gunicorn --workers=3 --worker-class=gevent registrar.config.wsgi -t 60
