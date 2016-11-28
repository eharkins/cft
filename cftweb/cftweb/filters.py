"""
Custom Jinja filters for use in CFT templates.

Learn more about Jinja filters at,
http://jinja.pocoo.org/docs/dev/api/#writing-filters

Also see typical usage in `templates/individuals.html` and `templates/index.html`

"""

from __future__ import print_function
import collections
from cftweb import app

@app.template_filter()
def clustersort(value, by=['run', 'seed', 'v_gene', 'd_gene', 'j_gene'],reverse=False):
    """Sort a dict of cluster objects by attributes supplied in `by`.

        {% for item in mydict|dictsort %}
            sort the dict by key, case insensitive

        {% for item in mydict|dictsort(true) %}
            sort the dict by key, case sensitive

        {% for item in mydict|dictsort(false, 'value') %}
            sort the dict by key, case insensitive, sorted
            normally and ordered by value.
    """
    def sort_func(item):
        value = item[1]
        return tuple(getattr(value, k) for k in by)

    return sorted(value.items(), key=sort_func, reverse=reverse)


# unique Jinja filter cribbed from ansible,
# https://github.com/ansible/ansible/blob/6787fc70a643fb6e2bdd2c6a6202072d21db72ef/lib/ansible/plugins/filter/mathstuff.py#L28
#
@app.template_filter()
def unique(a):
    if isinstance(a,collections.Hashable):
        c = set(a)
    else:
        c = []
        for x in a:
            if x not in c:
                c.append(x)
    return c

