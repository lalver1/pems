# Making a release

This list outlines the manual steps needed to make a new release of the
`pems` app.

A release is made by pushing an annotated [tag](https://git-scm.com/book/en/v2/Git-Basics-Tagging) that is named after the version number for the app and the release. The name of the tag must use the version number format mentioned below. Pushing an annotated tag kicks off a deployment (implemented as a GitHub Actions workflow) that builds, tags, and pushes the app's image to the GitHub Container Registry and then creates a GitHub release. It is often useful to monitor the release process by looking at the [status of the Deploy workflow](https://github.com/compilerla/pems/actions/workflows/deploy.yml) under the `Actions` section of the repository.

The list of releases can be found on the [repository's Releases page](https://github.com/compilerla/pems/releases)
on GitHub.

## 0. Decide on the new version number and create a `Release process Issue`

A new release implies a new version.

`pems` uses the [CalVer](https://calver.org/) versioning scheme, where
version numbers look like: `YYYY.0M.R`

- `YYYY` is the 4-digit year of the release; e.g. `2024`, `2025`
- `0M` is the 2-digit, 0-padded month of the release; e.g. `02` is February, `12`
  is December.
- `R` is the 1-based release counter for the given year and month;
  e.g. `1` for the first release of the month, `2` for the second, and so on.

Version numbers for release candidates append `-rcR`, where `R` is the 1-based release counter for the anticipated release. For example, the first release candidate for the `2025.01.1` release would be `2025.01.1-rc1`.

To coordinate the work that's required for a release, a `Release process Issue` needs to be created. The button below will help you start a new `Release process Issue` by using an Issue template.

[Start a new Release on Github](https://github.com/compilerla/pems/issues/new?labels=release&template=release.yml&title=Make+a+Release){ .md-button }

## 1. Create a release candidate tag on `main` and push it

```bash
git fetch
git checkout main
git reset --hard origin/main
git tag -a YYYY.0M.R-rcR
```

Git will open your default text editor and prompt you for the tag annotation. For the tag annotation, use `Release candidate R for YYYY.0M.R`. For example, `Release candidate 2 for 2025.01.1` would be the annotation for the second release candidate of the first release of January 2025. Finally, after closing the text editor:

```bash
git push origin YYYY.0M.R-rcR
```

This builds a new package, tags it, and pushes the app's image to GitHub Container Registry. No GitHub release is created for release candidates.

## 2. Create a release tag on `main` and push it

```bash
git fetch
git checkout main
git reset --hard origin/main
git tag -a YYYY.0M.R
```

Git will open your default text editor and prompt you for the tag annotation. For the tag annotation, use the title of the Release process issue that kicked off the release. Finally, after closing the text editor:

```bash
git push origin YYYY.0M.R
```

This builds the package, tags it, pushes the app's image to GitHub Container Registry, and creates a GitHub release.

## 3. [Generate release notes](https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes)

Edit release notes with additional context, images, animations, etc. as-needed and link to the `Release process Issue`.
