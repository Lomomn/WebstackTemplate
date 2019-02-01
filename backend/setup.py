import io

from setuptools import find_packages, setup

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='template',
    version='1.0.0',
    license='BSD',
    description='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'uwsgi',
        'flask-sqlalchemy',
        'flask-restplus',
        'psycopg2-binary'
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
            'sqlalchemy-utils',
        ],
    },
)