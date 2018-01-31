# Assignment 3 - Booking prototype

In this assignment you need to create a prototype for a (cabin and/or hotel) booking site using HTML and CSS. The prototype consists of three HTML pages (main page, property page, and checkout) and a single stylesheet file (style.css).

Under the `samples/` folder of the starting files (in your private GitHub repository) you will find screenshots that serve as examples of what you need to create. You don't have to produce the exact same output that is shown on the samples, you can deviate from it in any way you want (especially in the content) as long as you follow the instructions given below.


### Fonts and colors

  *	Sans-serif font family.
  * All headings are typeset Montserrat, all other text is typeset Raleway.
    -	https://fonts.google.com/specimen/Montserrat
    -	https://fonts.google.com/specimen/Raleway
  *	Font sizes are controlled by the browser; all font sizes need to be set relative, using *em*.
  *	Background color is white.
  *	You need to select a color palette from http://www.colourlovers.com/palettes, with maximum five colors, and use only those colors (plus white for page background).
    -	Provide in the `README.md` file the link to the chosen palette and also list the hex codes of the colors from that palette.


### Layout

  *	We need a fluid layout, where elements resize automatically when the page is resized. For that, you'll need to specify widths using percentages.
  *	Use the `<header>`,` <main>`, and `<footer>` HTML5 tags for structuring the page.
  *	The elements below are the same on all pages.
  *	**Header**
    -	Height is 40px. The header is always visible, even when the page is scrolled down.
    -	The logo area has a height of 60px. It is positioned 5% from the left of the page.
        -	You can write the name of your site here and/or create a logo.
        -	The logo needs to overlay any content (i.e., needs to have the highest z-index).
    -	The main menu is part of the header and is horizontally aligned.
        -	It has to be an unordered list inside a `<nav>` element.
        -	It is right aligned and 5% from the right side of the page.
        -	"Properties" points to index.html.
        -	"Special deals" points to property.html.
        -	"Checkout" points to checkout.html.
  *	**Main**
    -	There has to be 100px vertical space between the header and the top of the main area.
    -	The main area is 90% of the width of the page and is center-aligned. That means it resizes automatically when the window is resized, but has a minimum width of 600px and a maximum width of 1200px (see the screenshots under `samples/`).
    -	The main header (h1) inside main has a background color, 1.2em font size, and 5px padding around.
    -	Framed boxes have a solid 1px border and 5px padding. The font-size is 0.8em.
  *	**Footer**
    -	The footer always stays at the bottom of the page, but "scrolls away" (i.e., when the page is long, you need to scroll down to see the footer)
        -	See, e.g.,: https://css-tricks.com/snippets/css/sticky-footer/
    -	The height of the footer is 120px. It has a 5px wide top border.
    -	The footer contains contact information (tel, email). These are center-aligned both vertically and horizontally.


### Main page (`index.html`)

  *	The image banner has a width of 100% (that is, relative to the `<main>` element) and resizes with the page. It has 5px wide solid top and bottom borders.
  *	Lists (at least) 6 different properties
    -	Put each property inside an `<article>` element.
    -	There should be two properties per row. The property boxes resize automatically with the page.
    -	Put both vertical and horizontal space between the boxes.
    -	Image size is 200x150px.
    -	Product name is in `<h3>`, with no margins.
    -	Put the location over the image in a transparent box (hint: set z-index).
    -	Other formatting is the same as for framed boxes (i.e., solid 1px border, 5px padding, 0.8em font-size).
  *	Change the appearance of the property box on mouseover (for example, change the background or borders).
  *	"Details" needs to be a link in the bottom right corner with a double border (hint: use the outline property). On mouseover, it has to change its color.


### Property page (`property.html`)

  *	Show the image, name, and short description of the property at the top of the page in a framed box.
  *	The check-in form area is aligned to the bottom of the top box.
  *	Check-in is a HTML5 date field, nights is a select list, "Book property" is a submit button.
  *	Display a "Details" header (h1).
  *	Display a long description in a framed box.


### Checkout page (`checkout.html`)

  *	Show the image, name, and short description of the property in a framed box.
  *	Display a "Checkout" header (h1).
  *	Divide the form into 4 fieldsets, where each fieldset has a solid 1px border around it.
    1.	Check-in and check-out dates are disabled fields.
    2.	Name, street, city, and postcode are text input fields, country is a select list.
    3.	Comment is a textarea field that is 30 chars in width and 4 rows in height.
    4.	A submit button with the label "Book property". The button is center-aligned.
  *	Use `<label>` tags to align the fields, as shown in `samples/checkout.png`.
  *	All form elements must have the obligatory attributes.


Commit and push the files you created (`index.html`, `property.html`, `checkout.html`, `style.css`, plus optional images) to GitHub.



# Øving 3 - Booking prototype

I denne innleveringen skal du lage en prototype for en (hytte og/eller hotell) booking side med HTML og CSS. Denne prototypen skal bestå av tre HTML sider (hoved-, eiendom- og utskjekk-side) og en enkel css-fil (style.css).

Under `samples/` mappen av startfilene (i din egen private GitHub repository) finner du skjermbilder som skal fungere som eksempel av hva du skal lage. Du trenge ikke å lage en eksakt kopi av bildene, og så lenge du følger instruksjonene under kan du forandre på dem som du ønsker (spesielt i innhold).


### Font og farge

  *	Sans-serif font familie.
  *	Alle headings er av typen Montserrat, all annen tekst av typen Raleway.
    -	https://fonts.google.com/specimen/Montserrat
    -	https://fonts.google.com/specimen/Raleway
  *	Font størrelse er kontrollert av nettleser; ergo må de alle være relative, med bruk av *em*.
  *	Bakgrunnsfargen skal være hvit.
  *	Du må velge en color palette fra http://www.colourlovers.com/palettes, med max fem farger, og bruk kun disse fargene (pluss whit for sidebakgrunn).
    -	Oppgi i `README.md` lenken til den valgte paletten, og oppgi også heksekoder for fargene fra den paletten.


### Layout

  *	Det trengs et flytende layout, hvor elementer automatisk tilpasser seg når størrelsen på siden forandres. Du må derfor spesifisere bredde i prosenter.
  *	Bruk `<header>`, `<main>`, og `<footer>` HTML5 taggene for å strukturere siden.
  *	Elementene under er like på alle sider.
  *	Header
    -	Høyden er 40px. Headeren er alltid tilgjengelig, selv om vi blar nedover siden.
    -	Logoen skal ha en høyde på 60px. Den er posisjonert 5% fra venstre kant av siden.
        -	Du kan skrive navnet på siden din her og/eller lage en logo
        -	Logoen må ligge over alle andre typer innhold (ergo den trenger å ha den høyeste z-indexen).
    -	Hovedmenyen er en del av headeren og ligger på rekke horisontalt.
        -	Det skal være en uordnet liste inni et `<nav>` element.
        -	Den være høyre justert og er 5% fra høyre side av dokumentet.
        -	"Properties" (Eiendommer) peker til index.html.
        -	"Special deals" peker til property.html.
        -	"Checkout" peker til checkout.html.
  *	Main
    -	Det skal være 100px vertikalt rom mellom headeren og toppen av main.
    -	Skal være 90% bredden til siden og være sentrert. Det betyr at den skal automatisk tilpasse seg når sidestørrelsen forandres, men den skal ha en minimum bredde på 600px og en maksimum bredde på 1200px (se bildene under `samples/`).
    -	Hovedoverskriften (h1) i main skal ha en bakgrunnsfarge, 1.2em font størrelse og 5px padding rundt.
    -	Innrammede bokser har en solid 1px border og 5px padding. Font størrelse 0.8em.
  *	Footer
    -	Footeren skal alltid være på bunnen av siden, men "blas vekk" (så viss siden er for lang må du bla ned for å se den).
        -	Se, for eksempel: https://css-tricks.com/snippets/css/sticky-footer/
    -	Høyden skal være på 120px. Den skal ha en 5px bred topp border.
    -	Footeren skal inneholde kontaktinformasjon (telefon, e-post). Disse er sentrert både vertikalt og horisontalt.


### Main page (`index.html`)

  *	Bildebanneret skal ha en bredde på 100% (relativt til <main> elementet) og skal automatisk tilpasses sidestørrelsen. Den skal ha en 5px bred solid topp og bunn border.
  *	Det skal listes (minst) 6 forskjellige eiendommer
    -	Sett dem i ett eget `<article>` element.
    -	Det skal være to eiendommer per rad og boksene deres skal automatisk tilpasses.
    -	Lag både vertikal og horisontal plass mellom boksene.
    -	Bildestørrelse er 200x150px.
    -	Produktnavn skal skrives i `<h3>`, uten margins.
    -	Set lokasjonen over bildet i en gjennomsiktig boks (hint: bruk z-index).
    -	Annen formatering er den samme som for innrammede bokser (altså solid 1px border, 5px padding, 0.8em font-size).
  *	Eiendom boksen skal forandre utseende ved "mouseover" (for eksempel, forandre bakgrunn eller border).
  *	"Details" må være en link i bunnen av høyre hjørne med en dobbel border (hint: bruk *outline* egenskapen). Ved "mouseover" skal den forandre farge.


### Property page (`property.html`)

  *	Vise bildet navnet og en kort beskrivelse av eiendommen på toppen av siden i en innrammet boks.
  *	"Check-in" form området er justert/festet til bunnen av toppboksen.
  *	"Check-in" er en HTML5 dato felt, netter er en valgt liste og "Book property" er en submit button.
  *	Viser en "Details" header (h1).
  *	Viser en lang beskrivelse i en innrammet boks.


### Checkout page (`checkout.html`)

  *	Vis bildet navnet og en kort beskrivelse av eiendommen i en innrammet boks.
  *	Vise en "Checkout" header (h1).
  *	Del skjemaet i 4 feltsamlinger hvor hver samling har en solid 1px border rundt seg.
    1. "Check-in" og "check-out" datoer er deaktiverte felt.
    2. Navn, gate, by og postkode er innskrivning felt for tekst, land er en valgt liste.
    3. Kommentar er et tekstfelt som er 30 tegn bredt og 4 rader høyt.
    4. En submit button med skriften "Book property". Knappen er sentrert.
  *	Bruk `<label>` tagger for å justere feltene, som vist i `samples/checkout.png`.
  * Alle form elementene må ha de obligatoriske attributt.


Commit og push filene du laget (`index.html`, `property.html`, `checkout.html`, `style.css`, plus valgfrie bilder) til GitHub.
