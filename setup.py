# -*- coding: utf-8 -*-
"""Installer for the c2.search.llm package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='c2.search.llm',
    version='1.0a1',
    description="This product is for searching by LLM on Plone.",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone CMS',
    author='Manabu TERADA',
    author_email='terada@cmscom.jp',
    url='https://github.com/collective/c2.search.llm',
    project_urls={
        'PyPI': 'https://pypi.org/project/c2.search.llm/',
        'Source': 'https://github.com/collective/c2.search.llm',
        'Tracker': 'https://github.com/collective/c2.search.llm/issues',
        # 'Documentation': 'https://c2.search.llm.readthedocs.io/en/latest/',
    },
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['c2', 'c2.search'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.7",
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'z3c.jbot',
        'plone.api>=1.8.4',
        'plone.app.dexterity',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            'plone.testing>=5.0.0',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = c2.search.llm.locales.update:update_locale
    """,
)
