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
VERSION = "3.1.78"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.78',
    'huaweicloudsdkaad==3.1.78',
    'huaweicloudsdkantiddos==3.1.78',
    'huaweicloudsdkaom==3.1.78',
    'huaweicloudsdkaos==3.1.78',
    'huaweicloudsdkapig==3.1.78',
    'huaweicloudsdkapm==3.1.78',
    'huaweicloudsdkas==3.1.78',
    'huaweicloudsdkasm==3.1.78',
    'huaweicloudsdkbcs==3.1.78',
    'huaweicloudsdkbms==3.1.78',
    'huaweicloudsdkbss==3.1.78',
    'huaweicloudsdkbssintl==3.1.78',
    'huaweicloudsdkcae==3.1.78',
    'huaweicloudsdkcampusgo==3.1.78',
    'huaweicloudsdkcbh==3.1.78',
    'huaweicloudsdkcbr==3.1.78',
    'huaweicloudsdkcbs==3.1.78',
    'huaweicloudsdkcc==3.1.78',
    'huaweicloudsdkcce==3.1.78',
    'huaweicloudsdkccm==3.1.78',
    'huaweicloudsdkcdm==3.1.78',
    'huaweicloudsdkcdn==3.1.78',
    'huaweicloudsdkces==3.1.78',
    'huaweicloudsdkcfw==3.1.78',
    'huaweicloudsdkcgs==3.1.78',
    'huaweicloudsdkclassroom==3.1.78',
    'huaweicloudsdkcloudide==3.1.78',
    'huaweicloudsdkcloudpond==3.1.78',
    'huaweicloudsdkcloudrtc==3.1.78',
    'huaweicloudsdkcloudtable==3.1.78',
    'huaweicloudsdkcloudtest==3.1.78',
    'huaweicloudsdkcodeartsartifact==3.1.78',
    'huaweicloudsdkcodeartsbuild==3.1.78',
    'huaweicloudsdkcodeartscheck==3.1.78',
    'huaweicloudsdkcodeartsdeploy==3.1.78',
    'huaweicloudsdkcodeartsinspector==3.1.78',
    'huaweicloudsdkcodeartspipeline==3.1.78',
    'huaweicloudsdkcodecraft==3.1.78',
    'huaweicloudsdkcodehub==3.1.78',
    'huaweicloudsdkconfig==3.1.78',
    'huaweicloudsdkcph==3.1.78',
    'huaweicloudsdkcpts==3.1.78',
    'huaweicloudsdkcse==3.1.78',
    'huaweicloudsdkcsms==3.1.78',
    'huaweicloudsdkcss==3.1.78',
    'huaweicloudsdkcts==3.1.78',
    'huaweicloudsdkdas==3.1.78',
    'huaweicloudsdkdataartsstudio==3.1.78',
    'huaweicloudsdkdbss==3.1.78',
    'huaweicloudsdkdc==3.1.78',
    'huaweicloudsdkdcs==3.1.78',
    'huaweicloudsdkddm==3.1.78',
    'huaweicloudsdkdds==3.1.78',
    'huaweicloudsdkdeh==3.1.78',
    'huaweicloudsdkdevsecurity==3.1.78',
    'huaweicloudsdkdevstar==3.1.78',
    'huaweicloudsdkdgc==3.1.78',
    'huaweicloudsdkdis==3.1.78',
    'huaweicloudsdkdlf==3.1.78',
    'huaweicloudsdkdli==3.1.78',
    'huaweicloudsdkdns==3.1.78',
    'huaweicloudsdkdris==3.1.78',
    'huaweicloudsdkdrs==3.1.78',
    'huaweicloudsdkdsc==3.1.78',
    'huaweicloudsdkdwr==3.1.78',
    'huaweicloudsdkdws==3.1.78',
    'huaweicloudsdkec==3.1.78',
    'huaweicloudsdkecs==3.1.78',
    'huaweicloudsdkedgesec==3.1.78',
    'huaweicloudsdkeg==3.1.78',
    'huaweicloudsdkeihealth==3.1.78',
    'huaweicloudsdkeip==3.1.78',
    'huaweicloudsdkelb==3.1.78',
    'huaweicloudsdkeps==3.1.78',
    'huaweicloudsdker==3.1.78',
    'huaweicloudsdkevs==3.1.78',
    'huaweicloudsdkfrs==3.1.78',
    'huaweicloudsdkfunctiongraph==3.1.78',
    'huaweicloudsdkga==3.1.78',
    'huaweicloudsdkgaussdb==3.1.78',
    'huaweicloudsdkgaussdbfornosql==3.1.78',
    'huaweicloudsdkgaussdbforopengauss==3.1.78',
    'huaweicloudsdkges==3.1.78',
    'huaweicloudsdkgsl==3.1.78',
    'huaweicloudsdkhilens==3.1.78',
    'huaweicloudsdkhss==3.1.78',
    'huaweicloudsdkiam==3.1.78',
    'huaweicloudsdkidentitycenter==3.1.78',
    'huaweicloudsdkidentitycenterstore==3.1.78',
    'huaweicloudsdkidme==3.1.78',
    'huaweicloudsdkidmeclassicapi==3.1.78',
    'huaweicloudsdkiec==3.1.78',
    'huaweicloudsdkief==3.1.78',
    'huaweicloudsdkimage==3.1.78',
    'huaweicloudsdkimagesearch==3.1.78',
    'huaweicloudsdkims==3.1.78',
    'huaweicloudsdkiotanalytics==3.1.78',
    'huaweicloudsdkiotda==3.1.78',
    'huaweicloudsdkiotedge==3.1.78',
    'huaweicloudsdkivs==3.1.78',
    'huaweicloudsdkkafka==3.1.78',
    'huaweicloudsdkkms==3.1.78',
    'huaweicloudsdkkoomessage==3.1.78',
    'huaweicloudsdkkps==3.1.78',
    'huaweicloudsdklakeformation==3.1.78',
    'huaweicloudsdklive==3.1.78',
    'huaweicloudsdklts==3.1.78',
    'huaweicloudsdkmapds==3.1.78',
    'huaweicloudsdkmas==3.1.78',
    'huaweicloudsdkmeeting==3.1.78',
    'huaweicloudsdkmetastudio==3.1.78',
    'huaweicloudsdkmoderation==3.1.78',
    'huaweicloudsdkmpc==3.1.78',
    'huaweicloudsdkmrs==3.1.78',
    'huaweicloudsdkmsgsms==3.1.78',
    'huaweicloudsdkmssi==3.1.78',
    'huaweicloudsdknat==3.1.78',
    'huaweicloudsdknlp==3.1.78',
    'huaweicloudsdkobs==3.1.78',
    'huaweicloudsdkocr==3.1.78',
    'huaweicloudsdkoctopus==3.1.78',
    'huaweicloudsdkoms==3.1.78',
    'huaweicloudsdkoptverse==3.1.78',
    'huaweicloudsdkorganizations==3.1.78',
    'huaweicloudsdkoroas==3.1.78',
    'huaweicloudsdkosm==3.1.78',
    'huaweicloudsdkpangulargemodels==3.1.78',
    'huaweicloudsdkprojectman==3.1.78',
    'huaweicloudsdkrabbitmq==3.1.78',
    'huaweicloudsdkram==3.1.78',
    'huaweicloudsdkrds==3.1.78',
    'huaweicloudsdkres==3.1.78',
    'huaweicloudsdkrgc==3.1.78',
    'huaweicloudsdkrms==3.1.78',
    'huaweicloudsdkrocketmq==3.1.78',
    'huaweicloudsdkroma==3.1.78',
    'huaweicloudsdksa==3.1.78',
    'huaweicloudsdkscm==3.1.78',
    'huaweicloudsdksdrs==3.1.78',
    'huaweicloudsdksecmaster==3.1.78',
    'huaweicloudsdkservicestage==3.1.78',
    'huaweicloudsdksfsturbo==3.1.78',
    'huaweicloudsdksis==3.1.78',
    'huaweicloudsdksmn==3.1.78',
    'huaweicloudsdksms==3.1.78',
    'huaweicloudsdkswr==3.1.78',
    'huaweicloudsdktics==3.1.78',
    'huaweicloudsdktms==3.1.78',
    'huaweicloudsdkugo==3.1.78',
    'huaweicloudsdkvas==3.1.78',
    'huaweicloudsdkvcm==3.1.78',
    'huaweicloudsdkvod==3.1.78',
    'huaweicloudsdkvpc==3.1.78',
    'huaweicloudsdkvpcep==3.1.78',
    'huaweicloudsdkvpn==3.1.78',
    'huaweicloudsdkwaf==3.1.78',
    'huaweicloudsdkworkspace==3.1.78',
    'huaweicloudsdkworkspaceapp==3.1.78',
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
