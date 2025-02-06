# Poetry

Tool to manage dependencies

### Resolve 

`% poetry show --tree`

### Env
- Create new virtualenv: `poetry env use python3.8`
- Create in cwd: `poetry config virtualenvs.in-project true --local`
- Set global: `poetry config virtualenvs.in-project true`
- Activate: `poetry shell`
- See info: `poetry env info`
- List envs associated with project: `poetry env list`
- Delete one: `poetry env remove <name> (get name from info).
- Install dependencies: `poetry install` or `poetry install —no-dev`

## Dependencies
1. Lock and update all: `poetry lock`
2. Lock but do not update existing: `poetry lock --no-update`

### Tilde (~) - More Conservative:
- Allows patch-level updates only
- ~1.2.3 allows updates to 1.2.4, 1.2.5, etc., but not 1.3.0
- Only the last number can change

### Caret (^) - More Flexible:
- Allows both minor and patch-level updates
- ^1.2.3 allows updates to 1.2.4, 1.3.0, 1.9.9, etc., but not 2.0.0
- Any number can change as long as the first non-zero number stays the same
