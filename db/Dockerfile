FROM postgres:alpine
ENV POSTGRES_PASSWORD=secret
ENV POSTGRES_USER=username
ENV POSTGRES_DB=db
COPY create_fixtures.sql /docker-entrypoint-initdb.d/create_fixtures.sql
