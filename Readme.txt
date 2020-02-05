# BUILD
docker build -t publisher --build-arg app=pub_app.py docker_app/.
docker build -t subscriber --build-arg app=sub_app.py docker_app/.

# RUN
docker run --name redis-cnt -d redis
docker run --name pub-app --rm -p 5000:5000 --link redis-cnt:redis -d publisher
docker run --name sub-app --rm -v </some/directory/>:/var/log/ --link redis-cnt:redis -d subscriber

Or build dockers and run them via launch_dockers.py
It will run 3 dockers and start async_watchdog.py