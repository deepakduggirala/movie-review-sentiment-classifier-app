```
curl localhost:3000/predict -X POST -H 'content-type: application/json' -d '{"review": "N.T.R, Savitri, A.N.R in Mayabazar acted brilliantly. Dialogues look fresh!!!. Music and lyrics are super."}'

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
`docker build -t movie-review-sentiment-classifier .`
##### docker push docker.target.com/iag-ime/zscaler-sync
`docker rmi $(docker images --filter "dangling=true" -q --no-trunc)`
### Run docker container
`docker run --rm -p 3000:3000 movie-review-sentiment-classifier`

# Hosting
https://www.reddit.com/r/docker/comments/bxvoak/free_docker_hosting/
