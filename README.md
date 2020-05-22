# TwitchBot
A twitch bot for Scrabble stuff

Files you need on your local version:

  -csw.dat:
    this is the dictionary file, plain text, each word on one line following this example:
      
      AA	(Hawaiian) a volcanic rock consisting of angular blocks of lava with a very rough surface [n -S]	bcfm	hls	46	AA
      
      word (tab \t) definition (tab \t) front_hooks (tab \t) back_hooks (tab \t) probability (tab \t) alphagram
      
  -config.dat
    this is the configuration file to connect the bot to a twitch account and have it join channels, it has the following 4 lines only (made up info) instructions on how to set up your own bot found below:
    
      oauth:2cw2mrjef8fd8fdoyd95fbi2ajnwpvy1
      oe08ff8dfds8fdfjd99fda68g6pt
      BotsTwitchAccountName
      somestreamer, anotherstreamer , athirdstreamer
      
    
Setting up your own bot (you can run TwitchBot.py, or if you don't have python or just want to run the exe that works too):

  1. Create a new twitch account with the username you want the bot to have

  2. Go to https://twitchapps.com/tmi/ and click Connect, copy what is in the text box including "oauth:"

  3. Sign in as that account and go here: https://dev.twitch.tv/console/apps/create

  4. Register a new application, Name is not important, it isn't shown anywhere except in your applications list

  5. Paste the oauth you got earlier, you'll also need to put this into config.dat (just open in notepad or similar)

  6. Choose Chat Bot for Category

  7. Click Create

  8. You will be brough to a page called Console, where you will see your App, click on Manage

  9. Copy your Client ID, you will need to put this in config.dat

  10. Open config.dat and replace the lines with your information:
	  first line is the oauth
	  second line is your client id
	  third line is your bot's username
	  fourth line is the channels you want it to join separated 	by commas

  11. Save this file

  12. That's it, run TwitchBot.exe and it should connect and show a message saying "it is online"
  

Commands for the bot
