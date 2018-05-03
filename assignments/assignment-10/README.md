# Assignment 10 - Booking admin

## Task

Your task is to develop an admin back-end for the booking site using a combination of technologies (Flask, MySQL, Bootstrap).

There are no starter files provided for this assignment.
You need to use Flask with templating, Bootstrap, and MySQL for implementing the functionality below. It is allowed to use any external Python package/module and Bootstrap component, plugin, or add-on.  A list of resources can be found at the bottom of the task description.

  * Login
    - All the functionality described below should be available only to logged in admin users. Login is based on a username and password combination.
    - There is no need to implement front-end functionality for adding new admin users. But you need to add a test user to your database dump that we can use for testing, username: "test" password: "dat310#A10". You need to store passwords in a secure way in the database (i.e., no raw password strings). See [password salting](http://flask.pocoo.org/snippets/54/).
  * Property management
    - The user needs to be able to list, add, delete, and edit properties.
    - On the property edit/add form, check that
        - Property name, location, and description are not empty
        - Photo is provided
    - If an error appears, then show an alert and remember the form values already filled in.
    - Note that it is part of the task to be able to modify property photos. New properties can only uploaded if a photo is provided.
  * Booking management
    - The admin user can list all the bookings that have been made.
    - Upon clicking on an booking, show the booking details, with a link to the booked property's page.
    - Your database should contain at least 20 bookings (You can generate "fake bookings" with a script.)
  * Statistics
    - Provide a plot which shows the number of bookings over some period of time (e.g., the number of bookings for each day).
    - Provide a list of the "most popular properties", i.e., properties that have been booked the most. Show the property ID, name, location, and the total order number of bookings for that property.
  * General
    - When listing properties or bookings, show at most 10 items on a page and let the user paginate between pages.
    - All forms and alert/success messages must also be styled using Bootstrap.

It is up to you how you organize this functionality on the admin user interface (i.e., what menu points you have, etc.). Some example screenshots for a similar task are made available in the Resources section.

Commit and push files to GitHub. You also need to submit a dump of your database in a single `database.sql` file.  Executing this file should create all the tables that are needed for your application and should insert property and booking data.


## Resources

  * Example screenshots from last year's (similar) assignment can be found under [screenshots](screenshots/).
  * A login example can be found [under the flask examples](/examples/python/flask/9_login).
  * A file upload example can be found [under the flask examples](/examples/python/flask/8_file_upload). See also the [Flask documentation](http://flask.pocoo.org/docs/0.12/patterns/fileuploads/).
  * For plotting, you may use a JavaScript library, e.g., [D3.js](https://d3js.org/), [Chart.js](http://www.chartjs.org/), [CanvasJS](http://canvasjs.com/), or [one of these libraries](https://www.sitepoint.com/15-best-javascript-charting-libraries/).
    - Some specific examples using [D3.js](http://bl.ocks.org/d3noob/8952219), [Chart.js](http://www.chartjs.org/docs/#line-chart-introduction), or [CanvasJS](http://canvasjs.com/html5-javascript-line-chart/).


# Øving 10 - Booking admin

## Oppgave

Din oppgave er å utvikle en admin back-end for booking-siden ved bruk av en kombinasjon av teknologier (Flask, MySQL, Bootstrap).

Det finnes ingen startfiler for denne oppgaven.
Du må bruke Flask for templating, Bootstrap og MySQL for implementering av funksjonaliteten beskrevet under. Det er tillat å bruke eksterne Python packages/modules og Bootstrap components, plugins eller add-ons. En liste av ressurser kan bli funnet på bunnen av oppgavebeskrivelsen.

  * Innlogging
    - All funksjonalitet beskrevet under skal bare være tilgjengelig for brukere logget inn som admin. Innlogging er basert på kombinasjon av brukernavn og passord.
    - Det er ikke nødvendig å implementere en front-end funsjonalitet for å legge til nye admin-brukere. Men du må legge til en testbruker i din databasedump som vi kan bruke til testing, bruker: "test", passord:"dat310#A10". Du må lagre passordet på en sikker måte i databasen (ergo, ingen raw passord streng).
  * Eiendomshåndtering
    - Brukeren må ha muligheten til å liste opp, legge til, slette og endre eiendommer.
    - På eiendommenes edit/add-form, sjekk at
        - Eiendomsnavn, lokasjon og beskrivelse ikke er tomt
        - Bilde er gitt
    - Hvis en feil oppstår skal det vises en alert og formverdiene som allerede er tastet inn skal huskes.
    - Vær oppmerksom på at det er en del av oppgaven å kunne modifisere eiendomsbildene. Nye eiendommer kan bare legges til hvis et bilde er gitt.
  * Bookinghåndtering
    - Admin-brukeren kan liste opp alle bookinger som er registrert.
    - Når man klikker inn på en booking skal det vises bookingdetaljer med link til eiendommens side.
    - Din database skal inneholde minst 20 bookinger (du kan generere "fake bookings" med et skript).
  * Statistikk
    - Gi et plott som viser antall bookinger over tid (f.eks. antall bookinger hver dag).
    - Gi en liste av de mest populære eiendommene, dvs. eiendommer det har blitt bestilt mest av. Vis eiendoms-id, navn, lokasjon og totalt antall bookinger av eiendommen.
  * Generelt
    - Når eiendommer eller bookinger listes opp, vis maks 10 elementer per side og la brukeren bla mellom sider.
    - Alle former og alert/success meldinger skal også styles ved hjelp av Bootstrap


Det er opp til deg hvordan du organiserer funksjonaliteten på admin-brukergrensesnittet (dvs. hvilke menypunkter du har med, etc.). Noen eksempler med skjermbilder for en liknende oppgave er gitt i Ressurs-seksjonen.

Commit og push filene til GitHub. Du må også submitte en dump av databasen din i en `database.sql` fil. Kjøring av denne filen skal lage alle nødvendige tabeller for å kunne bruke din applikasjon og den skal sette inn eiendom- og bookingdata.


## Ressurser

  * Skjermbilder fra fjorårets (liknende) oppgave kan bli funnet under [screenshots](screenshots/).
  * Et innloggingseksempel kan bli funnet [under flask-eksemplene](/examples/python/flask/9_login).
  * Et filopplastningseksempel kan bli funnet [under flask-eksemplene](/examples/python/flask/8_file_upload). Se også [dokumentasjon for Flask](http://flask.pocoo.org/docs/0.12/patterns/fileuploads/).
  * Du bruke et JavaScript bibliotek for plotting, f.eks., [D3.js](https://d3js.org/), [Chart.js](http://www.chartjs.org/), [CanvasJS](http://canvasjs.com/), eller [ett av disse bibliotekene](https://www.sitepoint.com/15-best-javascript-charting-libraries/).
    - Noen spesifikke eksempler ved bruk av [D3.js](http://bl.ocks.org/d3noob/8952219), [Chart.js](http://www.chartjs.org/docs/#line-chart-introduction), or [CanvasJS](http://canvasjs.com/html5-javascript-line-chart/).
