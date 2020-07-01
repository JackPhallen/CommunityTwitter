# TweetCommune

TweetCommune is a site for submitting tweets to a crowdsourced Twitter account.

## Installation

Make sure Python is installed on your machine.

```bash
apt-get install python3
```

Now clone the repository to your local machine. In the root of the repository, install requirements by running:

```bash
pip install -r requirements.txt
```

Make the necessary database migrations by running:

```bash
python3 manage.py migrate
```

## Running locally

To run a local version of the site, run the following:

```bash
python3 manage.py runserver
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
