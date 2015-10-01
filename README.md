# cookiecutter-demands-pypackage

Cookiecutter template for a [demands](https://github.com/yola/demands) API
client library package. Based on [cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
See  [cookiecutter](https://github.com/audreyr/cookiecutter).

* Free software: MIT license
* Vanilla testing setup with `unittest` and `python setup.py test`
* [Travis-CI](http://travis-ci.org/): Ready for Travis Continuous Integration testing
* [Tox](http://testrun.org/tox/) testing: Setup to easily test Python 2.7, 3.3, 3.4, and 3.5 by default.
* [Sphinx](http://sphinx-doc.org/) docs: Documentation ready for generation with, for example, [ReadTheDocs](https://readthedocs.org/)

## Usage

Generate a Python package project::

    cookiecutter https://github.com/zoidbergwill/cookiecutter-demands-pypackage.git

Then:

* Create a repo and put it there.
* Add the repo to your Travis CI account.
* Add the repo to your ReadTheDocs account + turn on the ReadTheDocs service hook.
* Release your package the standard Python way. Here's a release checklist: https://gist.github.com/audreyr/5990987
