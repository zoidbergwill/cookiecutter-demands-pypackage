cookiecutter-demands-pypackage
==============================

Cookiecutter template for a demands_ API client library package. Based on cookiecutter-pypackage_. See cookiecutter_.

-  Free software: MIT license
-  Vanilla testing setup with ``unittest`` and ``python setup.py test``
-  Travis-CI_: Ready for Travis Continuous
   Integration testing
-  Tox_ testing: Setup to easily test Python 2.7, 3.3, 3.4, and 3.5 by default.
-  Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_.

Usage
-----

Generate a Python package project::

    cookiecutter https://github.com/zoidbergwill/cookiecutter-demands-pypackage.git

Then:

-  Create a repo and put it there.
-  Add the repo to your Travis CI account.
-  Add the repo to your ReadTheDocs account + turn on the ReadTheDocs
   service hook.
-  Release your package the standard Python way. Here's a release
   checklist: https://gist.github.com/audreyr/5990987

Fork This / Create Your Own
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Or create your own; it doesn't strictly have to
be a fork.

* Once you have your own version working, add it to the Similar Cookiecutter Templates list above with a brief description.

* It's up to you whether or not to rename your fork/own version. Do whatever you think sounds good.

.. _demands: https://github.com/yola/demands
.. _cookiecutter-pypackage: https://github.com/audreyr/cookiecutter-pypackage
.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _Travis-CI: http://travis-ci.org/
.. _tox: http://testrun.org/tox/
.. _sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.org/
