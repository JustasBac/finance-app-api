FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["/bin/bash", "docker-entrypoint.sh"]