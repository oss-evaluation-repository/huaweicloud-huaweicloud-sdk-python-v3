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
VERSION = "3.0.91"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.0.91',
    'huaweicloudsdkantiddos==3.0.91',
    'huaweicloudsdkaom==3.0.91',
    'huaweicloudsdkapig==3.0.91',
    'huaweicloudsdkapm==3.0.91',
    'huaweicloudsdkas==3.0.91',
    'huaweicloudsdkbcs==3.0.91',
    'huaweicloudsdkbms==3.0.91',
    'huaweicloudsdkbss==3.0.91',
    'huaweicloudsdkbssintl==3.0.91',
    'huaweicloudsdkcampusgo==3.0.91',
    'huaweicloudsdkcbh==3.0.91',
    'huaweicloudsdkcbr==3.0.91',
    'huaweicloudsdkcbs==3.0.91',
    'huaweicloudsdkcc==3.0.91',
    'huaweicloudsdkcce==3.0.91',
    'huaweicloudsdkccm==3.0.91',
    'huaweicloudsdkcdm==3.0.91',
    'huaweicloudsdkcdn==3.0.91',
    'huaweicloudsdkces==3.0.91',
    'huaweicloudsdkcgs==3.0.91',
    'huaweicloudsdkclassroom==3.0.91',
    'huaweicloudsdkcloudbuild==3.0.91',
    'huaweicloudsdkclouddeploy==3.0.91',
    'huaweicloudsdkcloudide==3.0.91',
    'huaweicloudsdkcloudpipeline==3.0.91',
    'huaweicloudsdkcloudrtc==3.0.91',
    'huaweicloudsdkcloudtable==3.0.91',
    'huaweicloudsdkcloudtest==3.0.91',
    'huaweicloudsdkcodecheck==3.0.91',
    'huaweicloudsdkcodecraft==3.0.91',
    'huaweicloudsdkcodehub==3.0.91',
    'huaweicloudsdkcpts==3.0.91',
    'huaweicloudsdkcse==3.0.91',
    'huaweicloudsdkcsms==3.0.91',
    'huaweicloudsdkcss==3.0.91',
    'huaweicloudsdkcts==3.0.91',
    'huaweicloudsdkdas==3.0.91',
    'huaweicloudsdkdbss==3.0.91',
    'huaweicloudsdkdcs==3.0.91',
    'huaweicloudsdkddm==3.0.91',
    'huaweicloudsdkdds==3.0.91',
    'huaweicloudsdkdeh==3.0.91',
    'huaweicloudsdkdevstar==3.0.91',
    'huaweicloudsdkdgc==3.0.91',
    'huaweicloudsdkdms==3.0.91',
    'huaweicloudsdkdns==3.0.91',
    'huaweicloudsdkdrs==3.0.91',
    'huaweicloudsdkdsc==3.0.91',
    'huaweicloudsdkdws==3.0.91',
    'huaweicloudsdkecs==3.0.91',
    'huaweicloudsdkeip==3.0.91',
    'huaweicloudsdkelb==3.0.91',
    'huaweicloudsdkeps==3.0.91',
    'huaweicloudsdkevs==3.0.91',
    'huaweicloudsdkfrs==3.0.91',
    'huaweicloudsdkfunctiongraph==3.0.91',
    'huaweicloudsdkgaussdb==3.0.91',
    'huaweicloudsdkgaussdbfornosql==3.0.91',
    'huaweicloudsdkgaussdbforopengauss==3.0.91',
    'huaweicloudsdkges==3.0.91',
    'huaweicloudsdkgsl==3.0.91',
    'huaweicloudsdkhilens==3.0.91',
    'huaweicloudsdkhss==3.0.91',
    'huaweicloudsdkiam==3.0.91',
    'huaweicloudsdkiec==3.0.91',
    'huaweicloudsdkief==3.0.91',
    'huaweicloudsdkies==3.0.91',
    'huaweicloudsdkimage==3.0.91',
    'huaweicloudsdkimagesearch==3.0.91',
    'huaweicloudsdkims==3.0.91',
    'huaweicloudsdkiotanalytics==3.0.91',
    'huaweicloudsdkiotda==3.0.91',
    'huaweicloudsdkiotedge==3.0.91',
    'huaweicloudsdkivs==3.0.91',
    'huaweicloudsdkkafka==3.0.91',
    'huaweicloudsdkkms==3.0.91',
    'huaweicloudsdkkps==3.0.91',
    'huaweicloudsdklive==3.0.91',
    'huaweicloudsdklts==3.0.91',
    'huaweicloudsdkmeeting==3.0.91',
    'huaweicloudsdkmoderation==3.0.91',
    'huaweicloudsdkmpc==3.0.91',
    'huaweicloudsdkmrs==3.0.91',
    'huaweicloudsdknat==3.0.91',
    'huaweicloudsdknlp==3.0.91',
    'huaweicloudsdkocr==3.0.91',
    'huaweicloudsdkoms==3.0.91',
    'huaweicloudsdkosm==3.0.91',
    'huaweicloudsdkprojectman==3.0.91',
    'huaweicloudsdkrabbitmq==3.0.91',
    'huaweicloudsdkrds==3.0.91',
    'huaweicloudsdkres==3.0.91',
    'huaweicloudsdkrms==3.0.91',
    'huaweicloudsdkrocketmq==3.0.91',
    'huaweicloudsdkroma==3.0.91',
    'huaweicloudsdksa==3.0.91',
    'huaweicloudsdkscm==3.0.91',
    'huaweicloudsdksdrs==3.0.91',
    'huaweicloudsdkservicestage==3.0.91',
    'huaweicloudsdksfsturbo==3.0.91',
    'huaweicloudsdksis==3.0.91',
    'huaweicloudsdksmn==3.0.91',
    'huaweicloudsdksms==3.0.91',
    'huaweicloudsdkswr==3.0.91',
    'huaweicloudsdktms==3.0.91',
    'huaweicloudsdkvas==3.0.91',
    'huaweicloudsdkvod==3.0.91',
    'huaweicloudsdkvpc==3.0.91',
    'huaweicloudsdkvpcep==3.0.91',
    'huaweicloudsdkvss==3.0.91',
    'huaweicloudsdkwaf==3.0.91',
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
