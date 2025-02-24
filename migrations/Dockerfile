FROM postgres:13-alpine

COPY ./migrations/init_tables.sql /migrations/init_tables.sql

RUN chown -R postgres:postgres /migrations

USER postgres