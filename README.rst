.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide_addons.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
imio.transmogrifier.PloneFormGen
==============================================================================


New blueprint to help Transmogrifier to migrate PloneFormGen objects.


Features
--------

Add new blueprint thanks in @@pipeline-config :
    
    ...
    referencesimporter
    fix_utf-8
    propertiesimporter
    ...
    
[fix_utf-8]
blueprint = imio.transmogrifier.PloneFormGen.fix_utf-8


Examples
--------

This add-on can be seen in action at the following sites:
- Is there a page on the internet where everybody can see the features?


Documentation
-------------

Full documentation for end users can be found in the "docs" folder, and is also available online at http://docs.plone.org/foo/bar


Translations
------------

This product has been translated into

- Klingon (thanks, K'Plai)


Installation
------------

Install imio.transmogrifier.PloneFormGen by adding it to your buildout::

    [buildout]

    ...

    eggs =
        imio.transmogrifier.PloneFormGen


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/imio.transmogrifier.PloneFormGen/issues
- Source Code: https://github.com/collective/imio.transmogrifier.PloneFormGen
- Documentation: https://docs.plone.org/foo/bar


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com


License
-------

The project is licensed under the GPLv2.
