# CoinIntegro
Simple web-app with CoinGate integration.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

```
- Python 3.6+ with PIP
- some Linux distributive recommended
```

### Local deploy

1) In the selected directory create project folder and initiate git repository there.

2) In root project folder create and activate virtual environment:

```
$ python3.6 -m venv env
$ . env/bin/activate
```

3) Install all the dependencies:

```
$ pip install -r requirements.txt
```

4) Fix coingate library. In coingate.clients.py:

```
from urlparse import urlunparse, urljoin
```
replace with:
```
from urllib.parse import urlunparse, urljoin
```

5) Create and fill .env with .env.example:

```
$ python manage.py runserver
```

6) Then run the server:

```
$ python manage.py runserver
```

 App is ready!
 