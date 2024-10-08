# django-zodb

Inspired by https://github.com/osantana-archive/django-zodb

- No RelStorage
- Based on
    - https://github.com/mongodb-labs/django-mongodb
    - https://github.com/django-nonrel/mongodb-engine
    - https://github.com/django/django/tree/main/django/db/backends

## Project setup

Assuming you've cloned this repository:

```
pip install .
django-admin startproject backend . --template=https://github.com/aclark4life/django-zodb-project/archive/refs/heads/main.zip
```

## Reference

- https://medium.com/django-unleashed/how-does-django-manage-db-connections-4c1a009cec91

## Supported features

### Management commands

#### `python manage.py migrate` management command (show migrations only)

```
test-django-zodb git:main  
(test-django-zodb) ❯ python manage.py migrate
Setting autocommit to True
Closing cursor
Closing cursor
Operations to perform:
  Apply all migrations: account, admin, auth, authtoken, contenttypes, explorer, sessions, siteuser, socialaccount
Running migrations:
Closing cursor
Setting autocommit to False
Executing SQL: CREATE TABLE django_migrations (...); with params: ()
Setting autocommit to True
  Applying contenttypes.0001_initial...Setting autocommit to False
Executing SQL: CREATE TABLE django_content_type (...); with params: ()
Altering unique_together for django_content_type from () to {('app_label', 'model')}
Closing cursor
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['contenttypes', '0001_initial', '2024-08-05 15:42:25.207858+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying contenttypes.0002_remove_content_type_name...Setting autocommit to False
Altering field name to name in model django_content_type
Removing field name from model django_content_type
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['contenttypes', '0002_remove_content_type_name', '2024-08-05 15:42:25.210410+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying auth.0001_initial...Setting autocommit to False
Executing SQL: CREATE TABLE auth_permission (...); with params: ()
Executing SQL: CREATE TABLE auth_group (...); with params: ()
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['auth', '0001_initial', '2024-08-05 15:42:25.214662+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying auth.0002_alter_permission_name_max_length...Setting autocommit to False
Altering field name to name in model auth_permission
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['auth', '0002_alter_permission_name_max_length', '2024-08-05 15:42:25.216138+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying auth.0003_alter_user_email_max_length...Setting autocommit to False
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['auth', '0003_alter_user_email_max_length', '2024-08-05 15:42:25.217894+00:00']
Closing cursor
…
```

#### `python manage.py dbshell`

```
test-django-zodb git:main
(test-django-zodb) ❯ python manage.py dbshell
Running shell
Python 3.12.4 (main, Jun  6 2024, 18:26:44) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> root
<ZODB with tables: ['django_migrations', 'django_content_type', 'auth_permission', 'auth_group', 'siteuser_user', 'account_emailaddress', 'account_emailconfirmation', 'django_admin_log', 'authtoken_token', 'explorer_query', 'explorer_querylog', 'explorer_queryfavorite', 'explorer_promptlog', 'explorer_explorervalue', 'explorer_databaseconnection', 'django_session', 'socialaccount_socialaccount', 'socialaccount_socialapp', 'socialaccount_socialtoken']>
>>> 
```

### `runzeo` management command

```
python manage.py runzeo
Starting ZEO server on 127.0.0.1:49275...
ZEO server is running... Press Ctrl+C to stop.
```

#### `python manage.py dumpzodb`

```
test-django-zodb git:main
(test-django-zodb) ❯ python manage.py dumpzodb
: {'catalog': <zope.catalog.catalog.Catalog object at 0x108f2c8a0 oid 0x1 in <ZODB.Connection.Connection object at 0x108f62870>>, 'tables': <BTrees.OOBTree.OOBTree object at 0x108f1a040 oid 0x4 in <ZODB.Connection.Connection object at 0x108f62870>>}
  /data: {'catalog': <zope.catalog.catalog.Catalog object at 0x108f2c8a0 oid 0x1 in <ZODB.Connection.Connection object at 0x108f62870>>, 'tables': <BTrees.OOBTree.OOBTree object at 0x108f1a040 oid 0x4 in <ZODB.Connection.Connection object at 0x108f62870>>}
    /data/catalog: <zope.catalog.catalog.Catalog object at 0x108f2c8a0 oid 0x1 in <ZODB.Connection.Connection object at 0x108f62870>>
    /data/tables: <BTrees.OOBTree.OOBTree object at 0x108f1a040 oid 0x4 in <ZODB.Connection.Connection object at 0x108f62870>>
      /data/tables/account_emailaddress: <BTrees.OOBTree.OOBTree object at 0x108f1a240 oid 0xa in <ZODB.Connection.Connection object at 0x108f62870>>
      /data/tables/account_emailconfirmation: <BTrees.OOBTree.OOBTree object at 0x108f1a2c0 oid 0xb in <ZODB.Connection.Connection object at 0x108f62870>>
      /data/tables/auth_group: <BTrees.OOBTree.OOBTree object at 0x108f1a340 oid 0x8 in <ZODB.Connection.Connection object at 0x108f62870>>
      /data/tables/auth_permission: <BTrees.OOBTree.OOBTree object at 0x108f1a440 oid 0x7 in <ZODB.Connection.Connection object at 0x108f62870>>
        /data/tables/auth_permission/1: ('Can add log entry', 2, 'add_logentry', 'Can change log entry', 2, 'change_logentry', 'Can delete log entry', 2, 'delete_logentry', 'Can view log entry', 2, 'view_logentry')
        /data/tables/auth_permission/2: ('Can add permission', 5, 'add_permission', 'Can change permission', 5, 'change_permission', 'Can delete permission', 5, 'delete_permission', 'Can view permission', 5, 'view_permission', 'Can add group', 6, 'add_group', 'Can change group', 6, 'change_group', 'Can delete group', 6, 'delete_group', 'Can view group', 6, 'view_group')
        /data/tables/auth_permission/3: ('Can add content type', 9, 'add_contenttype', 'Can change content type', 9, 'change_contenttype', 'Can delete content type', 9, 'delete_contenttype', 'Can view content type', 9, 'view_contenttype')
        /data/tables/auth_permission/4: ('Can add session', 12, 'add_session', 'Can change session', 12, 'change_session', 'Can delete session', 12, 'delete_session', 'Can view session', 12, 'view_session')
        /data/tables/auth_permission/5: ('Can add Token', 15, 'add_token', 'Can change Token', 15, 'change_token', 'Can delete Token', 15, 'delete_token', 'Can view Token', 15, 'view_token', 'Can add Token', 16, 'add_tokenproxy', 'Can change Token', 16, 'change_tokenproxy', 'Can delete Token', 16, 'delete_tokenproxy', 'Can view Token', 16, 'view_tokenproxy')
        /data/tables/auth_permission/6: ('Can add email address', 19, 'add_emailaddress', 'Can change email address', 19, 'change_emailaddress', 'Can delete email address', 19, 'delete_emailaddress', 'Can view email address', 19, 'view_emailaddress', 'Can add email confirmation', 20, 'add_emailconfirmation', 'Can change email confirmation', 20, 'change_emailconfirmation', 'Can delete email confirmation', 20, 'delete_emailconfirmation', 'Can view email confirmation', 20, 'view_emailconfirmation')
        /data/tables/auth_permission/7: ('Can add social account', 23, 'add_socialaccount', 'Can change social account', 23, 'change_socialaccount', 'Can delete social account', 23, 'delete_socialaccount', 'Can view social account', 23, 'view_socialaccount', 'Can add social application', 24, 'add_socialapp', 'Can change social application', 24, 'change_socialapp', 'Can delete social application', 24, 'delete_socialapp', 'Can view social application', 24, 'view_socialapp', 'Can add social application token', 25, 'add_socialtoken', 'Can change social application token', 25, 'change_socialtoken', 'Can delete social application token', 25, 'delete_socialtoken', 'Can view social application token', 25, 'view_socialtoken')
        /data/tables/auth_permission/8: ('Can add user', 28, 'add_user', 'Can change user', 28, 'change_user', 'Can delete user', 28, 'delete_user', 'Can view user', 28, 'view_user')
        /data/tables/auth_permission/9: ('Can add Query', 31, 'add_query', 'Can change Query', 31, 'change_query', 'Can delete Query', 31, 'delete_query', 'Can view Query', 31, 'view_query', 'Can add query log', 32, 'add_querylog', 'Can change query log', 32, 'change_querylog', 'Can delete query log', 32, 'delete_querylog', 'Can view query log', 32, 'view_querylog', 'Can add query favorite', 33, 'add_queryfavorite', 'Can change query favorite', 33, 'change_queryfavorite', 'Can delete query favorite', 33, 'delete_queryfavorite', 'Can view query favorite', 33, 'view_queryfavorite', 'Can add prompt log', 34, 'add_promptlog', 'Can change prompt log', 34, 'change_promptlog', 'Can delete prompt log', 34, 'delete_promptlog', 'Can view prompt log', 34, 'view_promptlog', 'Can add explorer value', 35, 'add_explorervalue', 'Can change explorer value', 35, 'change_explorervalue', 'Can delete explorer value', 35, 'delete_explorervalue', 'Can view explorer value', 35, 'view_explorervalue', 'Can add database connection', 36, 'add_databaseconnection', 'Can change database connection', 36, 'change_databaseconnection', 'Can delete database connection', 36, 'delete_databaseconnection', 'Can view database connection', 36, 'view_databaseconnection')
      /data/tables/authtoken_token: <BTrees.OOBTree.OOBTree object at 0x108f1a4c0 oid 0x11 in <ZODB.Connection.Connection object at 0x108f62870>>
      /data/tables/django_admin_log: <BTrees.OOBTree.OOBTree object at 0x108f1a540 oid 0x10 in <ZODB.Connection.Connection object at 0x108f62870>>
      /data/tables/django_content_type: <BTrees.OOBTree.OOBTree object at 0x108f1a5c0 oid 0x6 in <ZODB.Connection.Connection object at 0x108f62870>>
        /data/tables/django_content_type/1: ('admin', 'logentry')
        … 
```
