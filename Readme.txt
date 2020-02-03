# REDIS DOCKER
docker run --name redis-cnt -d redis

# PUBLISHER DOCKER
# build
cd publicher
docker build -t publicher .
# run
docker run --name pub-app --rm -p 5000:5000 --link redis-cnt:redis -d publicher

# SUBSCRIBER DOCKER
# build
cd subscriber
docker build -t subscriber .
# run
docker run --name sub-app --rm -v <this/directory/>:/var/log/ --link redis-cnt:redis -d subscriber
