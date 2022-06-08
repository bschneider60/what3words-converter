# what3words-converter
Use what3words to get a set of GPS coordinates and convert the format of the location

[what3words](https://what3words.com/clip.apples.leap) is a mapping program that assigns a three-word phrase to every 3mx3m square on Earth. These phrases are easier to rememeber than GPS coordinates and are useful for locations where street addresses don't exist, like parks or parking lots.

This Python script prompts the user for three words, and uses the [what3words API](https://developer.what3words.com/public-api/docs#overview) to return the coordinates of that location. The API uses the decimal degrees format, so this script also converts and displays the output to decimal minutes and decimal seconds as well.

This program requires users to have a [what3words account](https://what3words.com/select-plan?referrer=/public-api&currency=USD) to be able to use the API.
