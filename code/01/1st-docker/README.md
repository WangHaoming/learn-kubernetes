build a image 
```
docker build -t flask-simple-app .

```

run the docker image

```
docker run -d -p 8080:5000 --name my-flask-web flask-simple-app 
```


access the web server 

```
curl localhost:8080
```
