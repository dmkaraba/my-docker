FROM redis
HEALTHCHECK CMD redis-cli PING || exit 1
CMD ["redis-server"]