OMERO.web django-prometheus
===========================

Install and configure Django Prometheus exporter for OMERO.web.
Assumes OMERO.web has been installed using the openmicroscopy.omero-web role.

See https://github.com/korfuri/django-prometheus

Note: metric endpoint `/django_prometheus/metrics` is not authenticated.


Example playbook
----------------

    - hosts: localhost
      roles:
      - role: openmicroscopy.omero-web
      - role: omero-web-django-prometheus


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
