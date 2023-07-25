# YAML
- Yet Another Markup Language
- File format for data
- Common format for configuration files
- Object serialization makes it better than JSON.
    - YAML and JSON can be converted back and forth.

Simple example:

```python
---
doe: "a deer"
ray: "a drop"
xmas: true
french-hens: 3
calling-birds: 
  - huey
  - dewey
  - louie
  - fred
xmas-firth-day:
  callings-birgs: four
  french-hends: 3
  partridges:
    count: 1
    location: "pear tree"
  turtle-doves: two
```

## Outline
0. file.yaml to save.
1. File starts with x3 dashed lines.
2. Whitespace is central part of format.
3. Newline implies end of field.
4. Indentation creates structure. Can be 1 or more spaces, but no tabs.
5. Imported into python as dictionary.


### Comments
- "#" for comments; either inline or whole line

### Datatypes
- String: in single or double quotes or no quotes.
    - strings on mulple lines with "|" : useful for shell commands

```yaml
data: |
  This is a long string which
  requires multiple lines.
```

- Int: unquoted number
- Float: unquoted number
- Not-a-number: .inf, -.INT, .NAN
- Nulls: ~ or None
- Booleans: True, False, On, Off
- Arrays:
    - Inline: [1, 2, 3, 4] or ["one", "two", "three"]
    - Multiple lines: denoted by "-"; see "calling birds in example above"
- Dictionaries: 
    - Inline: numbers: {key1: val1, key2: val2}
    - Multiple lines:


## Import

```python
import yaml

stream = open("file.yaml", 'r')
dictrionary1 = yaml.load(stream)
```
