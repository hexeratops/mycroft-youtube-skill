# -*- coding: utf-8 -*-

# Used for calling the external youtube player script
import subprocess
import signal
import os

# Used for calling the youtube search API
from youtube_searcher import search_youtube

# Standard skill behaviour
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
#from mycroft.skills.core import MycroftSkill, IntentBuilder, intent_handler
from mycroft.audio import wait_while_speaking

__author__ = 'hexeratops'



class YoutubeSkill(MycroftSkill):
    def __init__(self):
        super(YoutubeSkill, self).__init__(name="YoutubeSkill")
        self.process = None
        self.ytp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "yt_player.sh")

    def search(self, text):
        """Search youtube for a subject and return a search ID.

        Arguments:
        text -- the subject to search for.

        Returns:
        The youtube video ID on success or None upon failure.
        """
        try:
            results = search_youtube(text)
            if 'videos' in results and len(results['videos']) > 0:
                result = results['videos'][0]
                id = result['url'].split('v=')[1].split('&')[0]
                title = result['title']
                return [id, title]
        except:
            pass

        return None

    @intent_handler(IntentBuilder("").require("YoutubeKeyword").require("YoutubeSubject"))
    def youtube(self, message):
        """Responds to the youtube keyword"""
        self.stop()
        subject = message.data.get('YoutubeSubject').lower()

        self.speak_dialog("lookup", {"query": subject})
        vid = self.search(subject)

        if vid is None:
            self.speak_dialog("no video found", {"query": subject})
        else:
            # Start the process, then display the title of the video
            self.process = subprocess.Popen([self.ytp, vid[0]], preexec_fn=os.setsid)
            wait_while_speaking()
            self.enclosure.mouth_text(vid[1])
            self.process.wait()

            # Upon completion or the task being killed, perform cleanup
            self.process = None
            self.enclosure.reset()

    def stop(self):
        if self.process:
            try:
                os.killpg(os.getpgid(self.process.pid), signal.SIGINT)
            except Exception as e:
                self.speak(str(e))


def create_skill():
    return YoutubeSkill()
