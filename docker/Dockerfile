FROM python:3.10
EXPOSE 1337
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY ./ .
CMD ["/bin/bash", "docker-entrypoint.sh"]