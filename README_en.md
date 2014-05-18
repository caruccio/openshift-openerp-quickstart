# OpenShift OpenERP quickstart

This quickstart contains an OpenERP installation ready to run on OpenShift.

If you don't have an account yet, go to http://getupcloud.com and register for a free trial.

## Create your app

First, create an application with PostgreSQL:

```
$ rhc app create openerp python-2.7 postgresql-9
```

Then, merge and push this repo into your new app. Please be patient, this operation may last for a long time.

```
$ cd openerp/
$ git remote add upstream https://github.com/caruccio/openshift-openerp-quickstart.git
$ git pull -s recursive -X theirs upstream master
$ git push
```

That's it!

Point your browser to [https://openerp-$namespace.getup.io](https://openerp-$namespace.getup.io) and login.
Default credentials are:

```
Username: admin
Password: admin
```

## Upgrade

This quickstart uses a nightly build of OpernERP from file http://nightly.openerp.com/7.0/nightly/src/openerp-7.0-20140517-231234.tar.gz

To upgrade OpenERP source, edit file `.openshift/action_hooks/build`, changing variables OPENERP_VERSION and OPENERP_TIMESTAMP to proper values.
Deploy after that.

```
$ vim .openshift/action_hooks/build
$ git commit -a -m "Upgrade to version XXX"
$ git push
```
