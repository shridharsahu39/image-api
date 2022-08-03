# This file is a template, and might need editing before it works on your project.
FROM python:3.9-alpine

# Edit with mysql-client, postgresql-client, sqlite3, etc. for your needs.
# Or delete entirely if not needed.


WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

# For Django



# For some other command
EXPOSE 5000
CMD ["python", "app.py"]
