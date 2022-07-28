import twint.run
from twint import Config

config = Config()
config.User_id = "narendramodi"
config.Search = True

twint.run.Search(config)

#  https://twitter.com/i/api/graphql/Bhlf1dYJ3bYCKmLfeEQ31A/UserByScreenName?variables=%7B%22screen_name%22%3A%20%22narendramodi%22%2C%20%22withSafetyModeUserFields%22%3A%20false%2C%20%22withSuperFollowsUserFields%22%3A%20false%7D
#  https://twitter.com/i/api/graphql/Bhlf1dYJ3bYCKmLfeEQ31A/UserByScreenName?variables=%7B%22screen_name%22%3A%20%22narendramodi%22%2C%20%22withSafetyModeUserFields%22%3A%20false%2C%20%22withSuperFollowsUserFields%22%3A%20false%7D