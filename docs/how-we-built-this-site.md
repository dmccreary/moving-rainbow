# How We Built This Site

This page describes how we built this website and some of 
the rationale behind why we made various design choices.

## Python

MicroSims are about how we use generative AI to create
animations and simulations.  The language of AI
is Python.  So we wanted to create a site that could
be easily understood by Python developers.

## Mkdocs vs. Docusaurus

There are two main tools used by Python developers
to write documentation: [Mkdocs](http://mkdocs.org)
and [Docusaurus](https://docusaurus.io/).  Mkdocs
is easier to use and more popular than Docusaurus.
Docusaurus is also optimized for single-page applications.
Mkdocs also has an extensive library of themes and plugins.
None of us are experts in JavaScript or React.
Based on our [ChatGPT Analysis of the Tradeoffs](https://chat.openai.com/share/c7fea52c-3ef2-4837-a70a-fc9bdb919d9a)
we chose mkdocs for this site management.

## GitHub and GitHub Pages

[GitHub](http://github.com) is a logical choice to store our 
site source code and documentation.  GitHub also has
a [Custom GitHub Action](https://github.com/marketplace/actions/deploy-mkdocs)
that does auto-deployment if any files on the site change.
We don't currently have this action enabled, but other
teams can use this feature if they don't have the ability
to do a local build with mkdocs.

GitHub also has [Issues](https://github.com/dmccreary/microsims/issues), 
[Projects](https://github.com/users/dmccreary/projects/2) and releases
that we can use to manage our bugs and tasks.

The best practice for low-cost websites that have public-only
content is [GitHub Pages](https://pages.github.com/).  
Mkdocs has a command (```mkdocs gh-deploy```) that does
deployment directly to GitHub Pages.  This was an easy choice to make.

### GitHub Clone

If you would like to clone this repository, here are the commands:

```sh
mkdir projects
cd projects
git clone https://github.com/dmccreary/microsims
```

### After Changes

After you make local changes you must do the following:

```sh
# add the new files to a a local commit transaction
git add FILES
# Execute the a local commit with a message about what and why you are doing the commit
git commit -m "comment"
# Update the central GitHub repository
git push
```

## Material Theme

We had several options when picking a mkdocs theme:

1. Mkdocs default
2. Readthedocs
3. Third-Party Themes [See Ranking](https://github.com/mkdocs/catalog#-theming)

The Material Theme had 16K stars.  No other theme had over a few hundred.
This was also an easy design decision.

One key criterial was the social Open Graph tags so that when our users
post a link to a simulation, the image of the simulation is included
in the link.  Since Material supported this, we used the Material theme.
You can see our [ChatGPT Design Decision Analysis](https://chat.openai.com/share/d152cc79-73eb-4112-8be2-f03459d7b312) if you want
to check our decision process.

## Conda vs VENV

There are two choices for virtual environments.  We can
use the native Python venv or use Conda.  venv is simle
but is only designed for pure Python projects.  We imagine
that this site could use JavaScript and other langauges
in the future, so we picked Conda. There is nothing
on this microsite that prevents you from using one or
the other.  See the [ChatGPT Analysis Here](https://chat.openai.com/share/f2a6a7e2-5b8d-4ec0-8755-4a06b4b574f6).

Here is the conda script that we ran to create a new mkdocs environment that also
supports the material social imaging libraries.

```sh
conda deactivate
conda create -n mkdocs python=3
conda activate mkdocs
pip install mkdocs "mkdocs-material[imaging]"
```

## Mkdocs Commands

There are three simple mkdoc commands we use.

### Local Build

```sh
mkdocs build
```

This builds your website in a folder called ```site```.  Use
this to test that the mkdocs.yml site is working and does not
have any errors.

### Run a Local Server

```sh
mkdocs serve
```

This runs a server on ```http://localhost:8000```.
Use this to test the display formatting locally
before you push your code up to the GitHub repo.


```sh
mkdoc gh-deploy
```

This pushes everything up to the GitHub Pages site.
Note that it does not commit your code to GitHub.

## Mkdocs Material Social Tags

We are using the [Material Social](https://squidfunk.github.io/mkdocs-material/setup/setting-up-social-cards/) tags.  This
is a work in progress!

Here is what we have learned.

1. There are extensive image processing libraries that can't be installed with just pip.  You will need to run a tool like [brew](https://brew.sh/) on the Mac to get the libraries installed.
2. Even after ```brew``` installs the libraries, you have to get your environment to find the libraries.  The only way I could get that to work was to set up a local UNIX environment variable.

Here is the brew command that I ran:

```sh
brew install cairo freetype libffi libjpeg libpng zlib
```

I then had to add the following to my ~/.zshrc file:

```sh
export DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib
```

Note that I am running on a Mac with Apple silicon.  This means that the
image libraries that brew downloads must be specific to the Mac Arm
instruction set.

* [Cover images for blog post #4364](https://github.com/squidfunk/mkdocs-material/issues/4364)
* [Discussion on overriding the Social Card Image](https://github.com/squidfunk/mkdocs-material/discussions/5162)