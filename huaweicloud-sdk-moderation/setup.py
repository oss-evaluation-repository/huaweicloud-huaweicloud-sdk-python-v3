# coding: utf-8

"""
    Moderation

    moderation v1 API，Open API  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages

NAME = "huaweicloudsdkmoderation"
DESCRIPTION = "Moderation"
AUTHOR = "HuaweiCloud SDK"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

VERSION = "3.0.1-beta"

REQUIRES = ["huaweicloudsdkcore"]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    license="Apache LICENSE 2.0",
    url=URL,
    keywords=["huaweicloud", "sdk", "Moderation"],
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
