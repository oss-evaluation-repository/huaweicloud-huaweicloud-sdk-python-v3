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
VERSION = "3.1.87"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.87',
    'huaweicloudsdkaad==3.1.87',
    'huaweicloudsdkantiddos==3.1.87',
    'huaweicloudsdkaom==3.1.87',
    'huaweicloudsdkaos==3.1.87',
    'huaweicloudsdkapig==3.1.87',
    'huaweicloudsdkapm==3.1.87',
    'huaweicloudsdkas==3.1.87',
    'huaweicloudsdkasm==3.1.87',
    'huaweicloudsdkbcs==3.1.87',
    'huaweicloudsdkbms==3.1.87',
    'huaweicloudsdkbss==3.1.87',
    'huaweicloudsdkbssintl==3.1.87',
    'huaweicloudsdkcae==3.1.87',
    'huaweicloudsdkcampusgo==3.1.87',
    'huaweicloudsdkcbh==3.1.87',
    'huaweicloudsdkcbr==3.1.87',
    'huaweicloudsdkcbs==3.1.87',
    'huaweicloudsdkcc==3.1.87',
    'huaweicloudsdkcce==3.1.87',
    'huaweicloudsdkccm==3.1.87',
    'huaweicloudsdkcdm==3.1.87',
    'huaweicloudsdkcdn==3.1.87',
    'huaweicloudsdkces==3.1.87',
    'huaweicloudsdkcfw==3.1.87',
    'huaweicloudsdkcgs==3.1.87',
    'huaweicloudsdkclassroom==3.1.87',
    'huaweicloudsdkcloudide==3.1.87',
    'huaweicloudsdkcloudpond==3.1.87',
    'huaweicloudsdkcloudrtc==3.1.87',
    'huaweicloudsdkcloudtable==3.1.87',
    'huaweicloudsdkcloudtest==3.1.87',
    'huaweicloudsdkcodeartsartifact==3.1.87',
    'huaweicloudsdkcodeartsbuild==3.1.87',
    'huaweicloudsdkcodeartscheck==3.1.87',
    'huaweicloudsdkcodeartsdeploy==3.1.87',
    'huaweicloudsdkcodeartsinspector==3.1.87',
    'huaweicloudsdkcodeartspipeline==3.1.87',
    'huaweicloudsdkcodecraft==3.1.87',
    'huaweicloudsdkcodehub==3.1.87',
    'huaweicloudsdkconfig==3.1.87',
    'huaweicloudsdkcph==3.1.87',
    'huaweicloudsdkcpts==3.1.87',
    'huaweicloudsdkcse==3.1.87',
    'huaweicloudsdkcsms==3.1.87',
    'huaweicloudsdkcss==3.1.87',
    'huaweicloudsdkcts==3.1.87',
    'huaweicloudsdkdas==3.1.87',
    'huaweicloudsdkdataartsstudio==3.1.87',
    'huaweicloudsdkdbss==3.1.87',
    'huaweicloudsdkdc==3.1.87',
    'huaweicloudsdkdcs==3.1.87',
    'huaweicloudsdkddm==3.1.87',
    'huaweicloudsdkdds==3.1.87',
    'huaweicloudsdkdeh==3.1.87',
    'huaweicloudsdkdevsecurity==3.1.87',
    'huaweicloudsdkdevstar==3.1.87',
    'huaweicloudsdkdgc==3.1.87',
    'huaweicloudsdkdis==3.1.87',
    'huaweicloudsdkdlf==3.1.87',
    'huaweicloudsdkdli==3.1.87',
    'huaweicloudsdkdns==3.1.87',
    'huaweicloudsdkdris==3.1.87',
    'huaweicloudsdkdrs==3.1.87',
    'huaweicloudsdkdsc==3.1.87',
    'huaweicloudsdkdwr==3.1.87',
    'huaweicloudsdkdws==3.1.87',
    'huaweicloudsdkec==3.1.87',
    'huaweicloudsdkecs==3.1.87',
    'huaweicloudsdkedgesec==3.1.87',
    'huaweicloudsdkeg==3.1.87',
    'huaweicloudsdkeihealth==3.1.87',
    'huaweicloudsdkeip==3.1.87',
    'huaweicloudsdkelb==3.1.87',
    'huaweicloudsdkeps==3.1.87',
    'huaweicloudsdker==3.1.87',
    'huaweicloudsdkevs==3.1.87',
    'huaweicloudsdkfrs==3.1.87',
    'huaweicloudsdkfunctiongraph==3.1.87',
    'huaweicloudsdkga==3.1.87',
    'huaweicloudsdkgaussdb==3.1.87',
    'huaweicloudsdkgaussdbfornosql==3.1.87',
    'huaweicloudsdkgaussdbforopengauss==3.1.87',
    'huaweicloudsdkgeip==3.1.87',
    'huaweicloudsdkges==3.1.87',
    'huaweicloudsdkgsl==3.1.87',
    'huaweicloudsdkhilens==3.1.87',
    'huaweicloudsdkhss==3.1.87',
    'huaweicloudsdkiam==3.1.87',
    'huaweicloudsdkiamaccessanalyzer==3.1.87',
    'huaweicloudsdkidentitycenter==3.1.87',
    'huaweicloudsdkidentitycenterstore==3.1.87',
    'huaweicloudsdkidme==3.1.87',
    'huaweicloudsdkidmeclassicapi==3.1.87',
    'huaweicloudsdkiec==3.1.87',
    'huaweicloudsdkief==3.1.87',
    'huaweicloudsdkimage==3.1.87',
    'huaweicloudsdkimagesearch==3.1.87',
    'huaweicloudsdkims==3.1.87',
    'huaweicloudsdkiotanalytics==3.1.87',
    'huaweicloudsdkiotda==3.1.87',
    'huaweicloudsdkiotedge==3.1.87',
    'huaweicloudsdkivs==3.1.87',
    'huaweicloudsdkkafka==3.1.87',
    'huaweicloudsdkkms==3.1.87',
    'huaweicloudsdkkoomessage==3.1.87',
    'huaweicloudsdkkps==3.1.87',
    'huaweicloudsdklakeformation==3.1.87',
    'huaweicloudsdklive==3.1.87',
    'huaweicloudsdklts==3.1.87',
    'huaweicloudsdkmapds==3.1.87',
    'huaweicloudsdkmas==3.1.87',
    'huaweicloudsdkmeeting==3.1.87',
    'huaweicloudsdkmetastudio==3.1.87',
    'huaweicloudsdkmoderation==3.1.87',
    'huaweicloudsdkmpc==3.1.87',
    'huaweicloudsdkmrs==3.1.87',
    'huaweicloudsdkmsgsms==3.1.87',
    'huaweicloudsdkmssi==3.1.87',
    'huaweicloudsdknat==3.1.87',
    'huaweicloudsdknlp==3.1.87',
    'huaweicloudsdkobs==3.1.87',
    'huaweicloudsdkocr==3.1.87',
    'huaweicloudsdkoctopus==3.1.87',
    'huaweicloudsdkoms==3.1.87',
    'huaweicloudsdkoptverse==3.1.87',
    'huaweicloudsdkorganizations==3.1.87',
    'huaweicloudsdkorgid==3.1.87',
    'huaweicloudsdkoroas==3.1.87',
    'huaweicloudsdkosm==3.1.87',
    'huaweicloudsdkpangulargemodels==3.1.87',
    'huaweicloudsdkprojectman==3.1.87',
    'huaweicloudsdkrabbitmq==3.1.87',
    'huaweicloudsdkram==3.1.87',
    'huaweicloudsdkrds==3.1.87',
    'huaweicloudsdkres==3.1.87',
    'huaweicloudsdkrgc==3.1.87',
    'huaweicloudsdkrms==3.1.87',
    'huaweicloudsdkrocketmq==3.1.87',
    'huaweicloudsdkroma==3.1.87',
    'huaweicloudsdksa==3.1.87',
    'huaweicloudsdkscm==3.1.87',
    'huaweicloudsdksdrs==3.1.87',
    'huaweicloudsdksecmaster==3.1.87',
    'huaweicloudsdkservicestage==3.1.87',
    'huaweicloudsdksfsturbo==3.1.87',
    'huaweicloudsdksis==3.1.87',
    'huaweicloudsdksmn==3.1.87',
    'huaweicloudsdksms==3.1.87',
    'huaweicloudsdkswr==3.1.87',
    'huaweicloudsdktics==3.1.87',
    'huaweicloudsdktms==3.1.87',
    'huaweicloudsdkugo==3.1.87',
    'huaweicloudsdkvas==3.1.87',
    'huaweicloudsdkvcm==3.1.87',
    'huaweicloudsdkvod==3.1.87',
    'huaweicloudsdkvpc==3.1.87',
    'huaweicloudsdkvpcep==3.1.87',
    'huaweicloudsdkvpn==3.1.87',
    'huaweicloudsdkwaf==3.1.87',
    'huaweicloudsdkworkspace==3.1.87',
    'huaweicloudsdkworkspaceapp==3.1.87',
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
