# KiTimer(きたいま)

KiTimer is timer for workers.

[![Circle CI](https://circleci.com/gh/pistatium/kitimer/tree/master.svg?style=svg)](https://circleci.com/gh/pistatium/kitimer/tree/master)


## Features
* Logging arrived time
* Logging left time
* Logging joined projects each day.

## Setup
```
git clone  kitimer
cd kitimer
mkvirtualenv kitimer --python=`which python3`
pip install -e .
kitimer syncdb
# Create superuser
```


## Runserver
```
kitimer runserver

open localhost:8000/admin
# Login with superuser
# Create User and Projects

open localhost:8000
# Timer Toppage
```
