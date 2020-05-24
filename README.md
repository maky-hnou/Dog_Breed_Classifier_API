# Dog_Breed_Classifier_API  

![Python version][python-version]
[![GitHub issues][issues-image]][issues-url]
[![GitHub forks][fork-image]][fork-url]
[![GitHub Stars][stars-image]][stars-url]
[![License][license-image]][license-url]

## About this repo:  

An API for dog breeds classification.  
The API has been developed using *Django Framework*. While the classifier was created based on *transfer learning* technique using the Google **Inception V3** architecture.  

## Content of the repo:  
The project has been organized as follows:  
- `manage.py`: the python script used to run several commands (`runserver/makemigrations/maigrate` and the commands added by the the user).  
- `requirements.txt`: a text file containing the needed packages to run the project.  
- `Dog_Breed_Classifier/`: the folder containing the model,views, urls, serializer, migration files and the custom commands and the core of the app.  
- `Dog_Breed_Classifier/core`: the folder containing the model and the code used for the classification.  
- `Dog_Breed_Classifier/management/`: the folder that contains the custom commands.  
- `Dog_Breed_Classifier/migrations/`: the folder containing the migration files.  
- `Dog_Breed_Classifier_API/`: the folder that contains the api settings and the urls.  
- `media/`: the folder where the uploaded images will be saved.  
- `templates/`: the folder that contains the HTML, CSS and Javscript files.

## Run the app:  
*N.B:* use Python 3.6+  

**1. Clone the repo:**  
on your terminal, run `git clone https://github.com/maky-hnou/Dog_Breed_Classifier_API.git`
Then get into the project folder: `cd Dog_Breed_Classifier_API/`  

**2. Install requirements:**  
Before running the app, we need to install some packages.  
- *Optional* Create a virtual environment:  To do things in a clean way, let's create a virtual environment to keep things isolated.  
Install the virtual environment wrapper: `pip3 install virtualenvwrapper`  
Add the following lines to `~/.bashrc`:  
```
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV=~/.local/bin/virtualenv
source ~/.local/bin/virtualenvwrapper.sh
```
Run `source ~/.bashrc`.
Run `mkvirtualenv dog_classifier`
Activate the virtual environment: `workon dog_classifier` (To deactivate the virtual environment, run `deactivate`)
- Install requirements: To install the packages needed to run the application, run `pip3 install -r requirements.txt`  

**3. Run the app:**  
To run the application, you need to run the following command: `python3 manage.py runserver`.  
Then on your browser, open http://127.0.0.1:8000/.  






[python-version]:https://img.shields.io/badge/python-3.6+-brightgreen.svg
[issues-image]:https://img.shields.io/github/issues/maky-hnou/Dog_Breed_Classifier_API.svg
[issues-url]:https://github.com/maky-hnou/Dog_Breed_Classifier_API/issues
[fork-image]:https://img.shields.io/github/forks/maky-hnou/Dog_Breed_Classifier_API.svg
[fork-url]:https://github.com/maky-hnou/Dog_Breed_Classifier_API/network/members
[stars-image]:https://img.shields.io/github/stars/maky-hnou/Dog_Breed_Classifier_API.svg
[stars-url]:https://github.com/maky-hnou/Dog_Breed_Classifier_API/stargazers
[license-image]:https://img.shields.io/github/license/maky-hnou/Dog_Breed_Classifier_API.svg
[license-url]:https://github.com/maky-hnou/Dog_Breed_Classifier_API/blob/master/LICENSE
