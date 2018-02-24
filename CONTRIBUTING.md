# How to contribute


## Reporting bugs

If you find a bug in this project, please [open an issue](https://github.com/breard-r/django-npb/issues) and describe the problem. When reporting a bug, please follow the generic [bug reporting recommendations](http://www.chiark.greenend.org.uk/~sgtatham/bugs.html).


## Translating


You know a language not yet supported and want to add it? You can improve the current supported translations? Please contribute!
If you know git and python development, you can read [Django's localization howto](https://docs.djangoproject.com/en/2.0/topics/i18n/translation/#localization-how-to-create-language-files) and open a pull request. If you don't, please [open an issue](https://github.com/breard-r/django-npb/issues) where you paste a translated [language file](https://github.com/breard-r/django-npb/blob/master/npb/locale/en/LC_MESSAGES/django.po).

## Writing tests

This project would use more tests, for example about permissions. If you are interested in writing tests, please open a pull request.


## Pull requests

When submitting code, please follow the following guidelines:

- report any remarkable change in the change log;
- document every publicly accessible item (module, function, …) and insert examples;
- write unit tests that checks your code is working well;
- for bug-fixes, write unit tests showing the corrected bug;
- for new features, do not forget to create the C-bindings;
- yes, unit tests have to be written for C-bindings too;
- **launch the test suite before submitting your code**, obviously every single test have to pass.

## Coding style

- Follow [PEP8](https://www.python.org/dev/peps/pep-0008/) as much as possible;
- indent code with 4 spaces;
- no trailing whitespace at the end of lines;
- use descriptive variable names;
- functions should be as short as possible, do only one thing and do it well.

In a more general way, if you feel your code doesn't look like the project's one, fix it.
