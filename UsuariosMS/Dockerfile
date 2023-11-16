FROM python:3.11-alpine
RUN apk add --no-cache bash
RUN apk add gcc musl-dev mariadb-connector-c-dev
COPY test_backend_est_app UsuariosMS
RUN pip install -r /UsuariosMS/requirements.txt
EXPOSE 8000
