from datadog_checks.updatenotifier import UpdatenotifierCheck


def test_check(aggregator, instance):
    check = UpdatenotifierCheck('updatenotifier', {}, {})
    check.check(instance)

    aggregator.assert_all_metrics_covered()
