# api-visited-urls
This service provides 2 HTTP resources: for loading links (POST) and for displaying ingormation about visited domains (GET).


### CodeClimate and CI status

<a href="https://codeclimate.com/github/Dddarknight/api-visited-urls/maintainability"><img src="https://api.codeclimate.com/v1/badges/f36de6461d70240a3424/maintainability" /></a> <a href="https://codeclimate.com/github/Dddarknight/api-visited-urls/test_coverage"><img src="https://api.codeclimate.com/v1/badges/f36de6461d70240a3424/test_coverage" /></a> [![Python CI](https://github.com/Dddarknight/api-visited-urls/actions/workflows/pyci.yml/badge.svg)](https://github.com/Dddarknight/api-visited-urls/actions)

## Links
This project was built using these tools:
| Tool | Description |
|----------|---------|
| [FastAPI](https://fastapi.tiangolo.com/) | "Web framework for building APIs with Python" |
| [Redis](https://redis.io/) |  "The open source, in-memory data store" |
| [poetry](https://python-poetry.org/) |  "Python dependency management and packaging made easy" |
| [Py.Test](https://pytest.org) | "A mature full-featured Python testing tool" |

## Installation and launch
```
$ git clone git@github.com:Dddarknight/api-visited-urls.git
$ pip install poetry
$ make install
$ make run

```

## Description and usage
|   | Description |
|----------|---------|
| POST /visited_links |  Post visited links to Redis database. |
| GET /visited_domains?from=1545221231&to=1545217638 | Get links which were visited during specified period of time. |

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
