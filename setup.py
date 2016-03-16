from setuptools import setup
from pip.req import parse_requirements
import ga4ghmongo.version
install_reqs = parse_requirements('requirements.txt')
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='ga4ghmongo',
    version=ga4ghmongo.version.__version__,
    packages=[
        'ga4ghmongo',
        'ga4ghmongo.schema',
        'ga4ghmongo.schema.models'],
    license='MIT',
    url='https://github.com/Phelimb/ga4gh-mongo',
    description='.',
    author='Phelim Bradley',
    author_email='wave@phel.im',
    install_requires=reqs)
