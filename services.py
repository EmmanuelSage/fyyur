from models import *

def get_venues():
  result = []
  
  # get all venues
  venues = Venue.query.all()

  # Use set so there are no duplicate venues
  locations = set()

  for venue in venues:
      # add city/state tuples
    locations.add((venue.city, venue.state))

  # for each unique city/state, add venues
  for location in locations:
    result.append({
        "city": location[0],
        "state": location[1],
        "venues": []
    })

  for venue in venues:
    num_upcoming_shows = 0

    shows = Show.query.filter_by(venue_id=venue.id).all()

    # get current date to filter num_upcoming_shows
    current_date = datetime.now()

    for show in shows:
      if show.start_time > current_date:
          num_upcoming_shows += 1

    for venue_location in result:
      if venue.state == venue_location['state'] and venue.city == venue_location['city']:
        venue_location['venues'].append({
            "id": venue.id,
            "name": venue.name,
            "num_upcoming_shows": num_upcoming_shows
        })
  
  return result
