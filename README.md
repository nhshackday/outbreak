This is outbreak - an [NHS Hack Day](http://nhshackday.com) project.

For development, to get started, run the following commands:

```
    python manage.py syncdb --migrate
    python manage.py runserver
```


### Deployment

The target deployment environment for this application is a Raspberry Pi or similar.

The `fabfile.py` should include automated environment configuration and deployment.

To configure the environment for the first time:

    fab configure

To deploy subsequent versions:

    fab deploy