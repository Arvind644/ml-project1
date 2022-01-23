# water quality prediction project

We are making a water quality prediction model which tell the quality of water

## Problem description

In this project, we are predicting quality of water as it is suitable to drink or not. The model take variables and predict whether it is safe or note


## file structure

notebook.ipynb - main jupyter noetbook <br />
model.py - contain extract and main model from jupyter noetbook.  <br />
predict.py - it perdict the result. <br /> 
predict-test.py - contain sample data <br /> 
model_C.bin - it saveds the model. <br />
Dockerfile - to riun the application in docker image

## Deployment of model

I am currently using Windows, so I am using waitress in order to deploy the model. To deploy this model with waitress, please use: waitress-serve --listen=0.0.0.0:9696 predict:app

# Docker

If you choose to build a docker file locally instead, here are the steps to do so:

In your command line, run: docker run -it --rm --entrypoint=bash python:3.8.12-slim to create a docker image.

Create a Dockerfile as such:
````
```
FROM python:3.8.12-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["predict.py", "catboostreg.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["waitress-serve", "--listen=0.0.0.0:9696", "predict:app"]
```
````
This allows us to install python, run pipenv and its dependencies, run our predict script and our model itself and deploys our model using waitress. Similarly, you can just use the dockerfile in this repository.
