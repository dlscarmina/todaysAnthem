# Today's Anthem

## Inspiration
Sometimes, you want a song that knows exactly how you feel. Sometimes, you want a song to tell you how to feel. This app does just that!

## What it does
**Today's Anthem** is a music recommendation app which chooses a theme song for their day. It's a simple, easy to use single-page web application that surveys the user's genre preference, mood, and energy level. The responses compare with Spotify's music database and searches for the perfect song, and plays it! If the user isn't content with their match, they can request another one!

## How we built it
With the user input and [_Spotify's API_](https://developer.spotify.com/documentation/web-api/reference/browse/get-recommendations/), we utilized the following _Tuneable Track attributes_: valence, energy, and genre. Valence describes musical positiveness; the higher the valence, the happier the song! Energy describes how fast, loud, and noisy a track is; so, you won't be seeing any Lo-Fi Hip Hop in there if you maxed out the energy bar! The generator picks 10 songs, so the user is allowed to "re-roll" their selection if they aren't satisfied.

For the front end, we used _Bootstrap_ and _jQuery_; for the back end, we used _Flask_ and _Jinja_.

## Accomplishments that we're proud of
This was a really awesome and unique experience for all four of us!
- **Josh:** Learning about the Flask framework.
- **Mitchell:** Building a Flask app without any prior knowledge.
- **Hazel:** Learning about a ton of stuff I never knew about, like front end web development.
- **Mina:** Surviving my first hackathon and sticking with the first idea that came to me.

## What's next for Today's Anthem
**Tomorrow's Anthem** builds more music recommendations off of more pin points. There are so many _Tuneable Track attributes_ that we didn't utilize, and there are so many other ways we can track them! This will make our song generation more accurate and catered to the user.
We also want to implement a feature that reads the computer's calendar date and, if it is April 1st, the assets turn derpy.

**Frameworks:** Bootstrap, jQuery, Flask

**Contributors:** Hazel, Josh, Mina, Mitchell
