# -*- coding: utf-8 -*-

import setuptools

import tuic_tunnel

with open('README.md', 'rb') as fp:
    README = fp.read().decode()


with open('requirements.txt', 'rb') as fp:
    text = fp.read().decode()
    REQUIREMENTS = text.split('\n')


setuptools.setup(
    author="drunkdream",
    author_email="drunkdream@qq.com",
    name='tuic-tunnel',
    license="MIT",
    description='TUIC tunnel plugin for turbo-tunnel.',
    version=tuic_tunnel.VERSION,
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/turbo-tunnel/tuic-tunnel',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=REQUIREMENTS,
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Intended Audience :: Developers',
    ],
    include_package_data=True
)
