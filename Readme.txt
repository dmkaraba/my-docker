# REDIS DOCKER
docker run --name redis-cnt -d redis

# PUBLISHER DOCKER
# build
cd publisher
docker build -t publisher .
# run
docker run --name pub-app --rm -p 5000:5000 --link redis-cnt:redis -d publisher

# SUBSCRIBER DOCKER
# build
cd subscriber
docker build -t subscriber .
# run
docker run --name sub-app --rm -v <this/directory/>:/var/log/ --link redis-cnt:redis -d subscriber
