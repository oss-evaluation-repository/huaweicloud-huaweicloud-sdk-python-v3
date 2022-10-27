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
VERSION = "3.1.6"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.6',
    'huaweicloudsdkantiddos==3.1.6',
    'huaweicloudsdkaom==3.1.6',
    'huaweicloudsdkapig==3.1.6',
    'huaweicloudsdkapm==3.1.6',
    'huaweicloudsdkas==3.1.6',
    'huaweicloudsdkbcs==3.1.6',
    'huaweicloudsdkbms==3.1.6',
    'huaweicloudsdkbss==3.1.6',
    'huaweicloudsdkbssintl==3.1.6',
    'huaweicloudsdkcae==3.1.6',
    'huaweicloudsdkcampusgo==3.1.6',
    'huaweicloudsdkcbh==3.1.6',
    'huaweicloudsdkcbr==3.1.6',
    'huaweicloudsdkcbs==3.1.6',
    'huaweicloudsdkcc==3.1.6',
    'huaweicloudsdkcce==3.1.6',
    'huaweicloudsdkccm==3.1.6',
    'huaweicloudsdkcdm==3.1.6',
    'huaweicloudsdkcdn==3.1.6',
    'huaweicloudsdkces==3.1.6',
    'huaweicloudsdkcgs==3.1.6',
    'huaweicloudsdkclassroom==3.1.6',
    'huaweicloudsdkcloudartifact==3.1.6',
    'huaweicloudsdkcloudbuild==3.1.6',
    'huaweicloudsdkclouddeploy==3.1.6',
    'huaweicloudsdkcloudide==3.1.6',
    'huaweicloudsdkcloudpipeline==3.1.6',
    'huaweicloudsdkcloudrtc==3.1.6',
    'huaweicloudsdkcloudtable==3.1.6',
    'huaweicloudsdkcloudtest==3.1.6',
    'huaweicloudsdkcodecheck==3.1.6',
    'huaweicloudsdkcodecraft==3.1.6',
    'huaweicloudsdkcodehub==3.1.6',
    'huaweicloudsdkcph==3.1.6',
    'huaweicloudsdkcpts==3.1.6',
    'huaweicloudsdkcse==3.1.6',
    'huaweicloudsdkcsms==3.1.6',
    'huaweicloudsdkcss==3.1.6',
    'huaweicloudsdkcts==3.1.6',
    'huaweicloudsdkdas==3.1.6',
    'huaweicloudsdkdbss==3.1.6',
    'huaweicloudsdkdcs==3.1.6',
    'huaweicloudsdkddm==3.1.6',
    'huaweicloudsdkdds==3.1.6',
    'huaweicloudsdkdeh==3.1.6',
    'huaweicloudsdkdevstar==3.1.6',
    'huaweicloudsdkdgc==3.1.6',
    'huaweicloudsdkdli==3.1.6',
    'huaweicloudsdkdms==3.1.6',
    'huaweicloudsdkdns==3.1.6',
    'huaweicloudsdkdrs==3.1.6',
    'huaweicloudsdkdsc==3.1.6',
    'huaweicloudsdkdws==3.1.6',
    'huaweicloudsdkecs==3.1.6',
    'huaweicloudsdkeg==3.1.6',
    'huaweicloudsdkeihealth==3.1.6',
    'huaweicloudsdkeip==3.1.6',
    'huaweicloudsdkelb==3.1.6',
    'huaweicloudsdkeps==3.1.6',
    'huaweicloudsdker==3.1.6',
    'huaweicloudsdkevs==3.1.6',
    'huaweicloudsdkfrs==3.1.6',
    'huaweicloudsdkfunctiongraph==3.1.6',
    'huaweicloudsdkgaussdb==3.1.6',
    'huaweicloudsdkgaussdbfornosql==3.1.6',
    'huaweicloudsdkgaussdbforopengauss==3.1.6',
    'huaweicloudsdkges==3.1.6',
    'huaweicloudsdkgsl==3.1.6',
    'huaweicloudsdkhilens==3.1.6',
    'huaweicloudsdkhss==3.1.6',
    'huaweicloudsdkiam==3.1.6',
    'huaweicloudsdkiec==3.1.6',
    'huaweicloudsdkief==3.1.6',
    'huaweicloudsdkies==3.1.6',
    'huaweicloudsdkimage==3.1.6',
    'huaweicloudsdkimagesearch==3.1.6',
    'huaweicloudsdkims==3.1.6',
    'huaweicloudsdkiotanalytics==3.1.6',
    'huaweicloudsdkiotda==3.1.6',
    'huaweicloudsdkiotedge==3.1.6',
    'huaweicloudsdkivs==3.1.6',
    'huaweicloudsdkkafka==3.1.6',
    'huaweicloudsdkkms==3.1.6',
    'huaweicloudsdkkps==3.1.6',
    'huaweicloudsdklive==3.1.6',
    'huaweicloudsdklts==3.1.6',
    'huaweicloudsdkmeeting==3.1.6',
    'huaweicloudsdkmoderation==3.1.6',
    'huaweicloudsdkmpc==3.1.6',
    'huaweicloudsdkmrs==3.1.6',
    'huaweicloudsdknat==3.1.6',
    'huaweicloudsdknlp==3.1.6',
    'huaweicloudsdkocr==3.1.6',
    'huaweicloudsdkoms==3.1.6',
    'huaweicloudsdkosm==3.1.6',
    'huaweicloudsdkprojectman==3.1.6',
    'huaweicloudsdkrabbitmq==3.1.6',
    'huaweicloudsdkrds==3.1.6',
    'huaweicloudsdkres==3.1.6',
    'huaweicloudsdkrms==3.1.6',
    'huaweicloudsdkrocketmq==3.1.6',
    'huaweicloudsdkroma==3.1.6',
    'huaweicloudsdksa==3.1.6',
    'huaweicloudsdkscm==3.1.6',
    'huaweicloudsdksdrs==3.1.6',
    'huaweicloudsdkservicestage==3.1.6',
    'huaweicloudsdksfsturbo==3.1.6',
    'huaweicloudsdksis==3.1.6',
    'huaweicloudsdksmn==3.1.6',
    'huaweicloudsdksms==3.1.6',
    'huaweicloudsdkswr==3.1.6',
    'huaweicloudsdktms==3.1.6',
    'huaweicloudsdkugo==3.1.6',
    'huaweicloudsdkvas==3.1.6',
    'huaweicloudsdkvcm==3.1.6',
    'huaweicloudsdkvod==3.1.6',
    'huaweicloudsdkvpc==3.1.6',
    'huaweicloudsdkvpcep==3.1.6',
    'huaweicloudsdkvss==3.1.6',
    'huaweicloudsdkwaf==3.1.6',
    'huaweicloudsdkworkspace==3.1.6',
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
