# Assignment 4 - JavaScript

Create an address book application using JavaScript (plus HTML and CSS).
(It is not allowed to use jQuery!)

The **required functionality** is the following:

  *	Entries
    -	Entries have the following fields: name, telephone number, email
    -	Individual entries must be represented as an Entry object
    -	The contact list must be represented as an array of Entry objects
    -	The application must be shipped with some sample initial data (meaning, with a non-empty address book)
  *	Display a list of entries
    -	Emails should be clickable links that open in the mail client
  *	Add a search field to filter the list
    -	Only those entries are displayed that contain the searched string as part of the name, telephone, or email
    -	Matching is case-insensitive
  *	The user can delete existing entries
    -	Ask for a confirmation before deleting the entry
  *	The user can add new entries
    -	Perform input check
        -	The name field must never be empty
        -	Either tel or email has to be filled in
        -	Email has to be a valid email
        -	Tel may contain only numbers and + - ( ) and space

In addition, you need to implement **at least one extra feature** (of your choosing) from the following options:

  * Allow the list to be sorted based on name, telephone, or email. The sorting criteria can be chosen from a select list.
  *	Add a settings panel that is hidden by default and is shown by clicking a button or link. The user can customize the appearance of the list, for example, change the font family and size for the different fields (name, tel, email), from predefined lists.
  *	Allow for existing entries to be modified.

The `samples/` folder in your GitHub repository contains some example screenshots. Note that the appearance is left to you, it doesn’t have to look the same.

Commit and push the files to GitHub.


# Øving 4 - JavaScript

Lag en kontaktlisteapplikasjon ved hjelp av JavaScript (og HTML og CSS).
(Det er ikke lov å bruke jQuery!)

Følgende funksjonalitet er **påkrevd**:

  *	Oppføringer
    -	Kontaktene har følgende felter: navn, telefonnummer, epostadresse
    -	Hver oppføring skal være representert som et Entry-objekt
    -	Kontaktlisten skal være representert som en array av Entry-objekter
    -	Applikasjonen skal leveres med eksempeldata (altså ikke en tom kontaktliste)    
  * Vise en liste av oppføringer
    -	Epostadresser skal vise som klikkbare linker som åpnes i epostklienten (f.eks. Outlook)
  *	Legg til et søkefelt for å filtrere listen
    -	Vis kun de oppføringene som har søkestrengen som en del av navnet, telefonnummeret eller epostadressen
    -	Søket skal være case-insensitive (ikke gjøre forskjell på små og store bokstaver)
  *	Brukeren kan slette oppføringer
    -	Be om bekreftelse før oppføringen blir slettet
  *	Brukeren kan legge til oppføringer
    -	Sjekk verdiene som blir fylt inn
        -	Navnet kan ikke være tomt
        -	Enten telefonnummer eller epostadresse må oppgis
        -	Epostadressen må være en gyldig epostadresse
        -	Telefonnummeret kan kun inneholde tall og + - ( ) og mellomrom

Du må implementere **minst en** (valgfri) av følgende **ekstrafunksjoner**:

  * Lag mulighet for å sortere listen på navn, telefonnummer eller epostadresse. Sorteringsvalget kan velges i en dropdown/select list (nedtrekksliste).
  * Legg til et kontrollpanel. Som standard er dette skjult, men kan vises ved å trykke på en knapp eller link. Her kan brukeren tilpasse listens utseende, for eksempel endre font family (skrifttype) og størrelse på de forskjellige feltene (navn, telefon, epost) fra forhåndsdefinerte lister med valg.
  * Lag mulighet for å endre på eksisterende oppføringer.

I mappen `samples/` i din GitHub repository ligger noen skjermbilder med eksempler. Merk at du bestemmer selv hvordan applikasjonen ser ut, den må ikke nødvendigvis se ut som i eksemplene.

Commit og push filene til GitHub.
