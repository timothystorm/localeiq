# LocaleIQ

## Using the LocaleIQ meta-repo (submodule)

### Setup

```bash
git submodule add https://github.com/timothystorm/localeiq-api.git api
```

```bash
git submodule add https://github.com/timothystorm/localeiq-ui.git ui
```

```bash
git submodule add https://github.com/timothystorm/localeiq-data.git data
```

### Cloning meta-repo

```bash
git clone --recurse-submodules https://github.com/timothystorm/localeiq.git
```

#### Or if you forget to clone 

```bash
git submodule update --init --recursive
```

### Making changes to submodules

If you make changes to `/api`; commit them in that submodule and you also need to update the meta-repo pointer:

```bash
# Step 1: Make changes in submodule /api
cd api
# .. make edits ..
git commit -m "*** commit message ***"
git push

# Step 2: Update parent repo to point to the new commit(s)
cd ..
git add api
git commit -m "update submodule pointer for api"
git push
```

