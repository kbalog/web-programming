# Assignment 6 - Gradebook

You task is to write a python script that takes three text files as input, and generates a set of HTML files based on that input.

### Input

The three input files are called `grades.tsv`, `courses.tsv`, and `students.tsv`. These contain data in tab-separated format.

The `grades.tsv` file has the following format (`{}` denote variables):
```
{student_no} {course_code} {semester} {grade}
```
I.e., each line is a grade of a certain person on a specific course in a given semester.

  - `student_no` is a numerical value
  - `course_code` has the format `XXXYYY` where `X` is a capital letter (`[A..Z]`) and `Y` is a digit (`[0..9]`)
  - `semester` is a numerical value (`1..10`)
  - `grade` is a value in the `A..F` range

The `courses.tsv` file contains the names of courses, one line per course:
```
{course_code} {course_name}
```

The `students.tsv` file contains the names of students, one line per student:
```
{student_no} {student_name}
```


### Output

You need to complete the `gradebook.py` file such that it generates a set of HTML files, organized in a dictionary structure, under the `output` folder.

  - `index.html`
    * This file contains an overview and links to all files. Specifically, there should be three tables:
        - List of all students, with columns "student no" and "name", sorted by student number. Add a link on the student number to the student's profile page.
        - List of all courses, with columns "course code" and "name", sorted by course code. Add a link on the course code to the course's page.
        - List of all semesters, with columns "semester" and "courses", sorted by semester. The course codes need to be sorted alphabetically. Add a link on the semester number to the semester's page, and a link on each of the courses to the course's page.        
  - `students/{student_no}.html`
    * For each student, there should be a file that contains:
        - The name and student number of the student.
        - A list (table) of all courses (with course code and name) together with the grade.
        - Courses need to be grouped and ordered by semesters.
  - `courses/{course_code}.html`
    * For each course, there should be a file with a list of student numbers and corresponding grades, ordered by student number. There should be a second table which summarizes the number of `A`s, `B`s, ... `F`s for that course (you may skip the zeros, i.e., if no one got a `C` then you don't have to show `C` in that table).
  - `semesters/{semester}.html`  
    * For each semester, there should be a file that shows a table with the list of courses given in that semester and the total number of students (that got a grade for that course). Courses should be ordered alphabetically by course code.


All HTML files need to be valid (i.e., with `<head>`, `<body>`, etc.) and need to use a shared CSS file.  The CSS file is already given (but you are free to make changes to it, if you wish).  The CSS file `gradebook.css` is in the same folder as `gradebook.py`.

You are given a skeleton, which (i) generates the necessary directory structure (but not the files within the directories) and (ii) a table with a list of students for `index.html` file. You may assume that the three input files (`grades.tsv`, `courses.tsv`, `students.tsv`) are in the same folder as this script and that their content is valid (i.e., follows the above format).

Under the `sample_output` folder, you can find the output corresponding to the given input files; this is what your script needs to generate.


### Submission

You need to submit (i.e., push to GitHub):

  - The completed script `gradebook.py`.
  - The output that this script generated for the given input data, i.e., the contents of your `output` folder.

Mind that we will also test your code with a different input (which follows the exact same format).


# Øving 6 - Karakterbok

Du skal lage et python-script som tar inn tre tekstfiler som input, og generere HTML filer basert på disse teksfilene.

### Input

De tre inputfilene kalles `grades.tsv`, `courses.tsv`, og `students.tsv`. Disse filene inneholder data i et 'tab'-separert format.

`grades.tsv` filen har følgende struktur, hvor `{}` inneholder variablene.
```
{student_no} {course_code} {semester} {grade}
```

Hver linje innheolder karakteren som en person fikk i et fag, ved et gitt semester.

  - `student_no` er et tall
  - `course_code` har formatet `XXXYYY`, hvor `X` er en stor bokstav (`[A..Z]`) og `Y` er et siffer (`[0..9]`)
  - `semester` har tallverdier (`1..10`)
  - `grade` har er en karakterer, A-F

`courses.tsv` filen inneholder navnene til kursene, en linje per kurs:
```
{course_code} {course_name}
```

`student.tsv` filen inneholder navenen til studentene, en linje per student:
```
{student_no} {student_name}
```


### Output

Du må fullføre `gradebook.py` filen, slik at den genererer et set med HTML filer, sortert i `output` mappen.

  - `index.html`
    * Denne filen inneholder en oversikt og linker til alle filer. Det skal være tre tabeller:
        - Liste over alle studenter, med kollonene "student no" og "name", sortert etter "student no". Legg til en link på studentnummeret til studentens profilside
        - Liste over alle emner, med kollonene "course code" og "name", sortert etter "course code". Legg til en link på emnekoden til emnets side.
        - Liste over alle semestere, med kollonene "semester" og "kurs", sortert etter "semester". Emnekodene skal sorteres alfabetisk. Legg til en link på semesteret til semesterets side, og en link på hvert kurs til kursets side.

  - `students/{student_no}.html`
    * For hver student skal filen inneholde:
        - Studentens navn og studentnummer
        - En liste (tabell) over alle emner (med emnekode og emnenavn), sammen med karakter
        - Emner skal være gruppert og sortert etter semester
  - `courses/{course_code}.html`
    * For hvert emne skal det være en liste med studentnummere og de tilhørende karakterer, sortert etter studentnummer. Det skal også være en tabell som summerer antall `A`er, `B`er, ... `F`er for det kurset ('nuller' kan ses bort i fra, for eksempel ved tilfeller hvor ingen har fått én `C`, trenger du ikke å vise `C` i tabellen)
  - `semesters/{semester}.html`
    * For hvert semester skal det være en fil som viser en tabell med liste over alle emner for det gitte semesteret, og totalt antall studenter (som har fått en karakter i emnet). Kurs skal være sortert alfabetisk etter emnekode.   


Alle HTML filer skal være gyldige (`<head>`, `<body>`, etc) and skal bruke en felles CSS fil. CSS filen er gitt, men du har lov til å gjøre forandringer på denne om du ønsker. CSS filen `gradebook.css` er i samme mappe som `gradebook.py`.

Du er blitt gitt et script, som (i) generer mappestrukturen (men ikke filene) og (ii) en tabell med liste over studenter til `index.html` filen. Du kan anta at de tre inputfilene (`grades.tsv`, `courses.tsv`, `students.tsv`) er i samme mappe som dette scriptet og at innholdet er i riktig format (som oppgitt tidligere i oppgaveteksten).

I `sample_output` mappen, kan du finne outputet som hører til de gitte inputfilene; dette er hva scriptet ditt skal generere.


### Innlevering

Du må laste opp filene (mao., push to GitHub):

  - Det ferdige scriptet `gradebook.py`
  - Outputet som dette scriptet generert med det gitte inputdataen, altså innholdet i din `output` mappe.

Husk at vi skal teste koden din med forskjellig input (men som har samme format)
