from ddtrace.appsec.iast.reporter import Evidence
from ddtrace.appsec.iast.reporter import Location
from ddtrace.appsec.iast.reporter import Source
from ddtrace.appsec.iast.reporter import Vulnerability


# e and e2 must be logically equal, f and g not equal to e


def _do_assert_hash(e, f, g, e2):
    assert hash(e) == hash(e2)
    assert hash(e) != hash(f) and hash(f) != hash(g) and hash(g) != hash(e)


def _do_assert_equality(e, f, g, e2):
    assert e == e2
    assert e != f and f != g and g != e


def test_evidence_hash_and_equality():
    e = Evidence(type="SomeEvidenceType", value="SomeEvidenceValue")
    f = Evidence(type="SomeOtherEvidenceType", value="SomeEvidenceValue")
    g = Evidence(type="SomeEvidenceType", value="SomeOtherEvidenceValue")
    e2 = Evidence(type="SomeEvidenceType", value="SomeEvidenceValue")

    _do_assert_hash(e, f, g, e2)
    _do_assert_equality(e, f, g, e2)


def test_location_hash_and_equality():
    e = Location(path="foobar.py", line=35, spanId=123)
    f = Location(path="foobar2.py", line=35, spanId=123)
    g = Location(path="foobar.py", line=36, spanId=123)
    e2 = Location(path="foobar.py", line=35, spanId=123)

    _do_assert_hash(e, f, g, e2)
    _do_assert_equality(e, f, g, e2)


def test_vulnerability_hash_and_equality():
    ev1 = Evidence(type="SomeEvidenceType", value="SomeEvidenceValue")
    ev1bis = Evidence(type="SomeEvidenceType", value="SomeEvidenceValue")
    ev2 = Evidence(type="SomeOtherEvidenceType", value="SomeEvidenceValue")

    loc = Location(path="foobar.py", line=35, spanId=123)

    e = Vulnerability(type="VulnerabilityType", evidence=ev1, location=loc)
    f = Vulnerability(type="VulnerabilityType", evidence=ev2, location=loc)
    g = Vulnerability(type="OtherVulnerabilityType", evidence=ev1, location=loc)
    e2 = Vulnerability(type="VulnerabilityType", evidence=ev1bis, location=loc)

    assert e.hash

    _do_assert_hash(e, f, g, e2)
    _do_assert_equality(e, f, g, e2)


def test_source_hash_and_equality():
    e = Source(origin="SomeOrigin", name="SomeName", value="SomeValue")
    f = Source(origin="SomeOtherOrigin", name="SomeName", value="SomeValue")
    g = Source(origin="SomeOrigin", name="SomeOtherName", value="SomeValue")
    e2 = Source(origin="SomeOrigin", name="SomeName", value="SomeValue")

    _do_assert_hash(e, f, g, e2)
    _do_assert_equality(e, f, g, e2)