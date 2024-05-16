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
VERSION = "3.1.96"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.96',
    'huaweicloudsdkaad==3.1.96',
    'huaweicloudsdkantiddos==3.1.96',
    'huaweicloudsdkaom==3.1.96',
    'huaweicloudsdkaos==3.1.96',
    'huaweicloudsdkapig==3.1.96',
    'huaweicloudsdkapm==3.1.96',
    'huaweicloudsdkas==3.1.96',
    'huaweicloudsdkasm==3.1.96',
    'huaweicloudsdkbcs==3.1.96',
    'huaweicloudsdkbms==3.1.96',
    'huaweicloudsdkbss==3.1.96',
    'huaweicloudsdkbssintl==3.1.96',
    'huaweicloudsdkcae==3.1.96',
    'huaweicloudsdkcampusgo==3.1.96',
    'huaweicloudsdkcbh==3.1.96',
    'huaweicloudsdkcbr==3.1.96',
    'huaweicloudsdkcbs==3.1.96',
    'huaweicloudsdkcc==3.1.96',
    'huaweicloudsdkcce==3.1.96',
    'huaweicloudsdkccm==3.1.96',
    'huaweicloudsdkcdm==3.1.96',
    'huaweicloudsdkcdn==3.1.96',
    'huaweicloudsdkces==3.1.96',
    'huaweicloudsdkcfw==3.1.96',
    'huaweicloudsdkcgs==3.1.96',
    'huaweicloudsdkclassroom==3.1.96',
    'huaweicloudsdkcloudide==3.1.96',
    'huaweicloudsdkcloudpond==3.1.96',
    'huaweicloudsdkcloudrtc==3.1.96',
    'huaweicloudsdkcloudtable==3.1.96',
    'huaweicloudsdkcloudtest==3.1.96',
    'huaweicloudsdkcodeartsartifact==3.1.96',
    'huaweicloudsdkcodeartsbuild==3.1.96',
    'huaweicloudsdkcodeartscheck==3.1.96',
    'huaweicloudsdkcodeartsdeploy==3.1.96',
    'huaweicloudsdkcodeartsinspector==3.1.96',
    'huaweicloudsdkcodeartspipeline==3.1.96',
    'huaweicloudsdkcodecraft==3.1.96',
    'huaweicloudsdkcodehub==3.1.96',
    'huaweicloudsdkconfig==3.1.96',
    'huaweicloudsdkcph==3.1.96',
    'huaweicloudsdkcpts==3.1.96',
    'huaweicloudsdkcse==3.1.96',
    'huaweicloudsdkcsms==3.1.96',
    'huaweicloudsdkcss==3.1.96',
    'huaweicloudsdkcts==3.1.96',
    'huaweicloudsdkdas==3.1.96',
    'huaweicloudsdkdataartsstudio==3.1.96',
    'huaweicloudsdkdbss==3.1.96',
    'huaweicloudsdkdc==3.1.96',
    'huaweicloudsdkdcs==3.1.96',
    'huaweicloudsdkddm==3.1.96',
    'huaweicloudsdkdds==3.1.96',
    'huaweicloudsdkdeh==3.1.96',
    'huaweicloudsdkdevsecurity==3.1.96',
    'huaweicloudsdkdevstar==3.1.96',
    'huaweicloudsdkdgc==3.1.96',
    'huaweicloudsdkdis==3.1.96',
    'huaweicloudsdkdlf==3.1.96',
    'huaweicloudsdkdli==3.1.96',
    'huaweicloudsdkdns==3.1.96',
    'huaweicloudsdkdris==3.1.96',
    'huaweicloudsdkdrs==3.1.96',
    'huaweicloudsdkdsc==3.1.96',
    'huaweicloudsdkdwr==3.1.96',
    'huaweicloudsdkdws==3.1.96',
    'huaweicloudsdkec==3.1.96',
    'huaweicloudsdkecs==3.1.96',
    'huaweicloudsdkedgesec==3.1.96',
    'huaweicloudsdkeg==3.1.96',
    'huaweicloudsdkeihealth==3.1.96',
    'huaweicloudsdkeip==3.1.96',
    'huaweicloudsdkelb==3.1.96',
    'huaweicloudsdkeps==3.1.96',
    'huaweicloudsdker==3.1.96',
    'huaweicloudsdkevs==3.1.96',
    'huaweicloudsdkfrs==3.1.96',
    'huaweicloudsdkfunctiongraph==3.1.96',
    'huaweicloudsdkga==3.1.96',
    'huaweicloudsdkgaussdb==3.1.96',
    'huaweicloudsdkgaussdbfornosql==3.1.96',
    'huaweicloudsdkgaussdbforopengauss==3.1.96',
    'huaweicloudsdkgeip==3.1.96',
    'huaweicloudsdkges==3.1.96',
    'huaweicloudsdkgsl==3.1.96',
    'huaweicloudsdkhilens==3.1.96',
    'huaweicloudsdkhss==3.1.96',
    'huaweicloudsdkiam==3.1.96',
    'huaweicloudsdkiamaccessanalyzer==3.1.96',
    'huaweicloudsdkidentitycenter==3.1.96',
    'huaweicloudsdkidentitycenterstore==3.1.96',
    'huaweicloudsdkidme==3.1.96',
    'huaweicloudsdkidmeclassicapi==3.1.96',
    'huaweicloudsdkiec==3.1.96',
    'huaweicloudsdkief==3.1.96',
    'huaweicloudsdkimage==3.1.96',
    'huaweicloudsdkimagesearch==3.1.96',
    'huaweicloudsdkims==3.1.96',
    'huaweicloudsdkiotanalytics==3.1.96',
    'huaweicloudsdkiotda==3.1.96',
    'huaweicloudsdkiotedge==3.1.96',
    'huaweicloudsdkivs==3.1.96',
    'huaweicloudsdkkafka==3.1.96',
    'huaweicloudsdkkms==3.1.96',
    'huaweicloudsdkkoomessage==3.1.96',
    'huaweicloudsdkkps==3.1.96',
    'huaweicloudsdklakeformation==3.1.96',
    'huaweicloudsdklive==3.1.96',
    'huaweicloudsdklts==3.1.96',
    'huaweicloudsdkmapds==3.1.96',
    'huaweicloudsdkmas==3.1.96',
    'huaweicloudsdkmeeting==3.1.96',
    'huaweicloudsdkmetastudio==3.1.96',
    'huaweicloudsdkmoderation==3.1.96',
    'huaweicloudsdkmpc==3.1.96',
    'huaweicloudsdkmrs==3.1.96',
    'huaweicloudsdkmsgsms==3.1.96',
    'huaweicloudsdkmssi==3.1.96',
    'huaweicloudsdknat==3.1.96',
    'huaweicloudsdknlp==3.1.96',
    'huaweicloudsdkobs==3.1.96',
    'huaweicloudsdkocr==3.1.96',
    'huaweicloudsdkoctopus==3.1.96',
    'huaweicloudsdkoms==3.1.96',
    'huaweicloudsdkoptverse==3.1.96',
    'huaweicloudsdkorganizations==3.1.96',
    'huaweicloudsdkorgid==3.1.96',
    'huaweicloudsdkoroas==3.1.96',
    'huaweicloudsdkosm==3.1.96',
    'huaweicloudsdkpangulargemodels==3.1.96',
    'huaweicloudsdkprojectman==3.1.96',
    'huaweicloudsdkrabbitmq==3.1.96',
    'huaweicloudsdkram==3.1.96',
    'huaweicloudsdkrds==3.1.96',
    'huaweicloudsdkres==3.1.96',
    'huaweicloudsdkrgc==3.1.96',
    'huaweicloudsdkrms==3.1.96',
    'huaweicloudsdkrocketmq==3.1.96',
    'huaweicloudsdkroma==3.1.96',
    'huaweicloudsdksa==3.1.96',
    'huaweicloudsdkscm==3.1.96',
    'huaweicloudsdksdrs==3.1.96',
    'huaweicloudsdksecmaster==3.1.96',
    'huaweicloudsdkservicestage==3.1.96',
    'huaweicloudsdksfsturbo==3.1.96',
    'huaweicloudsdksis==3.1.96',
    'huaweicloudsdksmn==3.1.96',
    'huaweicloudsdksms==3.1.96',
    'huaweicloudsdksts==3.1.96',
    'huaweicloudsdkswr==3.1.96',
    'huaweicloudsdktics==3.1.96',
    'huaweicloudsdktms==3.1.96',
    'huaweicloudsdkugo==3.1.96',
    'huaweicloudsdkvas==3.1.96',
    'huaweicloudsdkvcm==3.1.96',
    'huaweicloudsdkvod==3.1.96',
    'huaweicloudsdkvpc==3.1.96',
    'huaweicloudsdkvpcep==3.1.96',
    'huaweicloudsdkvpn==3.1.96',
    'huaweicloudsdkwaf==3.1.96',
    'huaweicloudsdkworkspace==3.1.96',
    'huaweicloudsdkworkspaceapp==3.1.96',
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
