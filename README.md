OMERO.web django-prometheus
===========================

Install and configure Django Prometheus exporter for OMERO.web.
Assumes OMERO.web has been installed using the openmicroscopy.omero-web role.

See https://github.com/korfuri/django-prometheus

Note: metric endpoint `/django_prometheus/metrics` is not authenticated.


Role Variables
--------------

Optional:
- `omero_web_django_prometheus_config_web`: Automatically set `omero.web.*` configuration properties, default `True`.
- `omero_web_django_prometheus_stats_dir`: Prometheus temporary statistics directory

**Warning** This will make configuration changes to the OMERO.web and Gunicorn configurations, see [`templates/omero-web-config-django-prometheus-omero.j2`](templates/omero-web-config-django-prometheus-omero.j2) and [`defaults/main.yml`](defaults/main.yml) for details.

If you have customised your OMERO.web installation such as installing other web apps or setting `omero.web` configuration properties ensure the configuration changes made by this role are compatible.


Example playbook
----------------

    - hosts: localhost
      roles:
      - role: openmicroscopy.omero-web
      - role: omero-web-django-prometheus


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
