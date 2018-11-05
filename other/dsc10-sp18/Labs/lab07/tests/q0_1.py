test = {
  'name': 'q0_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # The highest value is the 100th percentile.  What is the 91st percentile?
          >>> set(true_percentile) != set([1, 4])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> set(true_percentile) == set([1,3,4])
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
