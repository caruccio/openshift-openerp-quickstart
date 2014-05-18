# OpenShift OpenERP quickstart

Este quickstart contém uma instalação do OpenERP pronta para rodar no OpenShift.

Se você ainda não tem uma conta na Getup, vá em http://getupcloud.com e registre-se gratuitamente.

## Crie seu app

Primeiro, crie uma aplicação Python com PostgreSQL:

```
$ rhc app create openerp python-2.7 postgresql-9
```

Depois, faça o merge e o push deste repo para sua aplicação.

```
$ cd openerp/
$ git remote add upstream https://github.com/caruccio/openshift-openerp-quickstart.git
$ git pull -s recursive -X theirs upstream master
$ git push
```

Pronto!

Aponte seu browser para [https://openerp-$namespace.getup.io](https://openerp-$namespace.getup.io) e faça login.
As credentials padrão são:

```
Username: admin
Password: admin
```

## Atualização

Este quickstart utiliza um build noturno do OpenERP, a partir do arquivo http://nightly.openerp.com/7.0/nightly/src/openerp-7.0-20140517-231234.tar.gz

Para utilizar outra versão do openerp, edite o arquivo `.openshift/action_hooks/build`, atualizando as variaveis OPENERP_VERSION e OPENERP_TIMESTAMP para os valores desejados.
Em seguida faça o deploy.

```
$ vim .openshift/action_hooks/build
$ git commit -a -m "Upgrade to version XXX"
$ git push
```
