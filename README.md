[![Build Status](https://travis-ci.org/maperghis/stan_coding_challenge.svg?branch=master)](https://travis-ci.org/maperghis/stan_coding_challenge)
# Stan Coding Challenge
Welcome to the Solution to the [Stan Coding Challenge](https://challengeaccepted.streamco.com.au/)!
Please read [My Solution](solution.md) for reasonings behind my choice of
language and framework.

## The Challenge
Receive a post request with some JSON data to my given URL, filter the data and
return a few fields. You can see the example request and response json files
under the resources/ directory.

### Details
From the list of shows in the request payload, return the ones with DRM enabled
(drm: true) and at least one episode (episodeCount > 0).

The returned JSON should have a response key with an array of shows. Each
element should have the following fields from the request:

* image - corresponding to image/showImage from the request payload
* slug
* title

### Error Handling
If we send invalid JSON, You'll need to return a JSON response with HTTP status
400 Bad Request, and with a `error` key containing the string Could not decode
request. For example:

```json
{
    "error": "Could not decode request: JSON parsing failed"
}
```

## Solution

### Deployment
URL this app is deployed using [Heroku](https://devcenter.heroku.com/) at
https://stan-movie-filter.herokuapp.com/.

Using [HTTPie](http://httpie.org/), post resources/request.json to receieve
HTTP 200 OK with filtered JSON response.
```shell
http POST https://stan-movie-filter.herokuapp.com/ Content-Type:application/json < resources/request.json
```

Post resources/invalid.json to receive HTTP 400 Bad Request with an error
message.
```shell
http POST https://stan-movie-filter.herokuapp.com/ Content-Type:application/json < resources/invalid.json
```

Receive HTTP 415 Unsupported Media Type for all Content-Types except JSON.
```shell
http POST https://stan-movie-filter.herokuapp.com/ Content-Type:application/json < resources/invalid.json
```

## Getting Started

### Prerequisites
* Python2.7
* Virtualenv

### Installation
```shell
source env/bin/activate
pip install -r requirements.txt
```

### Run App Locally
Start app.
```shell
gunicorn --reload ''stan_coding_challenge.app:get_app()''
```

Post resources/request.json to local URL.
```shell
http POST localhost:8000/ Content-Type:image/png < resources/request.json
```

### Running Tests
From the main stan_coding_challenge directory run tests:
```shell
pytest tests
```
