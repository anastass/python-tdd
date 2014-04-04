python-tdd
==========

Python version of perl-tdd

## Links
- [Python Testing](http://pythontesting.net/start-here/)
- [Improve Your Python: Understanding Unit Testing](https://www.jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/)
- [Improve Your Python: Decorators Explained](https://www.jeffknupp.com/blog/2013/11/29/improve-your-python-decorators-explained/)

## Miscellaneous

### Install pip and virtualenv
- download get-pip.py from [pip](http://pip.readthedocs.org/en/latest/installing.html) website
- run pip __get-pip.py__ command
- install virtualenv with __pip install virtualenv__ command
- create environment: __virtualenv env__
- activate environment with __env\scripts\activate__
- "freeze" environment with __pip feeze >requirements.txt__
	Note: To update requirements.txt use:
		__pip feeze -r requirements.txt >requirements.txt__ 
- exclude __env__ from git.
	Note: Virtual enviroment for Python27 can be re-created with: 
		virtualenv --python=C:\Python27\python env
		pip install -r requirements.txt

		# start project using env\scripts\python
		PyScripter.exe --project=python-tdd.psproj --python27 --pythondllpath=env\Scripts\
- deactivate enviromnet when finish __env\scripts\deactivate__

To search for a package use:
	pip search flask									# search for a package (in this case flask)
	pip install flask									# install flask package
	pip feeze -r requirements.txt >requirements.txt 	# update requirements.txt
	pip deinstall flask									# de-install the package