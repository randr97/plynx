#!/usr/bin/env python
import plynx
from setuptools import setup, find_packages

install_requires = [
    'boto>=2.48.0',
    'pymongo>=3.5.1',
    'pyyaml>=3.11',
    'passlib>=1.7.1',
    'itsdangerous>=0.24',
    'Flask>=0.12.2',
    'Flask-Cors>=3.0.3',
    'Flask-HTTPAuth>=3.2.3',
    'gevent>=1.3.7',
    'requests>=2.18.4',
]

setup(
    name='plynx',
    version=plynx.__version__,
    description='ML platform',
    long_description='Interactive, Scalable, Shareable and Reproducible ML experiments',
    url='https://plynx.com',
    author='Ivan Khomyakov',
    author_email='ivan@plynx.com',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Environment :: Console',
        'Environment :: Web Environment',

        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',

        'License :: OSI Approved :: Apache Software License',

        'Operating System :: POSIX',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3'

        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
    keywords='data science, machine learning, pipeline, workflow, experiments',
    packages=find_packages(exclude=['scripts', 'docker']),
    install_requires=install_requires,
    package_data={  # Optional
        # 'sample': ['package_data.dat'],
    },
    entry_points={  # Optional
        'console_scripts': [
            'plynx=plynx.bin:main',
        ],
    },
    project_urls={  # Optional
        'Demo': 'https://plynx.com',
        'Source': 'https://github.com/khaxis/plynx',
    },
    # plynx.graph.base_nodes.collection uses reference to __file__
    zip_safe=False,
)