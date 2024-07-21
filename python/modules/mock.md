# Mock

Use with unit testing to mock inputs

```
python
@mock.patch.object(Object, "method", return_value=value, autospec=True)
def test_mock(mock_raw_data):
```