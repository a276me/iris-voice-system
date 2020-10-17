# Intelligent Recognition Integrated System (I.R.I.S)
### Inspired by Tony Stark's Jarvis system

## Quick Start
To start Iris, run main.py.
remember to record a noise file for noise reduction, or else iris may be unable to recognize your voice
currently only supports english.
Uses Baidu API for voice recognition
## Writing an iris app
To write an app, go to apps.py and append to the "routes" list.
``` python
{'name': 'your app name', 'main': function_to_start_your_app, 'keys': [a list of key words that will activate your app]},
```
## Development Process
Still working on GUI  
Working on a Tensorflow audio recognition model  
### !Anyone is welcome to commit!
