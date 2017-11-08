## Evedom Demonstration

This is to demonstrate the [evedom](https://github.com/nam4dev/evedom) python package.

### Installation & Setup

##### Prerequisites

Setup a MongoDB database.

##### Virtualenv (recommended)

Create a dedicated virtual environment.

##### Setup MongoDB info

In the `settings.py` file,
update mongo database info directly (development mode)

or set environment variables accordingly.

```python
MONGO_HOST = os.environ.get('MONGO_HOST', '127.0.0.1')
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
MONGO_USERNAME = os.environ.get('MONGO_USERNAME')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME')
```

##### Clone the repo

```bash
# cd /your/projects/folder (optional)
git clone https://github.com/nam4dev/evedom_demo.git
cd evedom_demo
```

##### Install dependencies

```bash
# . /virtualenv/bin/activate
pip install -r requirements.txt
```

##### Run the application

```bash
python wsgi.py
```

##### Open the browser

Your application shall run @[http://127.0.0.1:5000](http://127.0.0.1:5000)

That's all folks!

