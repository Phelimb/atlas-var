from setuptools import setup

setup(
    name='atlasvar',
    version='0.0.1.1',
    packages=[
        'atlasvar',
        'atlasvar.probes',
        'atlasvar.probes.models'],
    license='MIT',
    url='https://github.com/Phelimb/ga4gh-mongo',
    description='A document based Variant database inspired by ga4gh Variants schema',
    author='Phelim Bradley',
    author_email='wave@phel.im',
    install_requires=["mongoengine"])
