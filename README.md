# mycroft-youtube
A skill to play youtube videos. It searches youtube for what you say to it, then
it plays the first thing it finds in the results. 

The python figures out the URL, then uses the external yt\_player.sh file to pipe 
youtube-dl into mplayer to play the content. The plus side of this approach is
that we never leave any files behind. The downside is that this makes the script
incredibly dumb. It can only start/stop videos and not control the tracking.

In the future, this skill may be expanded to be able to queue up songs or even handle
playlists, but for now, it just trys to play the video you ask it to play.

Special thanks to [JarbasAI](https://github.com/augustnmonteiro) for providing the
[search utility](https://github.com/HelloChatterbox/youtube_searcher) for this project.
Were it not for them, the project would have likely been archived.

# Requirements 
* mpv player

# Install Using [MSM (Mycroft Skill Manager)](https://github.com/MycroftAI/mycroft-skills-manager)
    sudo msm install https://github.com/hexeratops/mycroft-youtube-skill

# Install Manualy
    sudo apt-get install mplayer
    sudo mkdir -p /opt/mycroft/skills
    cd /opt/mycroft/skills 
    sudo git clone https://github.com/hexeratops/mycroft-youtube-skill 
    pip install -r requirements.txt 
     

# Using
* Say `youtube John Denver`
* Say `youtube Rocky Mountain High`
* Say `youtube search for Im a believer by the Monkeys`
