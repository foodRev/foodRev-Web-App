# foodRev Web App

Quick and scalable deployment of a food donation webapp

## Project Aims:

 - open source
 - easy to deploy
 - easy to maintain
 - easy to _extend_
 - great documentation and support
 
## Setup
 
### Set Up Google App Engine

[link to official documentation](https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env)

### Set Up Python Requirements

Be sure to add the following requirements:

`pip install -r requirements.txt -t lib`

## Running Locally

execute the following from the project's root dir:

`dev_appserver.py app.yaml`

## Deploying

Run the following from the root directory of the project:

`gcloud app deploy`


