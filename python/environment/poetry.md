# Poetry

Tool to manage dependencies

### Resolve 

`% poetry show --tree`

## Dependencies

### Tilde (~) - More Conservative:
- Allows patch-level updates only
- ~1.2.3 allows updates to 1.2.4, 1.2.5, etc., but not 1.3.0
- Only the last number can change

### Caret (^) - More Flexible:
- Allows both minor and patch-level updates
- ^1.2.3 allows updates to 1.2.4, 1.3.0, 1.9.9, etc., but not 2.0.0
- Any number can change as long as the first non-zero number stays the same
