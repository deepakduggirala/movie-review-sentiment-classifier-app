```
curl https://movie-review-sentiment-clf-zrefb57tqq-uc.a.run.app/predict -X POST -H 'content-type: application/json' -d '{"review": "The Movie Was So Cool! I Want To Watch The Again And Again!"}'

curl localhost:3000/predict -X POST --data "@reviews/review-1.json" -H 'content-type: application/json'
```

### Install pipenv

https://realpython.com/pipenv-guide/

`pip install pipenv`

`pipenv shell`

`pipenv install flask`

`pipenv install numpy beautifulsoup4 unidecode contractions spacy nltk`

`spacy download en_core_web_md`

`pipenv lock`

### Run application
`python app.py`

### Run application without creating pipenv shell
`pipenv run python app.py`

### Build docker container
`docker build -t us.gcr.io/movie-review-sentiment-clf/movie-review-sentiment-clf .`
##### docker push docker.target.com/iag-ime/zscaler-sync
`docker rmi $(docker images --filter "dangling=true" -q --no-trunc)`
### Run docker container
`docker run --rm -p 80:80 movie-review-sentiment-classifier`

## Stopping flask in docker
https://github.com/docker/compose/issues/4199

# Hosting
free https://www.reddit.com/r/docker/comments/bxvoak/free_docker_hosting/

# Amazon Web Services
Follow this guide: https://towardsdatascience.com/simple-way-to-deploy-machine-learning-models-to-cloud-fd58b771fdcf

```
sudo amazon-linux-extras install docker
sudo yum install docker
sudo service docker start
sudo usermod -a -G docker ec2-user
```


I'm using the ubuntu vm as the aws vm had problems with running docker
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04

```
sudo apt-get install software-properties-common
sudo apt-add-repository universe
sudo apt-get update
sudo apt-get install python3-pip
```

https://www.liquidweb.com/kb/how-to-install-pyenv-on-ubuntu-18-04/

# Google Cloud Run
How to avoid pipeline errors when running with gunicorm: https://rebeccabilbro.github.io/module-main-has-no-attribute/