why?
-> To install packages that are specific to certain project. 
-> Each project should have its own packages seperated from each other.

windows venv commands:

python -m venv c:\path\to\myenv
C:\> <venv>\Scripts\activate.bat
pip install -r requirements.txt
deactivate (no longer active but still exists)
rmdir c:\path\to\myenv /s

To access global python system packages:

python -m venv c:\path\to\myenv --system-site-packages
C:\> <venv>\Scripts\activate.bat
pip list --local (to list the packages installed only on venv)
pip freeze --local

Tip: copy the packages from pip freeze and save it on requirements.txt
