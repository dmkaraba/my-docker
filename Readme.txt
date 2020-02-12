# BUILD
docker build -t redis docker_redis/.
docker build -t publisher --build-arg app=pub_app.py --build-arg healthcheck=pub_healthcheck.sh docker_app/.
docker build -t subscriber --build-arg app=sub_app.py --build-arg healthcheck=sub_healthcheck.sh docker_app/.

# RUN
docker run --rm --name redis-cnt -d redis
docker run --rm --name pub-app --link redis-cnt:redis -d -p 5000:5000 publisher
docker run --rm --name sub-app --link redis-cnt:redis -d -v D:/dev/my-docker/docker_app/:/var/log/ subscriber

Or build dockers and run them via launch_dockers.py
It will run 3 dockers and start async_watchdog.py