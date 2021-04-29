===============================
{{ cookiecutter.package_name }}
===============================

{{ cookiecutter.project_short_description }}

### Tagging a new release

Tagging releases is straightforward with [`rever`](https://regro.github.io/rever-docs). By calling a single command, you'll be able to:  
* increment the version number in both `setup.py` and `__init.py`
* update the `CHAGELOG`
* generate a new git tag
* push all changes back up to GitHub. 

We can run a quick check to make sure you have permissios and proper libraries installed:

```bash
rever check
```

When you are ready to release run `rever <new_version_number>` and rever will take care of the rest. 


