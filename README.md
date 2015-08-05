# hrlnt 
**hrlnt** creates metal lyrics from dante's inferno, and tourettes some cool heaviness.

Several years ago I was making a gibbering, fanboy pest of my self to Ian Christie: https://en.wikipedia.org/wiki/Sound_of_the_Beast. I'm not a big metal fan, so I was a total ignoramus about anything south of Mötorhead. Christie's chapters on the weird church-burning crazoids involved in the Black Metal scene were so compelling, and the quoted lyrics so absolutely nuts that I thought "hey, I'll make him a toy death metal lyrics generator". I kind of did, but it was weak, and his site was in PHP and I'm a python bigot, so . . .

A couple of years later one of my co-workers turned me on to heroku, I wanted to learn some of the basics, and I still had the code for the stupid thing on a backup drive. Cue the Six Million Dollar Man theme. I cleaned some stuff up, changed the name to something web 2.9.b3 and now you can play random metal mad-libs, too. 

This is too lame, and I am too cheap, for an actual domain:

https://very-metal.herokuapp.com/

The API is publicly accessable, I'm sure you'll want to use it, I mean, who wouldn't?

## setup
### local
1. Clone this repository.
1. Set up virtualenv as discussed here: https://devcenter.heroku.com/articles/getting-started-with-python-o#start-flask-app-inside-a-virtualenv
1. Start virtual environment and install requirements
```bash
$ source venv/bin/activate
(venv)$ pip install -r requirements.txt

```

### heroku
1. Clone this repository.
1. Set up virtualenv and push to an heroku project as discussed here: https://devcenter.heroku.com/articles/getting-started-with-python-o#start-flask-app-inside-a-virtualenv
1. (optional) Dude, pick a brutal name when doing heroku add
```bash
$ heroku add ostimoticles-of-mephistopheles
$ git push heroku master 
$ heroku ps:scale web=1
$ heroku ps
$ heroku open
```
## api
You have to have one, right? It's all GET. Load it all with js. Switch out the textfiles with Ayn Rand novels (you won't even need to change the image backgrounds).
- /api/json
- /api/xml
- /api/html # pre-configured with the classes: "brutal song", "blood_drenched_verses", "metallic_verse", and "evil_line". The lines are paragraphs, which kind of sucks.

## configuration
metalconfig.py loads a lyrics source and a source of BRUTAL EPITHETS, which serve as titles for the songs and awesome end-of-stanza screamy bits. Alter the values in the SONG dictionary to change the number of lines and stanzas.

### inferno.txt
I downloaded Dante's Inferno from http://www.gutenberg.org/cache/epub/8800/pg8800.txt. 

To make it work, I stripped out all the headers, blank lines and punctuation. It's more utterly brutal that way.

### epithets.txt
A list of brutal, brutal epithets. ALL CAPS. One per line.
