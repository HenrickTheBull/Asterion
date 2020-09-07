#################################
# 
#  Initilization File for Asterion Discord Bot
#  Written by: Bryant Stafford
#  Email: bryant.stafford@outlook.com
#  Discord: HenrickTheBull#1102
#  
#  🌟🐂
#################################

# Init the bot from the __init__.py file in the sky directory. 

from sky import get_bot

if __name__ == "__main__":
    bot = get_bot()
    bot.log.info(f"Initilization Completed in {bot.time.round_time()} seconds.")
    bot.run()