django-admin-approx-count
=========================

A dirty mixin to rescue from dumb `count(*)` query of Django admin


What is this for?
-----------------

Django admin works well with less set of rows.

But it slows down on large database system - every single list page of admin needs `SELECT COUNT(*) FROM TABLE` query to calculate the count of rows.
And this causes severe performance issues on production system. 

We don't really want to know *EXACT* count of rows. Right? Then use this.

See this [Stackoverflow question](http://stackoverflow.com/questions/10433173/prevent-django-admin-from-running-select-count-on-the-list-form)


Installation
------------

    pip install django-admin-approx-count

or, download / clone from [source repo](https://github.com/lqez/django-admin-approx-count)


Usage
-----

Use shipped mixin in `admin.py`.

    from approx_count.mixin import MaxIdAdminMixin, TableStatusMixin

    class SomeAdmin(MaxIdAdminMixin):
        ...

    class AnotherAdmin(TableStatusMixin):
        ...


Mixins
------

Default django queryset uses `SELECT COUNT(*) FROM TABLE` to calculate row count. However,

 - `MaxIdAdminMixin` uses `SELECT MAX(ID) FROM TABLE`.
 - `TableStatusMixin` uses table status / information.


Note
----

 - For MySQL, by Nova
    - <http://stackoverflow.com/a/10446271/366908>
 - For Postgres, by Woody Anderson
    - <http://stackoverflow.com/a/23118765/366908>


Author
------

Park Hyunwoo([@lqez](https://twitter.com/lqez))


License
-------

`django-admin-approx-count` is distributed under MIT license.
