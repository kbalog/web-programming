# Assignment 8 - Booking site

This exercise builds on [Assignment 3](../assignment-3) from before. The static booking prototype will now be developed into a dynamic site using Flask and MySQL.

You can work with your submission from before or can also choose to work with the reference solution; the reference solution can be downloaded from the [solutions repository](https://github.com/uis-dat310-spring2018/solutions/tree/master/assignment-3).

  *	Use templates instead of static HTML pages
    - Pages should share the same "HTML frame" (i.e., the `<html>`, `<head>`, `<body>` elements should be present only in a single template file `layout.html`)
  *	Create a table for storing property information
    - Store property identifier (as auto increment field), name, location, description, details, and photo (filename)
    -	Add at least 6 different properties to the table
  * Load properties from the database when listing them on the index page. When the "Details" button is clicked, show the details of the selected property on the property page.
  *	Implement the booking process, which consists of three steps
    1. Display the property page where the user can select the check-in date and the number of nights
        - Alternatively, check-out date may also be selected instead of the number of nights
    2. Providing user details.
        - At the top of the page, show the check-in and check-out dates (either as text or as readonly input fields).
        - A form for providing contact details: name, email, telephone, and billing address (postcode, city, street) are obligatory fields. It's not possible to go to the next step unless these are provided. Additionally, the user may provide comments in a textarea field (it may be empty). You application should "remember" the values the user already filled in (i.e., in case there is an error, only the missing parts need to be completed, the rest of the values are remembered).
    3. Display a confirmation page, listing the property and user details. The user must tick a checkbox saying she accepts the "Terms and Conditions".
        - "Terms and Conditions" should be a link that opens in a new browser window. Make a page with some dummy content.
  * Upon confirmation of the booking, store it in a database and display a confirmation number.
    - You can assign any confirmation number as long as it uniquely identifies the order.

The skeleton of the solution is provided, which implements the main program logic.

Commit and push files to GitHub.

You also need to submit a dump of your database in a single file called `database.sql`.  Executing this file should create all the tables that are needed for your application and should insert property data.


# Øving 8 - Booking side

Denne oppgaven bygger videre på [Øving 3](../assignment-3) fra tidligere. Den statiske booking-prototypen skal nå utvikles til en dynamisk side, ved bruk av Flask og MySQL.

Du kan bygge videre på dine egne filer du har fra den tidligere innleveringen, eventuelt kan du bruke filene fra løsningsforslaget. Løsningsforslaget kan lastes ned fra [solutions repository](https://github.com/uis-dat310-spring2018/solutions/tree/master/assignment-3)

  * Bruk maler (templates) istedenfor statiske HTML sider
    - Sider skal dele samme "HTML ramme" (`<html>`, `<head>`, `<body>` elementene skal bare være å finne i én mal-fil (template file) `layout.html`)
  * Lag en MySQL-tabell for lagring av eiendom (property) informasjon
    - Lagre eiendomidentifikator (som auto increment felt), navn, sted, beskrivelser, detaljer, og bilde (filnavn)
    - Legg inn minst 6 eiendommer i tabellen
  * Last inn eiendom fra database når du viser dem på index-siden. Når "Details" knappen klikkes, vis detaljene for den valgte eiendom på eiendommen (property) siden.

** Translation in progress ... **


Du er gitt grunnkoden, som implementerer hovedfunksjonene til programmet som du ikke trenger å tenke på.

Last opp til GitHub (commit og push).

Du må også lage en dump av databasen i en enkelt fil som heter `database.sql`. Utfører denne filen skal lage alle tabellene som er nødvendig for din applikasjon og skal sette inn eiendom (property) data.
