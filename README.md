aaconvert
=========

The aaconvert tool lets you convert images to ASCII art, using the
[aalib](http://aa-project.sourceforge.net/) package. Since aalib for Python
comes with lots of dependencies, a Dockerfile is provided for running the
script inside a [Docker](https://www.docker.com/) container.

Here's how you build the image (you may need root privileges depending
on your Docker setup):

    $ docker build -t aaconvert .

Once the image is build, you can call the converter like so:

    $ docker run --rm aaconvert http://google.com/favicon.ico

Running the container without a URL gives you a help screen with available
command line options.
