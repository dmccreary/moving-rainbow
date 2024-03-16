# How We Built This Site

This page describes how we built this website and some of 
the rationale behind why we made various design choices.

## Basic Requirements

1. Hosting the site must be free using [GitHub Pages](glossary.md/#github-pages)
2. We need to document the Python sample code
3. We want professional-quality code highlighting
4. We wanted the site to have a strong search function
5. We wanted to make it easy to generate the HTML from easy-to-edit [Markdown](./glossary.md#markdown) files
6. We wanted to make it easy for an instructor to copy the link from any section of any lesson plan directly into a Zoom/Chat window so students can just click on the link to get the right lesson.  This is called [Deep Linking](./glossary.md#deep-linking)
7. We wanted to make it easy to build user interfaces that are consistent with our other projects including:
    1. [Beginning Python](https://www.coderdojotc.org/python/trinket/00-introduction/)
    2. [Beginning Electronics](https://dmccreary.github.io/beginning-electronics/)
    2. [MicroPython for Kids](https://www.coderdojotc.org/micropython/)
    3. [Robot Faces](https://dmccreary.github.io/robot-faces/)
    4. [Clocks and Watches](https://dmccreary.github.io/micropython-clocks-and-watches/)
    5. [Robot Day](https://dmccreary.github.io/robot-day/)
    6. [STEM Robots](https://dmccreary.github.io/stem-robots/)
    7. [MicroSims for Education](https://dmccreary.github.io/microsims/)
    10. [Digital Electronics](https://dmccreary.github.io/digital-electronics/)
8. We wanted to make it easy for other schools and organizations to
just "fork" this repository to put their own school logo and colors
on the site.
9. We wanted to leverage existing GitHub tools for reporting bugs, organizing projects and tasks and automating the build process.
10. We wanted to make sure we would support consistent build and release management so we could add new features without disrupting existing sites. (branches, tagging and release).


## Why Python Mkdocs

The goal of this site is to teach computational thinking 
in the coolest hands-on way we can think of.
We also do this by using AI to help us find the lowest-cost parts.

We also leverage open-source MicroPython, and it is natural
to want to use a website builder that also uses Python.  
Python is language of data science and AI.  So we wanted to create a site that could be familiar to Python developers.

But we also wanted to make it easy for non-programmers to update
the site.  Let's review some of these design decisions and
explain how you can "fork" this site (duplicate it) and put your school or organization's brand and logo on the pages

We will also touch a little bit on how we are using Google
Analytics to track site usage and how this can be added
with just a few new lines in the configuration file for this
site.

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