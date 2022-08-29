# coding= utf-8
"""
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache LICENSE, Version 2.0 (the
 "LICENSE"); you may not use this file except in compliance
 with the LICENSE.  You may obtain a copy of the LICENSE at

     http=//www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the LICENSE is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the LICENSE for the
 specific language governing permissions and limitations
 under the LICENSE.
"""

from os import path

from setuptools import setup, find_packages

NAME = "huaweicloudsdkall"
VERSION = "3.0.107"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.0.107',
    'huaweicloudsdkantiddos==3.0.107',
    'huaweicloudsdkaom==3.0.107',
    'huaweicloudsdkapig==3.0.107',
    'huaweicloudsdkapm==3.0.107',
    'huaweicloudsdkas==3.0.107',
    'huaweicloudsdkbcs==3.0.107',
    'huaweicloudsdkbms==3.0.107',
    'huaweicloudsdkbss==3.0.107',
    'huaweicloudsdkbssintl==3.0.107',
    'huaweicloudsdkcampusgo==3.0.107',
    'huaweicloudsdkcbh==3.0.107',
    'huaweicloudsdkcbr==3.0.107',
    'huaweicloudsdkcbs==3.0.107',
    'huaweicloudsdkcc==3.0.107',
    'huaweicloudsdkcce==3.0.107',
    'huaweicloudsdkccm==3.0.107',
    'huaweicloudsdkcdm==3.0.107',
    'huaweicloudsdkcdn==3.0.107',
    'huaweicloudsdkces==3.0.107',
    'huaweicloudsdkcgs==3.0.107',
    'huaweicloudsdkclassroom==3.0.107',
    'huaweicloudsdkcloudbuild==3.0.107',
    'huaweicloudsdkclouddeploy==3.0.107',
    'huaweicloudsdkcloudide==3.0.107',
    'huaweicloudsdkcloudpipeline==3.0.107',
    'huaweicloudsdkcloudrtc==3.0.107',
    'huaweicloudsdkcloudtable==3.0.107',
    'huaweicloudsdkcloudtest==3.0.107',
    'huaweicloudsdkcodecheck==3.0.107',
    'huaweicloudsdkcodecraft==3.0.107',
    'huaweicloudsdkcodehub==3.0.107',
    'huaweicloudsdkcph==3.0.107',
    'huaweicloudsdkcpts==3.0.107',
    'huaweicloudsdkcse==3.0.107',
    'huaweicloudsdkcsms==3.0.107',
    'huaweicloudsdkcss==3.0.107',
    'huaweicloudsdkcts==3.0.107',
    'huaweicloudsdkdas==3.0.107',
    'huaweicloudsdkdbss==3.0.107',
    'huaweicloudsdkdcs==3.0.107',
    'huaweicloudsdkddm==3.0.107',
    'huaweicloudsdkdds==3.0.107',
    'huaweicloudsdkdeh==3.0.107',
    'huaweicloudsdkdevstar==3.0.107',
    'huaweicloudsdkdgc==3.0.107',
    'huaweicloudsdkdli==3.0.107',
    'huaweicloudsdkdms==3.0.107',
    'huaweicloudsdkdns==3.0.107',
    'huaweicloudsdkdrs==3.0.107',
    'huaweicloudsdkdsc==3.0.107',
    'huaweicloudsdkdws==3.0.107',
    'huaweicloudsdkecs==3.0.107',
    'huaweicloudsdkeg==3.0.107',
    'huaweicloudsdkeip==3.0.107',
    'huaweicloudsdkelb==3.0.107',
    'huaweicloudsdkeps==3.0.107',
    'huaweicloudsdkevs==3.0.107',
    'huaweicloudsdkfrs==3.0.107',
    'huaweicloudsdkfunctiongraph==3.0.107',
    'huaweicloudsdkgaussdb==3.0.107',
    'huaweicloudsdkgaussdbfornosql==3.0.107',
    'huaweicloudsdkgaussdbforopengauss==3.0.107',
    'huaweicloudsdkges==3.0.107',
    'huaweicloudsdkgsl==3.0.107',
    'huaweicloudsdkhilens==3.0.107',
    'huaweicloudsdkhss==3.0.107',
    'huaweicloudsdkiam==3.0.107',
    'huaweicloudsdkiec==3.0.107',
    'huaweicloudsdkief==3.0.107',
    'huaweicloudsdkies==3.0.107',
    'huaweicloudsdkimage==3.0.107',
    'huaweicloudsdkimagesearch==3.0.107',
    'huaweicloudsdkims==3.0.107',
    'huaweicloudsdkiotanalytics==3.0.107',
    'huaweicloudsdkiotda==3.0.107',
    'huaweicloudsdkiotedge==3.0.107',
    'huaweicloudsdkivs==3.0.107',
    'huaweicloudsdkkafka==3.0.107',
    'huaweicloudsdkkms==3.0.107',
    'huaweicloudsdkkps==3.0.107',
    'huaweicloudsdklive==3.0.107',
    'huaweicloudsdklts==3.0.107',
    'huaweicloudsdkmeeting==3.0.107',
    'huaweicloudsdkmoderation==3.0.107',
    'huaweicloudsdkmpc==3.0.107',
    'huaweicloudsdkmrs==3.0.107',
    'huaweicloudsdknat==3.0.107',
    'huaweicloudsdknlp==3.0.107',
    'huaweicloudsdkocr==3.0.107',
    'huaweicloudsdkoms==3.0.107',
    'huaweicloudsdkosm==3.0.107',
    'huaweicloudsdkprojectman==3.0.107',
    'huaweicloudsdkrabbitmq==3.0.107',
    'huaweicloudsdkrds==3.0.107',
    'huaweicloudsdkres==3.0.107',
    'huaweicloudsdkrms==3.0.107',
    'huaweicloudsdkrocketmq==3.0.107',
    'huaweicloudsdkroma==3.0.107',
    'huaweicloudsdksa==3.0.107',
    'huaweicloudsdkscm==3.0.107',
    'huaweicloudsdksdrs==3.0.107',
    'huaweicloudsdkservicestage==3.0.107',
    'huaweicloudsdksfsturbo==3.0.107',
    'huaweicloudsdksis==3.0.107',
    'huaweicloudsdksmn==3.0.107',
    'huaweicloudsdksms==3.0.107',
    'huaweicloudsdkswr==3.0.107',
    'huaweicloudsdktms==3.0.107',
    'huaweicloudsdkugo==3.0.107',
    'huaweicloudsdkvas==3.0.107',
    'huaweicloudsdkvcm==3.0.107',
    'huaweicloudsdkvod==3.0.107',
    'huaweicloudsdkvpc==3.0.107',
    'huaweicloudsdkvpcep==3.0.107',
    'huaweicloudsdkvss==3.0.107',
    'huaweicloudsdkwaf==3.0.107',
]

OPTIONS = {
    'bdist_wheel': {
        'universal': True
    }
}

setup(
    name=NAME,
    version=VERSION,
    options=OPTIONS,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="Apache LICENSE 2.0",
    url=URL,
    keywords=["huaweicloud", "sdk", "all"],
    packages=find_packages(),
    platforms=['any'],
    install_requires=INSTALL_REQUIRES,
    python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development'
    ]
)
