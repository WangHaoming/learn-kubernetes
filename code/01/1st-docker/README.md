build a image 
```
docker build -t flask-simple-app .

```

run the docker image

```
docker run -d -p 8080:5000 --name my-flask-web flask-simple-app 
docker run -d -p 8080:5000 --name my-flask-web wanghaoming/flask-simple-app:v1.0
```


access the web server 

```
curl localhost:8080
```

push to docker hub

```
docker tag flask-simple-app wanghaoming/flask-simple-app:v1.0
docker push wanghaoming/flask-simple-app:v1.0
```


install docker 

```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

```


