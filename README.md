# hrlnt 
Several years ago I was making a pest of my self to Ian Christie https://en.wikipedia.org/wiki/Sound_of_the_Beast. I'm not a big metal fan, so I was a total ignoramus. His chapters on the weird church-burning crazoids involved in the Black Metal scene was so compelling, and the quoted lyrics so absolutely nuts that I thought "hey, I'll make him a toy death metal lyrics generator". I kind of did, but it was weak, and his site was in PHP, so . . .

A couple of years later one of my cow-orkers turned me on to heroku, I wanted to learn some of the basics, and I still had the code on a backup drive. Cue the Six Million Dollar Man theme. I cleaned some stuff up, changed the name to something web 2.9.b3 and now you can play random metal mad-libs, too. 

**hrlnt** creates metal lyrics from dante's inferno, and tourettes some cool heaviness from epthitets.txt.

This is too lame, and I am too cheap for an actual domain:

https://very-metal.herokuapp.com/

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
- /api/xml
- /api/json
- /api/html

## configuration
metalconfig.py loads a lyrics source and a source of BRUTAL EPITHETS, which serve as titles for the songs and awesome end-of-stanza screamy bits. Alter the values in the SONG dictionary to change the number of lines and stanzas.

### inferno.txt
I downloaded Dante's Inferno from http://www.gutenberg.org/cache/epub/8800/pg8800.txt. 

To make it work, I stripped out all the headers and punctuation. It's more brutal that way.

### epithets.txt
A list of brutal, brutal epithets. ALL CAPS. One per line.
