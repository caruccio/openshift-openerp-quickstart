from setuptools import setup

setup(name='YourAppName',
      version='1.0',
      description='OpenShift App',
      author='Your Name',
      author_email='example@example.com',
      url='http://www.python.org/sigs/distutils-sig/',
      dependency_links = ['http://download.gna.org/pychart/'],
      install_requires=['gevent',
                         # OpenERP requires
                         'pychart',
                         'babel',
                         'docutils',
                         'feedparser',
                         'gdata',
                         'Jinja2',
                         'lxml',
                         'mako',
                         'mock',
                         # We use Pillow instead PIL
                         'pillow',
                         # PIL must be installed using pip, not easy_install.
                         # See https://mail.python.org/pipermail/image-sig/2010-August/006480.html
                         #'PIL', # windows binary http://www.lfd.uci.edu/~gohlke/pythonlibs/
                         'psutil', # windows binary code.google.com/p/psutil/downloads/list
                         'psycopg2 >= 2.2',
                         'pydot',
                         'python-dateutil < 2',
                         #'python-ldap', # optional
                         'python-openid',
                         'pytz',
                         'pywebdav',
                         'pyyaml',
                         'reportlab', # windows binary pypi.python.org/pypi/reportlab
                         'simplejson',
                         'unittest2',
                         'vatnumber',
                         'vobject',
                         'werkzeug',
                         'xlwt',
      ]
)
