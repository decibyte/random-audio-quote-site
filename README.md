# Random Audio Quote Site

_All you need to serve a small website letting your visitors play a random MP3 from your fine collection of audio quotes._

There are only a few things to note about this package:

## 1. The `audio` directory

This is where you should collect your audio quotes. Look at the README in the directory for further instructions.

## 2. The `preprocess.py` Python script

Which is used to:

 * Run through your collected quotes and compile a `library.json` file with information about your audio quotes.
 * Prepare an `index.html` file for you, ready to serve, that will let your visitors play random audio quotes.

Simply run the Python script, and you'll be ready in a few seconds. It will ask you for the name of your audio quote site (protip -- you can specify the name as a first argument to the script), and then prepare everything for you.

Serving the website requires nothing but a webserver capable of serving static files. Just point your webserver to root of the project after running `preprocess.py` and you're ready to go viral!

Did you collect new audio quotes that you want to add to the library? Lucky you! Just copy them to the audio directory and re-run the preprocessing script to update the library used by the website.
