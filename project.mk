PROJECT_NAME := django-zodb

django-project:
	django-admin startproject backend . --template https://github.com/aclark4life/django-zodb-project/archive/refs/heads/main.zip 

django-settings-base:
	@echo "$$DJANGO_SETTINGS_BASE" >> $(DJANGO_SETTINGS_BASE_FILE)
	@echo "$$DJANGO_SETTINGS_AUTHENTICATION_BACKENDS" >> $(DJANGO_SETTINGS_BASE_FILE)
	@echo "$$DJANGO_SETTINGS_REST_FRAMEWORK" >> $(DJANGO_SETTINGS_BASE_FILE)
	@echo "$$DJANGO_SETTINGS_INSTALLED_APPS" >> $(DJANGO_SETTINGS_BASE_FILE)
	@echo "$$DJANGO_SETTINGS_MIDDLEWARE" >> $(DJANGO_SETTINGS_BASE_FILE)
	@echo "$$DJANGO_SETTINGS_CRISPY_FORMS" >> $(DJANGO_SETTINGS_BASE_FILE)

clean:
	rm -rvf backend/
	rm -vf manage.py
	rm Data.fs.*


dump:
	python manage.py dumpzodb
