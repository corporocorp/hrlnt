# -*- coding: utf-8 -*-
import datetime
import uuid
import random
import json
from io import BytesIO
import xml.etree.ElementTree as ET
from flask import Flask, render_template, make_response, request, url_for, g
from flask.ext import restful
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.from_object("metalconfig")
api = restful.Api(app)

class JSong(object):
    """
    base class for producing the various song objects.
    """

    def epithet(self):
        """get a random line from EPITHETS in config and return"""
        idx = random.randint(0, len(app.config["EPITHETS"])-1)
        return app.config["EPITHETS"][idx]

    def line(self):
        """grab a random line of dante's inferno
        return it as brutal text"""
        idx = random.randint(0, len(app.config["INFERNO"])-1)
        return app.config["INFERNO"][idx]

    def stanza(self):
        """assemble line() strings into a stanza
        add a couple of epithets for verisimilitude
        return list"""
        stanza = []
        for i in range(app.config["SONG"]["lines"]):
            stanza.append(self.line())
        stanza += [self.epithet(), self.epithet()]
        return stanza

    def song(self):
        """Assemble stanza() lists into a song object"""
        song = {
                "title": self.epithet(),
                "verses": []
                }
        for i in range(app.config["SONG"]["stanzas"]):
            song["verses"].append(self.stanza())
        return song

class XMHell(JSong):
    """
    Build XML song.
    """
    def song(self):
        """Assemble stanza() lists into an xml song object"""
        song = ET.Element("song")
        title = ET.SubElement(song, "title")
        title.text = self.epithet()
        verses = ET.SubElement(song, "verses")
        for i in range(app.config["SONG"]["stanzas"]):
            verse = ET.SubElement(verses, "stanza")
            for s in self.stanza():
                line = ET.SubElement(verse, "line")
                line.text = s 
        tree = ET.ElementTree(song)
        f = BytesIO()
        tree.write(f, encoding="utf-8", xml_declaration=True)
        return f.getvalue()

class HTMHell(JSong):
    """
    Build song in HTML format with hard-coded classes, because I'm a lazy, lazy,
    lazy man.
    """
    def song(self):
        """Assemble stanza() lists into an xml song object"""
        song = ET.Element("div")
        song.attrib["class"] = "brutal_song"
        title = ET.SubElement(song, "h1")
        title.text = self.epithet()
        verses = ET.SubElement(song, "div")
        verses.attrib["class"] = "blood_drenched_verses"
        for i in range(app.config["SONG"]["stanzas"]):
            verse = ET.SubElement(verses, "div")
            verse.attrib["class"] = "metallic_verse"
            for s in self.stanza():
                line = ET.SubElement(verse, "p")
                line.attrib["class"] = "evil_line"
                line.text = s 
        tree = ET.ElementTree(song)
        f = BytesIO()
        tree.write(f, encoding="utf-8")
        return f.getvalue()

class Natas(restful.Resource):
    """Fucking backwards-masking man!"""

    def get(self):
        song = JSong()
        return song.song(), 200
 
class Flies(restful.Resource):
    """Lord of, The"""

    def get(self):
        """
        Note that we have to use make_response to output the correct
        content-type of application/xml, since flask-restful defaults
        to json.
        """
        song = XMHell()
        response = make_response(song.song())
        response.headers["content-type"] = "application/xml"
        return response

class Satin(restful.Resource):
    """It ain't evil if it's spelled right"""

    def get(self):
        """
        Same as the get in Flies, only outputting text/html
        """
        song = HTMHell()
        response = make_response(song.song())
        response.headers["content-type"] = "text/html"
        return response 

# paths to api calls
api.add_resource(Natas, "/api/json")
api.add_resource(Flies, "/api/xml")
api.add_resource(Satin, "/api/html")

@app.route("/")
def index():
    song = HTMHell()
    g.song = song.song()
    return render_template("index.html")

# this template uses jquery to access the html api
@app.route("/fromapi")
def fromapi():
    return render_template("fromapi.html")
