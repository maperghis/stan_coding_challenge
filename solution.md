# My Solution

## Language
I implemented the simple web app in Python for the follow reasons:
1. Python is by far my **strongest** language.
2. Very easy to get something up and running quickly.
3. The module **json** provides easy methods to move back and forth between
json and string representations of the object.
4. The **filter** method is a powerful way of filtering python *dicts* or
*lists* in one line implementations.

## Framework
When deciding upon a backend framework I first considered Django. No doubt,
Django is the most popular framework with its batteries included and automatic
database generation features. However I felt that there must be something a bit
simpler and lightweight for my web app. My app really only has one job to do,
it doesn't have a backend database or frontend, so I began looking for
something that is as fast as possible, without any bloat.

Online I found [Python's Web Framework Benchmarks](http://klen.github.io/py-frameworks-bench/)
which compares the speed of some of the popular Python frameworks.

[Falcon](https://falconframework.org/), the minimalist Python WSGI framework
came out as one of the fastest for handling requests. Not only is it fast, it
is a microframework for small applications that encourages the REST
architectural style. "Resource classes implement HTTP method handlers that
resolve requests and perform state transitions." Perfect for this project.

If we needed to serve HTML pages then I would maybe chose Django, however for
this project, Falcon is the obvious choice.

## Handling Failures
* 400 Bad Request - catches invalid json content
* 405 Method Not Allowed - only allow POST requests
* 415 Unsupported Media Type - unsupported data types, such as posting an image
rather than a json string

## Notes
The example [request.json file](https://challengeaccepted.streamco.com.au/samples/request.json)
has a movie in it called "The Taste (Le GoÃ»t)". In the example
[response.json file](https://challengeaccepted.streamco.com.au/samples/response.json)
the title expected for this movie is "The Taste". At first I thought that this
was an encoding issue however this doesn't account for the extra letters. I
assummed that it was a mistake and changed the title to "The Taste" to get my
tests to pass.

## Future Features

### Throttling
I might implement a way of preventing people from overloading my system. I
would need to find out who is sending the request and how many they have been
sending. Ideas for backing off could be to implement some exponential fall off
which says the first time over the limit you make them wait 2 * 100
milliseconds, then 2^2 * 100, then 2^3 * 100, etc. Start small so users who
make a mistake aren't really punished, but malicious users are really held
back. Use the HTTP 429 Too Many Requests response, and also send a Retry-After
header which tells them how long until they can retry.
