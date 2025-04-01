# CoderDojo Content Authoring Guide
When our CoderDojo clubs were just getting started we struggled to find high-quality content that was age appropriate for our students.  We learned of the CoderDojo international foundation used simple laminated [Concept Cards](../glossary.md#concept-cards)

## Our Current CoderDojoTC Content Publishing Stack

### Markdown
We use [Markdown](https://en.wikipedia.org/wiki/Markdown) for all our content.  A good way to learn Markdown is to use a [Markdown cheat sheet](https://www.markdownguide.org/cheat-sheet/).  We want you to put many images into your classes so make sure to use the image links!

### GitHub for Source
We use [GitHub](https://github.com/) to store our content.  GitHub is free for all public content and has many advanced features that allow team to work together to build and test learning content.  Many of our
content authors are familiar with GitHub.

### GitHub Pages for Web Sites
We use [GitHub Pages](https://pages.github.com/) to publish our content to microsites.  Each coding group has their own microsite and search does not currently work across the microsites (we are working on fixing this). All content should be published into a gh-deploy branch.  If you change content using the web-based editor (the pencil in the upper right
corner of the github page viewer - you may need to have a friend help republish the content to the GitHub Pages site.)

### MkDocs for Publishing
We use [mkdocs](https://www.mkdocs.org/) for our publishing tool.  This converts our Markdown pages into HTML web sites.  To deploy mkdocs you will need to have python installed on your local computer.  You must run the "mkdocs gh-deploy" command every time you make changes.

### Google Material User Interface Components
We use the [mkdocs material theme](https://squidfunk.github.io/mkdocs-material/).  We encourage you to learn to add custom material widgets to your content.

### CoderDojo Style Guide
We use [CoderDojo style guide](https://company-51033.frontify.com/d/E6KNDhunr9mR/coderdojo-style-guide-1460385526) for our colors, icons and fonts.  Please try to stay close to these guidelines so that mentors, parents, and students
all know they are on a kid-safe site.

We like our lesson plans to start with an image, gif or short video clip (under 10-seconds).

## Setting Up a Virtual Environment with Conda

This section is for programmers that are setting up "build" systems on their desktops to automate the mkdocs publishing process.  If you are new to Python and Conda virtual environments, please ask for help!  This is not as easy is it looks, especially on Windows systems.

First, follow the installation instruction on the Conda web site:

[Conda Virtual Environment Shell Installation](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

```
$ conda create --name  mkdocs python=3.6
$ conda activate mkdocs
$ pip install mkdocs
$ pip install mkdocs-material
```

If you are also installing quizzes on your microsite you will need additional steps not included here.

## Add the site dir to your .gitignore
The mkdocs process takes Markdown files and converts them to HTML.  These files are put into a folder called ```site```.  However, to publish we push this folder to the ```gh-deploy``` branch.  To keep the site directory from being pushed to the main branch we need to add the directory to the .gitignore file:

Contents of .gitignore
```
site
.DS_Store
~$*
```

Try to avoid links to resources that are not kid-safe.

By using these standards it will enable us to reuse this content for search, recommendation and building tools that allow students to use chatbots to help them code.

## Images
All images should be stored in the doc/img directory in your site.  Please keep images reasonably small (under 50K) to keep the load times fast.

## Navigation
Make sure when you add a new content file you link it into the navigation menu.  Try to keep navigation lists under 30 items.  Try using nesting if your lists get too long.

## Mkdocs commands
There are only four mkdocs commands.  You will rarely need to use the new command.

#### **mkdocs build**
Build the MkDocs documentation.  We use this to test at the nav pages all match a document.
If you get error messages in the build process you work on fixing them until the build
does not return any errors.

#### **mkdocs gh-deploy**
Deploy your documentation to GitHub Pages.  Run this when you want to take your local changes and push them to the web site.

Here is an example of this run:

```sh
$ mkdocs gh-deploy
INFO    -  Cleaning site directory 
INFO    -  Building documentation to directory: /Users/dmccrea1/Documents/ws/CoderDojoTC/site 
INFO    -  Documentation built in 0.90 seconds 
INFO    -  Copying '/Users/dmccrea1/Documents/ws/CoderDojoTC/site' to 'gh-pages' branch and pushing to GitHub. 
INFO    -  Your documentation should shortly be available at: [https://CoderDojoTC.github.io/CoderDojoTC](https://CoderDojoTC.github.io/CoderDojoTC)
```

#### **mkdocs new**
Create a new MkDocs project.  Most of our mentors will not need to do this.  We will supply you with a template zip file with all the right content if you need to create a new CoderDojo microsite of your own.

#### **mkdocs serve**
Run the builtin development server and display the web site on your local computer.  This is a great way to quickly check your changes since the server watches for any file changes and immediately updates the web page.

### Material examples

We chose the Google Material theme because there are tens of thousands of components you can add to your pages.  You can get a sample of them here:

[Material Components](https://material.io/components) 

## Embedding Videos

We strongly encourage some movement in short 10-second demos using videos.

To embed a YouTube video do the following

1. Use the Share button
2. Select the **Embed** option
3. Copy the iFrame code and paste it into your MarkDown
4. Add the ```?rel=0``` link which will only put your own related videos on the More Video when the video is done playing.

See [YouTube Embed Option for Related Videos Changes](https://cornertab.com/youtube-embed-option-related-videos-changes/
) for details.
