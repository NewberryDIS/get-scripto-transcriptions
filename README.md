# get-scripto-transcriptions

This Python script is meant to be used as an extension to Omeka's [Scripto transcription plugin](https://github.com/omeka/plugin-Scripto), exporting all current transcriptions from a project into a machine-readable and legible JSON data file. 

The script takes as an argument a full link to an Omeka Scripto project with no trailing slash, like so:

`python get_scripto_transcriptions.py http://publications.newberry.org/transcription/mms-transcribe`

For the script to work, the API has to be enabled for the project. This can be done by Super Users from the settings tab in the Omeka admin interface.

All transcriptions will be grouped at the item level and be saved into a file named 'alltranscripts.json'.
