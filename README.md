Flask web app deployment with nginx + gunicorn + supervisord
============================================================

An Ansible playbook to deploy small web application written in Python using
a Flask application factory and an SQLite database via SQLAlchemy.
Assumes Debian8 because of paths and user/group names. Definitely not production
ready.

Notes
-----

* tested on Debian8 only
* systemd support via `service` module is kind of broken in ansible, use `command` module instead
* some tasks don't indicate `changed` correctly :(
* pyvenv is used, but virtualenv should be easy to get working
* virtualenvs are called `env` by default
* sites use sqlite databases by default
* wsgi script very specific
* a script called `reset_db` creates a bare-bones database file in `/tmp/<sitename>.db`
* don't set user on supervisor AND gunicorn - DOH!
