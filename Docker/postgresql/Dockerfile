FROM postgres:latest

ENV POSTGRES_USER=test
ENV POSTGRES_PASSWORD=123321
ENV POSTGRES_DB=test

COPY ./init.sql /docker-entrypoint-initdb.d/

CMD ["postgres"]
