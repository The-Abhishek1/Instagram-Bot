from instabot import Bot 
bot =Bot()
bot.login(username="YouruserName" password="YourPassword")

bot.upload_photo("/Alone.png",caption="Just be Crazy")

bot.follow("Virat Kohli")

bot.send_message("Hiii from Abhishek",['creative17','the_wonder'])

followers=bot.get_user_follower("elonmusk")
for follower in followers:
  print(bot.get_user_info(follower))

bot.unfollow_everyone()

