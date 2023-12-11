# Emag-Scraping
The app takes an URL for the wanted product from Emag, a value below which the user will get notified if the price drops and a email address for the notification to be sent to.

Using Beutiful Soup and the URL provided by the user, the app gets the price of the item, checks if the price is lower than the specified value, if so using SMTPlib it sends a notification
via email, the sensible data is hidend using .env and os
![Image 11 12 2023 at 05 30](https://github.com/gabrielsorin88/Emag-Scraping/assets/126314730/f2df27fd-7f2e-479e-a51d-99a9cc697100)
![Image 11 12 2023 at 05 30](https://github.com/gabrielsorin88/Emag-Scraping/assets/126314730/6599ee05-faf0-4711-8d21-7a2c9c1df3c4)
![Image 11 12 2023 at 05 28](https://github.com/gabrielsorin88/Emag-Scraping/assets/126314730/c8c79407-6486-4fca-926f-f9486acf2f24)

