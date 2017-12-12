from setuptools import setup

setup(name='geru_app',
      version='1.0',
      include_package_data=True,
      description='Geru challenge app',
      packages=[
          'app',
          'app.models',
          'app.views',
          ],
      install_requires=[
          'requests',
          'pyramid',
          'pyramid-chameleon',
          'sqlalchemy',
          'waitress',
          ],
      zip_safe=False)
