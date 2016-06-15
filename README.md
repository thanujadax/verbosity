# Setting up the environment
This project uses python version 3.4 along with anaconda package manager. Following instructions will guide you to set up the programming environment.
The name of the conda environment is *projectverbosity*
## Install Git
### Windows
Installation instructions can be found [here](https://desktop.github.com/)

### General
Installation instructions can be found [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Install anaconda
Installation instructions can be found [here](https://docs.continuum.io/anaconda/install)

## Install SDL
Installation instructions can be found [here](https://wiki.libsdl.org/Installation)

## Install PyGame dependencies (Linux only)
### Ubuntu
```
sudo apt-get build-dep python-pygame
```
## Clone the project
```
git clone https://github.com/thanujadax/verbosity.git
```
This will create a directory called `verbosity`

## Setting up conda environment
To change into the source directory `verbosity`:
```
cd verbosity
```

To set up the conda environment:
```
conda env create -f environment.yml
```
This will create a conda environment called *projectverbosity*

To activate the environment:
```
source activate projectverbosity
```

# Usage
The main application is contained in the python module in `verbosity/gui/MainWindow.py`

Make sure you have the most recent version of the `master` branch of the git repository
```
git pull origin master
```

Navigate into the subdirectory `verbosity/gui`
To invoke the application:
```
python MainWindow.py
``` 
