import vlc

    
# media object
media = vlc.Media('/media/songs/19.mp3')
  
# setting media to the media player
media_player.set_media(media)
media_player = vlc.MediaPlayer()
media_player.set_media(media)

# Play to open/load the video
media_player.play()

# Pause the Video
media_player.pause()

# Other Stuff Happens

time.sleep(init_delay)
media_player.play()