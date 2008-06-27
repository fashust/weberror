from setuptools import setup, find_packages
import sys, os

version = '0.9'

setup(name='WebError',
      version=version,
      description="Web Error handling and exception catching",
      long_description="""\
""",
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: Internet :: WWW/HTTP :: WSGI",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
      ],
      keywords='wsgi',
      author='Ben Bangert, Ian Bicking, Mark Ramm',
      author_email='',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      package_data = { 'weberror.evalexception': [ "*.html.tmpl", "media/*" ] },
      zip_safe=False,
      install_requires=[
        'WebOb',
        'wsgiref',
        'Tempita',
        'simplejson',
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'webtest', 'Paste'],
      entry_points="""
      [paste.filter_app_factory]
      error_catcher = weberror.errormiddleware:make_error_middleware
      evalerror = weberror.evalmiddleware:make_eval_exception
      """,
      )
