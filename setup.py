from setuptools import setup

setup(
    name='atlasvar',
    version='0.5.2',
    packages=[
        'atlasvar',
        'atlasvar.probes',
        'atlasvar.probes.models',
        'atlasvar.schema',
        'atlasvar.schema.models',
        'atlasvar.cmds',
        'atlasvar.annotation',
        'atlasvar._vcf',
        'atlasvar.annotation.genes',
    ],
    license='MIT',
    url='https://github.com/Phelimb/atlas-var',
    description='A document based Variant database inspired by ga4gh Variants schema',
    author='Phelim Bradley',
    author_email='wave@phel.im',
    install_requires=["mongoengine"],
    entry_points={
        'console_scripts': [
            'atlas-var = atlasvar.__main__:main',
        ]})
