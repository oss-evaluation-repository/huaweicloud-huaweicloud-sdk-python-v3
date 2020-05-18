# coding: utf-8

"""
    IMS

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v2
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages

NAME = "huaweicloudsdkims"
DESCRIPTION = "IMS"
AUTHOR = "HuaweiCloud SDK"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

VERSION = "3.0.1-beta"

REQUIRES = ["huaweicloudsdkcore"]

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    license="Apache LICENSE 2.0",
    url=URL,
    keywords=["huaweicloud", "sdk", "IMS"],
    packages=find_packages(exclude=["tests*"]),
    install_requires=REQUIRES,
    include_package_data=True,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
    )
)
