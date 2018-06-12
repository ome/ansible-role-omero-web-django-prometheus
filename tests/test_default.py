import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_django_exporter_metrics(Command):
    out = Command.check_output(
        'curl http://localhost/django_prometheus/metrics')
    assert "django_http_responses_body_total_bytes_count" in out
