from setuptools import setup

setup(
    name='ga4ghmongo',
    version='0.0.1.1',
    packages=[
        'ga4ghmongo',
        'ga4ghmongo.schema',
        'ga4ghmongo.schema.models'],
    license='MIT',
    url='https://github.com/Phelimb/ga4gh-mongo',
    description='A document based Variant database inspired by ga4gh Variants schema',
    author='Phelim Bradley',
    author_email='wave@phel.im',
    install_requires=["mongoengine"])
