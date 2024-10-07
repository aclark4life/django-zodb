PROJECT_NAME := django-zodb

django-project:
	django-admin startproject backend . --template https://github.com/aclark4life/django-zodb-project/archive/refs/heads/main.zip 
	-$(GIT_ADD) backend/*.py
