# Smart Tek Odoo test task

This is a custom module for Odoo 16.
![image](https://github.com/me1nyk/SmartTek-odoo-task/assets/123767529/bd8fae37-050b-4386-9716-77ac2dd92fb4)


## Description

The module adds a new object called `demo.demo` with a single field named `name` of type `char`.
![image](https://github.com/me1nyk/SmartTek-odoo-task/assets/123767529/382db1b3-aa7f-4ac8-96b6-ef9e1b9c85d2)
Here is the directory structure for the Demo module:
```
addons/
    demo/
        __init__.py
        __manifest__.py
        models/
            __init__.py
            demo_models.py
        views/
            menu.xml
            demo.xml
        security/
            ir.model.access.csv
```


## Features

- Adds a new object `demo.demo` with the field `name`;
  ![image](https://github.com/me1nyk/SmartTek-odoo-task/assets/123767529/f07d7952-b1ad-47f4-8c48-193ea422e85a)

- Provides separate menu, tree view, and form view for the `demo.demo` object;
  ![image](https://github.com/me1nyk/SmartTek-odoo-task/assets/123767529/4195cc94-5dd9-44c0-ace6-829d15ddcf5d)


## Installation
- Utilize the provided [Installation Guide](https://www.odoo.com/documentation/16.0/administration/install/install.html#packaged-installers) to perform the Odoo installation on your local machine;
 
- Use this command to run server:
```
python odoo\odoo-bin -c odoo/debian/odoo.conf -d dbodoo16 -u demo
```


