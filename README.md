# Homepage Repo

This repository contains two separate [Hugo](https://gohugo.io/) websites plus a small helper script.

## Structure

- `main/`: personal homepage built with the `academic` Hugo theme.
- `alt/`: blog-style site built with the `even` Hugo theme.
- `bin/meta.py`: helper script for updating Markdown front matter metadata such as `lastmod`.

Each site is independent and has its own Hugo config, content, static files, and vendored theme.

## Prerequisites

Install Hugo Extended on Ubuntu:

```bash
sudo apt update
sudo apt install hugo
```

Verify that the installed build is the extended edition:

```bash
hugo version
```

The version string should include `+extended`.

## Build

Build the academic homepage:

```bash
cd main
hugo
```

Generated files will be written to `main/public/`.
To preview the website directly, simply do `hugo server`.

The same applies to the blog site, under `alt/`.
Generated files will be written to `alt/public/`.

## Important Note

Do not open generated `public/*.html` files directly with `file://` in a browser.
These sites use root-relative asset URLs such as `/css/academic.css`,
so they should be viewed through an HTTP server such as `hugo server`.
