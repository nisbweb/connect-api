# connect-api
API Server for NISB Connect


## To run this:
- install python 3.5+
- install pip
- `pip3 install virtualenv`
- `virtualenv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python3 main.py`

## Swagger Spec:
Inside openapi/swagger.yaml

# Dev Guide
- The views are inside `views` folder.
- There is direct mapping of swagger spec and view functions
- We use mongo DB
- Use github issues to report bugs and track features
- Comment code always