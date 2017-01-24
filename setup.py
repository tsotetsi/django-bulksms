from setuptools import setup


CLASSIFIERS = [
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'License :: OSI Approved :: MIT License',
    'Environment :: Web Environment',
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python',
    'Framework :: Django',
    'Framework :: Django :: 1.5',
    'Framework :: Django :: 1.6',
    'Framework :: Django :: 1.7',
    'Framework :: Django :: 1.8',
    'Framework :: Django :: 1.9',
    'Framework :: Django :: 1.10',
]

setup(
    name='django-bulksms',
    description='Django BulkSMS library/API.',
    long_description='Django BulkSMS library/API',
    version='0.0.1',
    package_dir={'': 'src'},
    packages=['bulksms'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Django',
        'requests',
        'phonenumbers',
        'tenacity'
    ],
    author='Thapelo Tsotetsi',
    author_email='info@thapelotsotetsi.co.za',
    url="https://github.com/tsotetsi/django-bulksms",
    license='MIT',
    keywords='django bulk sms sending',
    classifiers=CLASSIFIERS,
)
