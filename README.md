# django-zodb

Inspired by https://github.com/osantana-archive/django-zodb

- No RelStorage
- Based on
    - https://github.com/mongodb-labs/django-mongodb
    - https://github.com/django-nonrel/mongodb-engine

## Reference

- https://medium.com/django-unleashed/how-does-django-manage-db-connections-4c1a009cec91

## Current status

- `dbshell` client

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

- Show migrations

```
test-django-zodb git:main  
(test-django-zodb) ❯ python manage.py dbshell
python manage.py migrate
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
Setting autocommit to True
 OK
  Applying auth.0004_alter_user_username_opts...Setting autocommit to False
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['auth', '0004_alter_user_username_opts', '2024-08-05 15:42:25.219585+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying auth.0005_alter_user_last_login_null...Setting autocommit to False
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['auth', '0005_alter_user_last_login_null', '2024-08-05 15:42:25.221811+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying auth.0006_require_contenttypes_0002...Setting autocommit to False
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['auth', '0006_require_contenttypes_0002', '2024-08-05 15:42:25.222482+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying auth.0007_alter_validators_add_error_messages...Setting autocommit to False
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['auth', '0007_alter_validators_add_error_messages', '2024-08-05 15:42:25.224159+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying auth.0008_alter_user_username_max_length...Setting autocommit to False
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['auth', '0008_alter_user_username_max_length', '2024-08-05 15:42:25.225894+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying auth.0009_alter_user_last_name_max_length...Setting autocommit to False
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['auth', '0009_alter_user_last_name_max_length', '2024-08-05 15:42:25.227612+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying auth.0010_alter_group_name_max_length...Setting autocommit to False
Altering field name to name in model auth_group
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['auth', '0010_alter_group_name_max_length', '2024-08-05 15:42:25.229067+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying auth.0011_update_proxy_permissions...Setting autocommit to False
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['auth', '0011_update_proxy_permissions', '2024-08-05 15:42:25.230745+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying auth.0012_alter_user_first_name_max_length...Setting autocommit to False
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['auth', '0012_alter_user_first_name_max_length', '2024-08-05 15:42:25.232396+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying siteuser.0001_initial...Setting autocommit to False
Executing SQL: CREATE TABLE siteuser_user (...); with params: ()
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['siteuser', '0001_initial', '2024-08-05 15:42:25.234984+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying account.0001_initial...Setting autocommit to False
Executing SQL: CREATE TABLE account_emailaddress (...); with params: ()
Executing SQL: CREATE TABLE account_emailconfirmation (...); with params: ()
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['account', '0001_initial', '2024-08-05 15:42:25.240118+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying account.0002_email_max_length...Setting autocommit to False
Altering field email to email in model account_emailaddress
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['account', '0002_email_max_length', '2024-08-05 15:42:25.242493+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying account.0003_alter_emailaddress_create_unique_verified_email...Setting autocommit to False
Altering unique_together for account_emailaddress from () to {('user', 'email')}
Adding constraint unique_verified_email to model account_emailaddress
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['account', '0003_alter_emailaddress_create_unique_verified_email', '2024-08-05 15:42:25.247024+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying account.0004_alter_emailaddress_drop_unique_email...Setting autocommit to False
Altering field email to email in model account_emailaddress
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['account', '0004_alter_emailaddress_drop_unique_email', '2024-08-05 15:42:25.249330+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying account.0005_emailaddress_idx_upper_email...Setting autocommit to False
Executing SQL: CREATE INDEX "account_emailaddress_upper" ON "account_emailaddress" ((UPPER("email"))) with params: None
Unsupported SQL command
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['account', '0005_emailaddress_idx_upper_email', '2024-08-05 15:42:25.251842+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying account.0006_emailaddress_lower...Setting autocommit to False
Executing SQL: UPDATE "account_emailaddress" SET "email" = LOWER("account_emailaddress"."email") WHERE NOT ("account_emailaddress"."email" = (LOWER("account_emailaddress"."email"))) with params: ()
Unsupported SQL command
Closing cursor
Executing SQL: UPDATE "siteuser_user" SET "email" = LOWER("siteuser_user"."email") WHERE NOT ("siteuser_user"."email" = (LOWER("siteuser_user"."email"))) with params: ()
Unsupported SQL command
Closing cursor
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['account', '0006_emailaddress_lower', '2024-08-05 15:42:25.254863+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying account.0007_emailaddress_idx_email...Setting autocommit to False
Executing SQL: DROP INDEX "account_emailaddress_upper" with params: ()
Unsupported SQL command
Altering field email to email in model account_emailaddress
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['account', '0007_emailaddress_idx_email', '2024-08-05 15:42:25.258930+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying account.0008_emailaddress_unique_primary_email_fixup...Setting autocommit to False
Executing SQL: SELECT "account_emailaddress"."user_id", COUNT("account_emailaddress"."user_id") AS "user__count" FROM "account_emailaddress" WHERE "account_emailaddress"."primary" GROUP BY "account_emailaddress"."user_id" HAVING COUNT("account_emailaddress"."user_id") > %s with params: (1,)
Unsupported SQL command
Closing cursor
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['account', '0008_emailaddress_unique_primary_email_fixup', '2024-08-05 15:42:25.262574+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying account.0009_emailaddress_unique_primary_email...Setting autocommit to False
Adding constraint unique_primary_email to model account_emailaddress
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['account', '0009_emailaddress_unique_primary_email', '2024-08-05 15:42:25.266053+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying admin.0001_initial...Setting autocommit to False
Executing SQL: CREATE TABLE django_admin_log (...); with params: ()
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['admin', '0001_initial', '2024-08-05 15:42:25.269583+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying admin.0002_logentry_remove_auto_add...Setting autocommit to False
Altering field action_time to action_time in model django_admin_log
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['admin', '0002_logentry_remove_auto_add', '2024-08-05 15:42:25.272253+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying admin.0003_logentry_add_action_flag_choices...Setting autocommit to False
Altering field action_flag to action_flag in model django_admin_log
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['admin', '0003_logentry_add_action_flag_choices', '2024-08-05 15:42:25.274949+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying authtoken.0001_initial...Setting autocommit to False
Executing SQL: CREATE TABLE authtoken_token (...); with params: ()
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['authtoken', '0001_initial', '2024-08-05 15:42:25.278378+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying authtoken.0002_auto_20160226_1747...Setting autocommit to False
Altering field created to created in model authtoken_token
Altering field key to key in model authtoken_token
Altering field user to user in model authtoken_token
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['authtoken', '0002_auto_20160226_1747', '2024-08-05 15:42:25.287475+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying authtoken.0003_tokenproxy...Setting autocommit to False
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['authtoken', '0003_tokenproxy', '2024-08-05 15:42:25.288403+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying authtoken.0004_alter_tokenproxy_options...Setting autocommit to False
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['authtoken', '0004_alter_tokenproxy_options', '2024-08-05 15:42:25.290059+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying explorer.0001_initial...Setting autocommit to False
Executing SQL: CREATE TABLE explorer_query (...); with params: ()
Executing SQL: CREATE TABLE explorer_querylog (...); with params: ()
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['explorer', '0001_initial', '2024-08-05 15:42:25.297496+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying explorer.0002_auto_20150501_1515...Setting autocommit to False
Removing field is_playground from model explorer_querylog
Altering field sql to sql in model explorer_querylog
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['explorer', '0002_auto_20150501_1515', '2024-08-05 15:42:25.302743+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying explorer.0003_query_snapshot...Setting autocommit to False
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['explorer', '0003_query_snapshot', '2024-08-05 15:42:25.305774+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying explorer.0004_querylog_duration...Setting autocommit to False
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['explorer', '0004_querylog_duration', '2024-08-05 15:42:25.309556+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying explorer.0005_auto_20160105_2052...Setting autocommit to False
Altering field snapshot to snapshot in model explorer_query
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['explorer', '0005_auto_20160105_2052', '2024-08-05 15:42:25.312746+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying explorer.0006_query_connection...Setting autocommit to False
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['explorer', '0006_query_connection', '2024-08-05 15:42:25.315909+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying explorer.0007_querylog_connection...Setting autocommit to False
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['explorer', '0007_querylog_connection', '2024-08-05 15:42:25.319092+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying explorer.0008_auto_20190308_1642...Setting autocommit to False
Altering field connection to connection in model explorer_query
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['explorer', '0008_auto_20190308_1642', '2024-08-05 15:42:25.322724+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying explorer.0009_auto_20201009_0547...Setting autocommit to False
Altering field connection to connection in model explorer_query
Altering field connection to connection in model explorer_querylog
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['explorer', '0009_auto_20201009_0547', '2024-08-05 15:42:25.331527+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying explorer.0010_sql_required...Setting autocommit to False
Altering field sql to sql in model explorer_query
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['explorer', '0010_sql_required', '2024-08-05 15:42:25.334672+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying explorer.0011_query_favorites...Setting autocommit to False
Executing SQL: CREATE TABLE explorer_queryfavorite (...); with params: ()
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['explorer', '0011_query_favorites', '2024-08-05 15:42:25.338813+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying explorer.0012_alter_queryfavorite_query_alter_queryfavorite_user...Setting autocommit to False
Altering field query to query in model explorer_queryfavorite
Altering field user to user in model explorer_queryfavorite
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['explorer', '0012_alter_queryfavorite_query_alter_queryfavorite_user', '2024-08-05 15:42:25.345172+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying explorer.0013_querylog_error_querylog_success...Setting autocommit to False
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['explorer', '0013_querylog_error_querylog_success', '2024-08-05 15:42:25.351608+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying explorer.0014_promptlog...Setting autocommit to False
Executing SQL: CREATE TABLE explorer_promptlog (...); with params: ()
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['explorer', '0014_promptlog', '2024-08-05 15:42:25.356085+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying explorer.0015_explorervalue...Setting autocommit to False
Executing SQL: CREATE TABLE explorer_explorervalue (...); with params: ()
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['explorer', '0015_explorervalue', '2024-08-05 15:42:25.357814+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying explorer.0016_alter_explorervalue_key...Setting autocommit to False
Altering field key to key in model explorer_explorervalue
Executing SQL: SELECT "explorer_explorervalue"."id", "explorer_explorervalue"."key", "explorer_explorervalue"."value" FROM "explorer_explorervalue" WHERE ("explorer_explorervalue"."key" = %s AND "explorer_explorervalue"."value" = %s) LIMIT 21 with params: ('ASP', "You are a data analyst's assistant and will be asked write or modify a SQL query to assist a business\nuser with their analysis. The user will provide a prompt of what they are looking for help with, and may also\nprovide SQL they have written so far, relevant table schema, and sample rows from the tables they are querying.\n\nFor complex requests, you may use Common Table Expressions (CTEs) to break down the problem into smaller parts.\nCTEs are not needed for simpler requests.\n")
Unsupported SQL command
Closing cursor
Executing SQL: SAVEPOINT "s8371260416_x1" with params: None
Unsupported SQL command
Closing cursor
Executing SQL: INSERT INTO "explorer_explorervalue" ("key", "value") VALUES (%s, %s) with params: ['ASP', "You are a data analyst's assistant and will be asked write or modify a SQL query to assist a business\nuser with their analysis. The user will provide a prompt of what they are looking for help with, and may also\nprovide SQL they have written so far, relevant table schema, and sample rows from the tables they are querying.\n\nFor complex requests, you may use Common Table Expressions (CTEs) to break down the problem into smaller parts.\nCTEs are not needed for simpler requests.\n"]
Closing cursor
Executing SQL: RELEASE SAVEPOINT "s8371260416_x1" with params: None
Unsupported SQL command
Closing cursor
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['explorer', '0016_alter_explorervalue_key', '2024-08-05 15:42:25.363853+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying explorer.0017_databaseconnection...Setting autocommit to False
Executing SQL: CREATE TABLE explorer_databaseconnection (...); with params: ()
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['explorer', '0017_databaseconnection', '2024-08-05 15:42:25.365711+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying explorer.0018_alter_databaseconnection_host_and_more...Setting autocommit to False
Altering field host to host in model explorer_databaseconnection
Altering field password to password in model explorer_databaseconnection
Altering field user to user in model explorer_databaseconnection
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['explorer', '0018_alter_databaseconnection_host_and_more', '2024-08-05 15:42:25.367839+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying explorer.0019_alter_databaseconnection_engine...Setting autocommit to False
Altering field engine to engine in model explorer_databaseconnection
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['explorer', '0019_alter_databaseconnection_engine', '2024-08-05 15:42:25.369272+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying explorer.0020_databaseconnection_extras_and_more...Setting autocommit to False
Altering field engine to engine in model explorer_databaseconnection
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['explorer', '0020_databaseconnection_extras_and_more', '2024-08-05 15:42:25.370951+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying explorer.0021_alter_databaseconnection_password_and_more...Setting autocommit to False
Altering field password to password in model explorer_databaseconnection
Altering field user to user in model explorer_databaseconnection
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['explorer', '0021_alter_databaseconnection_password_and_more', '2024-08-05 15:42:25.372556+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying sessions.0001_initial...Setting autocommit to False
Executing SQL: CREATE TABLE django_session (...); with params: ()
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['sessions', '0001_initial', '2024-08-05 15:42:25.374100+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying socialaccount.0001_initial...Setting autocommit to False
Executing SQL: CREATE TABLE socialaccount_socialaccount (...); with params: ()
Executing SQL: CREATE TABLE socialaccount_socialapp (...); with params: ()
Executing SQL: CREATE TABLE socialaccount_socialtoken (...); with params: ()
Altering unique_together for socialaccount_socialtoken from () to {('app', 'account')}
Altering unique_together for socialaccount_socialaccount from () to {('provider', 'uid')}
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['socialaccount', '0001_initial', '2024-08-05 15:42:25.389139+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying socialaccount.0002_token_max_lengths...Setting autocommit to False
Altering field uid to uid in model socialaccount_socialaccount
Altering field client_id to client_id in model socialaccount_socialapp
Altering field key to key in model socialaccount_socialapp
Altering field secret to secret in model socialaccount_socialapp
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['socialaccount', '0002_token_max_lengths', '2024-08-05 15:42:25.394841+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying socialaccount.0003_extra_data_default_dict...Setting autocommit to False
Altering field extra_data to extra_data in model socialaccount_socialaccount
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['socialaccount', '0003_extra_data_default_dict', '2024-08-05 15:42:25.399386+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying socialaccount.0004_app_provider_id_settings...Setting autocommit to False
Altering field provider to provider in model socialaccount_socialaccount
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['socialaccount', '0004_app_provider_id_settings', '2024-08-05 15:42:25.404443+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying socialaccount.0005_socialtoken_nullable_app...Setting autocommit to False
Altering field app to app in model socialaccount_socialtoken
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['socialaccount', '0005_socialtoken_nullable_app', '2024-08-05 15:42:25.408992+00:00']
Closing cursor
Setting autocommit to True
 OK
  Applying socialaccount.0006_alter_socialaccount_extra_data...Setting autocommit to False
Altering field extra_data to extra_data in model socialaccount_socialaccount
Executing SQL: INSERT INTO "django_migrations" ("app", "name", "applied") VALUES (%s, %s, %s) with params: ['socialaccount', '0006_alter_socialaccount_extra_data', '2024-08-05 15:42:25.412960+00:00']
Closing cursor
Setting autocommit to True
 OK
Executing SQL: SELECT "django_migrations"."id", "django_migrations"."app", "django_migrations"."name", "django_migrations"."applied" FROM "django_migrations" with params: ()
Unsupported SQL command
Closing cursor
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = %s with params: ('admin',)
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") INSERT INTO ... VALUES ... with params: ('admin', 'logentry')
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('admin', 'logentry')
Unsupported SQL command
Closing cursor
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('admin', 'logentry')
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") VALUES (%s, %s) with params: ['admin', 'logentry']
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "auth_permission"."content_type_id", "auth_permission"."codename" FROM "auth_permission" INNER JOIN "django_content_type" ON ("auth_permission"."content_type_id" = "django_content_type"."id") WHERE "auth_permission"."content_type_id" IN (%s) ORDER BY "django_content_type"."app_label" ASC, "django_content_type"."model" ASC, "auth_permission"."codename" ASC with params: (2,)
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "auth_permission" ("name", "content_type_id", "codename") INSERT INTO ... VALUES ... with params: ('Can add log entry', 2, 'add_logentry', 'Can change log entry', 2, 'change_logentry', 'Can delete log entry', 2, 'delete_logentry', 'Can view log entry', 2, 'view_logentry')
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = %s with params: ('admin',)
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") INSERT INTO ... VALUES ... with params: ('admin', 'logentry')
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = %s with params: ('auth',)
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") INSERT INTO ... VALUES ... with params: ('auth', 'permission', 'auth', 'group')
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('auth', 'permission')
Unsupported SQL command
Closing cursor
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('auth', 'permission')
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") VALUES (%s, %s) with params: ['auth', 'permission']
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('auth', 'group')
Unsupported SQL command
Closing cursor
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('auth', 'group')
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") VALUES (%s, %s) with params: ['auth', 'group']
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "auth_permission"."content_type_id", "auth_permission"."codename" FROM "auth_permission" INNER JOIN "django_content_type" ON ("auth_permission"."content_type_id" = "django_content_type"."id") WHERE "auth_permission"."content_type_id" IN (%s, %s) ORDER BY "django_content_type"."app_label" ASC, "django_content_type"."model" ASC, "auth_permission"."codename" ASC with params: (5, 6)
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "auth_permission" ("name", "content_type_id", "codename") INSERT INTO ... VALUES ... with params: ('Can add permission', 5, 'add_permission', 'Can change permission', 5, 'change_permission', 'Can delete permission', 5, 'delete_permission', 'Can view permission', 5, 'view_permission', 'Can add group', 6, 'add_group', 'Can change group', 6, 'change_group', 'Can delete group', 6, 'delete_group', 'Can view group', 6, 'view_group')
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = %s with params: ('auth',)
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") INSERT INTO ... VALUES ... with params: ('auth', 'permission', 'auth', 'group')
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = %s with params: ('contenttypes',)
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") INSERT INTO ... VALUES ... with params: ('contenttypes', 'contenttype')
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('contenttypes', 'contenttype')
Unsupported SQL command
Closing cursor
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('contenttypes', 'contenttype')
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") VALUES (%s, %s) with params: ['contenttypes', 'contenttype']
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "auth_permission"."content_type_id", "auth_permission"."codename" FROM "auth_permission" INNER JOIN "django_content_type" ON ("auth_permission"."content_type_id" = "django_content_type"."id") WHERE "auth_permission"."content_type_id" IN (%s) ORDER BY "django_content_type"."app_label" ASC, "django_content_type"."model" ASC, "auth_permission"."codename" ASC with params: (9,)
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "auth_permission" ("name", "content_type_id", "codename") INSERT INTO ... VALUES ... with params: ('Can add content type', 9, 'add_contenttype', 'Can change content type', 9, 'change_contenttype', 'Can delete content type', 9, 'delete_contenttype', 'Can view content type', 9, 'view_contenttype')
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = %s with params: ('contenttypes',)
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") INSERT INTO ... VALUES ... with params: ('contenttypes', 'contenttype')
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = %s with params: ('sessions',)
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") INSERT INTO ... VALUES ... with params: ('sessions', 'session')
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('sessions', 'session')
Unsupported SQL command
Closing cursor
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('sessions', 'session')
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") VALUES (%s, %s) with params: ['sessions', 'session']
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "auth_permission"."content_type_id", "auth_permission"."codename" FROM "auth_permission" INNER JOIN "django_content_type" ON ("auth_permission"."content_type_id" = "django_content_type"."id") WHERE "auth_permission"."content_type_id" IN (%s) ORDER BY "django_content_type"."app_label" ASC, "django_content_type"."model" ASC, "auth_permission"."codename" ASC with params: (12,)
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "auth_permission" ("name", "content_type_id", "codename") INSERT INTO ... VALUES ... with params: ('Can add session', 12, 'add_session', 'Can change session', 12, 'change_session', 'Can delete session', 12, 'delete_session', 'Can view session', 12, 'view_session')
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = %s with params: ('sessions',)
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") INSERT INTO ... VALUES ... with params: ('sessions', 'session')
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = %s with params: ('authtoken',)
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") INSERT INTO ... VALUES ... with params: ('authtoken', 'token', 'authtoken', 'tokenproxy')
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('authtoken', 'token')
Unsupported SQL command
Closing cursor
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('authtoken', 'token')
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") VALUES (%s, %s) with params: ['authtoken', 'token']
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('authtoken', 'tokenproxy')
Unsupported SQL command
Closing cursor
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('authtoken', 'tokenproxy')
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") VALUES (%s, %s) with params: ['authtoken', 'tokenproxy']
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "auth_permission"."content_type_id", "auth_permission"."codename" FROM "auth_permission" INNER JOIN "django_content_type" ON ("auth_permission"."content_type_id" = "django_content_type"."id") WHERE "auth_permission"."content_type_id" IN (%s, %s) ORDER BY "django_content_type"."app_label" ASC, "django_content_type"."model" ASC, "auth_permission"."codename" ASC with params: (16, 15)
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "auth_permission" ("name", "content_type_id", "codename") INSERT INTO ... VALUES ... with params: ('Can add Token', 15, 'add_token', 'Can change Token', 15, 'change_token', 'Can delete Token', 15, 'delete_token', 'Can view Token', 15, 'view_token', 'Can add Token', 16, 'add_tokenproxy', 'Can change Token', 16, 'change_tokenproxy', 'Can delete Token', 16, 'delete_tokenproxy', 'Can view Token', 16, 'view_tokenproxy')
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = %s with params: ('authtoken',)
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") INSERT INTO ... VALUES ... with params: ('authtoken', 'token', 'authtoken', 'tokenproxy')
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = %s with params: ('allauth',)
Unsupported SQL command
Closing cursor
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = %s with params: ('allauth',)
Unsupported SQL command
Closing cursor
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = %s with params: ('account',)
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") INSERT INTO ... VALUES ... with params: ('account', 'emailaddress', 'account', 'emailconfirmation')
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('account', 'emailaddress')
Unsupported SQL command
Closing cursor
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('account', 'emailaddress')
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") VALUES (%s, %s) with params: ['account', 'emailaddress']
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('account', 'emailconfirmation')
Unsupported SQL command
Closing cursor
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('account', 'emailconfirmation')
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") VALUES (%s, %s) with params: ['account', 'emailconfirmation']
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "auth_permission"."content_type_id", "auth_permission"."codename" FROM "auth_permission" INNER JOIN "django_content_type" ON ("auth_permission"."content_type_id" = "django_content_type"."id") WHERE "auth_permission"."content_type_id" IN (%s, %s) ORDER BY "django_content_type"."app_label" ASC, "django_content_type"."model" ASC, "auth_permission"."codename" ASC with params: (19, 20)
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "auth_permission" ("name", "content_type_id", "codename") INSERT INTO ... VALUES ... with params: ('Can add email address', 19, 'add_emailaddress', 'Can change email address', 19, 'change_emailaddress', 'Can delete email address', 19, 'delete_emailaddress', 'Can view email address', 19, 'view_emailaddress', 'Can add email confirmation', 20, 'add_emailconfirmation', 'Can change email confirmation', 20, 'change_emailconfirmation', 'Can delete email confirmation', 20, 'delete_emailconfirmation', 'Can view email confirmation', 20, 'view_emailconfirmation')
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = %s with params: ('account',)
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") INSERT INTO ... VALUES ... with params: ('account', 'emailaddress', 'account', 'emailconfirmation')
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = %s with params: ('socialaccount',)
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") INSERT INTO ... VALUES ... with params: ('socialaccount', 'socialaccount', 'socialaccount', 'socialapp', 'socialaccount', 'socialtoken')
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('socialaccount', 'socialaccount')
Unsupported SQL command
Closing cursor
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('socialaccount', 'socialaccount')
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") VALUES (%s, %s) with params: ['socialaccount', 'socialaccount']
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('socialaccount', 'socialapp')
Unsupported SQL command
Closing cursor
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('socialaccount', 'socialapp')
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") VALUES (%s, %s) with params: ['socialaccount', 'socialapp']
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('socialaccount', 'socialtoken')
Unsupported SQL command
Closing cursor
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('socialaccount', 'socialtoken')
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") VALUES (%s, %s) with params: ['socialaccount', 'socialtoken']
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "auth_permission"."content_type_id", "auth_permission"."codename" FROM "auth_permission" INNER JOIN "django_content_type" ON ("auth_permission"."content_type_id" = "django_content_type"."id") WHERE "auth_permission"."content_type_id" IN (%s, %s, %s) ORDER BY "django_content_type"."app_label" ASC, "django_content_type"."model" ASC, "auth_permission"."codename" ASC with params: (24, 25, 23)
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "auth_permission" ("name", "content_type_id", "codename") INSERT INTO ... VALUES ... with params: ('Can add social account', 23, 'add_socialaccount', 'Can change social account', 23, 'change_socialaccount', 'Can delete social account', 23, 'delete_socialaccount', 'Can view social account', 23, 'view_socialaccount', 'Can add social application', 24, 'add_socialapp', 'Can change social application', 24, 'change_socialapp', 'Can delete social application', 24, 'delete_socialapp', 'Can view social application', 24, 'view_socialapp', 'Can add social application token', 25, 'add_socialtoken', 'Can change social application token', 25, 'change_socialtoken', 'Can delete social application token', 25, 'delete_socialtoken', 'Can view social application token', 25, 'view_socialtoken')
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = %s with params: ('socialaccount',)
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") INSERT INTO ... VALUES ... with params: ('socialaccount', 'socialaccount', 'socialaccount', 'socialapp', 'socialaccount', 'socialtoken')
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = %s with params: ('django_extensions',)
Unsupported SQL command
Closing cursor
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = %s with params: ('django_extensions',)
Unsupported SQL command
Closing cursor
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = %s with params: ('django_recaptcha',)
Unsupported SQL command
Closing cursor
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = %s with params: ('django_recaptcha',)
Unsupported SQL command
Closing cursor
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = %s with params: ('siteuser',)
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") INSERT INTO ... VALUES ... with params: ('siteuser', 'user')
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('siteuser', 'user')
Unsupported SQL command
Closing cursor
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('siteuser', 'user')
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") VALUES (%s, %s) with params: ['siteuser', 'user']
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "auth_permission"."content_type_id", "auth_permission"."codename" FROM "auth_permission" INNER JOIN "django_content_type" ON ("auth_permission"."content_type_id" = "django_content_type"."id") WHERE "auth_permission"."content_type_id" IN (%s) ORDER BY "django_content_type"."app_label" ASC, "django_content_type"."model" ASC, "auth_permission"."codename" ASC with params: (28,)
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "auth_permission" ("name", "content_type_id", "codename") INSERT INTO ... VALUES ... with params: ('Can add user', 28, 'add_user', 'Can change user', 28, 'change_user', 'Can delete user', 28, 'delete_user', 'Can view user', 28, 'view_user')
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = %s with params: ('siteuser',)
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") INSERT INTO ... VALUES ... with params: ('siteuser', 'user')
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = %s with params: ('explorer',)
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") INSERT INTO ... VALUES ... with params: ('explorer', 'query', 'explorer', 'querylog', 'explorer', 'queryfavorite', 'explorer', 'promptlog', 'explorer', 'explorervalue', 'explorer', 'databaseconnection')
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('explorer', 'query')
Unsupported SQL command
Closing cursor
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('explorer', 'query')
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") VALUES (%s, %s) with params: ['explorer', 'query']
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('explorer', 'querylog')
Unsupported SQL command
Closing cursor
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('explorer', 'querylog')
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") VALUES (%s, %s) with params: ['explorer', 'querylog']
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('explorer', 'queryfavorite')
Unsupported SQL command
Closing cursor
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('explorer', 'queryfavorite')
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") VALUES (%s, %s) with params: ['explorer', 'queryfavorite']
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('explorer', 'promptlog')
Unsupported SQL command
Closing cursor
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('explorer', 'promptlog')
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") VALUES (%s, %s) with params: ['explorer', 'promptlog']
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('explorer', 'explorervalue')
Unsupported SQL command
Closing cursor
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('explorer', 'explorervalue')
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") VALUES (%s, %s) with params: ['explorer', 'explorervalue']
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('explorer', 'databaseconnection')
Unsupported SQL command
Closing cursor
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = %s AND "django_content_type"."model" = %s) LIMIT 21 with params: ('explorer', 'databaseconnection')
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") VALUES (%s, %s) with params: ['explorer', 'databaseconnection']
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "auth_permission"."content_type_id", "auth_permission"."codename" FROM "auth_permission" INNER JOIN "django_content_type" ON ("auth_permission"."content_type_id" = "django_content_type"."id") WHERE "auth_permission"."content_type_id" IN (%s, %s, %s, %s, %s, %s) ORDER BY "django_content_type"."app_label" ASC, "django_content_type"."model" ASC, "auth_permission"."codename" ASC with params: (32, 33, 34, 35, 36, 31)
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "auth_permission" ("name", "content_type_id", "codename") INSERT INTO ... VALUES ... with params: ('Can add Query', 31, 'add_query', 'Can change Query', 31, 'change_query', 'Can delete Query', 31, 'delete_query', 'Can view Query', 31, 'view_query', 'Can add query log', 32, 'add_querylog', 'Can change query log', 32, 'change_querylog', 'Can delete query log', 32, 'delete_querylog', 'Can view query log', 32, 'view_querylog', 'Can add query favorite', 33, 'add_queryfavorite', 'Can change query favorite', 33, 'change_queryfavorite', 'Can delete query favorite', 33, 'delete_queryfavorite', 'Can view query favorite', 33, 'view_queryfavorite', 'Can add prompt log', 34, 'add_promptlog', 'Can change prompt log', 34, 'change_promptlog', 'Can delete prompt log', 34, 'delete_promptlog', 'Can view prompt log', 34, 'view_promptlog', 'Can add explorer value', 35, 'add_explorervalue', 'Can change explorer value', 35, 'change_explorervalue', 'Can delete explorer value', 35, 'delete_explorervalue', 'Can view explorer value', 35, 'view_explorervalue', 'Can add database connection', 36, 'add_databaseconnection', 'Can change database connection', 36, 'change_databaseconnection', 'Can delete database connection', 36, 'delete_databaseconnection', 'Can view database connection', 36, 'view_databaseconnection')
Closing cursor
Setting autocommit to True
Executing SQL: SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = %s with params: ('explorer',)
Unsupported SQL command
Closing cursor
Setting autocommit to False
Executing SQL: INSERT INTO "django_content_type" ("app_label", "model") INSERT INTO ... VALUES ... with params: ('explorer', 'query', 'explorer', 'querylog', 'explorer', 'queryfavorite', 'explorer', 'promptlog', 'explorer', 'explorervalue', 'explorer', 'databaseconnection')
Closing cursor
Setting autocommit to True
```
