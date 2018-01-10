# UiS DAT310 Exam information 2018 spring

## Entrance requirements

Min. 4 points from Assignments 1–5 and min. 4 points Assignments 6–10.


## Allowed resources

  * All written and printed material
    - Including textbooks, slides, program code, etc.
  * The following websites
    - http://w3schools.com (except the online 'tryit' editors! site search within w3schools is OK)
    - http://docs.python.org
    - http://flask.pocoo.org
    - http://jinja.pocoo.org
    - https://dev.mysql.com/doc/connector-python/en/
    - http://api.jquery.com
    - http://getbootstrap.com
    - http://github.com/kbalog/web-programming
    - http://speakerdeck.com/kbalog
    - http://translate.google.com

It is **not allowed** to 'run' code and test it in a browser!


## Grading

Total: 100+N points, where N is the number of multiple choice questions
  * For multiple choice questions: correct answers=2 or 3 points, incorrect answers=-1 points
  * If you got bonus points from the assignments, bring your bonus code(s)

Scale:
  * 0-39: F
  * 40-49: E
  * 50-59: D
  * 60-79: C
  * 80-89: B
  * 90+: A


## Topics

**This is a tentative list based on last year's requirements, and is subject to changes.**

  * **Client vs. server-side programming**
  * **HTML**
    - Syntax
    - Document structure
    - Main head elements
    - Main body elements
        - Headings
        - Paragraphs
        - Text formatting
        - Character entities
        - Lists (ordered, unordered)
        - Tables (table head/body, merging rows and columns)
        - Images
        - Links
        - Container elements (div and span, and the difference between them)
        - iframe
    - Forms
        - Form elements (input text, password, radio, checkbox, select list, textarea, button)
        - Hidden variables
        - HTML5 form elements (number, date, email, url, search)
        - Global attributes (disabled, readonly, required)
        - Labeling and grouping form elements
  * **CSS**
    - Syntax (selectors, declarations, comments)
    - CSS levels
        - inline (using the style attribute)
        - internal (using the `<style>` element in `<head>`)
        - external (using `<link>` inside `<head>` to an external css file)
    - Difference between id-s and classes
    - Styling/formatting using CSS
        - Text (color, font, size, alignment, spacing, etc.)
        - Links (and pseudo selectors based on state)
        - Lists
        - Borders
        - Colors and backgrounds
    - The box model, setting border, margin, and padding
    - Selectors
        - Element, class, ID selectors
        - Contextual selectors (child, descendant, sibling, etc.)
        - Pseudo-class and attribute selectors
    - Cascading rules, CSS priority scheme
        - Selector specificity, computing specificity
        - Inheritance
        - Positioning
        - Difference between block-level and inline elements
    - Positioning schemes (normal flow, relative, absolute, fixed positioning, floating elements)
    - Media queries
  * **JavaScript**
    - Syntax (variables, functions, objects, control flows, comments)
    - Embedding in HTML (explicit, implicit), execution (when in head vs. in body)
    - Variables (types, scope)
        - Primitive types
        - Type conversions, type coercions
        - Operators (comparison, boolean, numeric, string)
    - Displaying to console
        - Functions (assigned to variables, passed as parameters)
    - Objects
        - Prototypes
        - Properties
        - Methods
        - instanceof operator
        - Built-in objects (Number, Math, Array, String, Date)
    - Event handling
        - Common events (blur, change, click, mouseover, mouseout, keypress, keyup, keydown, submit)
        - Accessing event properties
        - Assigning event handlers
    - Document Object Model (DOM)
        - Window and document objects
        - Accessing DOM elements (by ID, tag name, class name)
        - Creating, deleting, modifying DOM elements
        - Getting and setting the attributes of DOM elements (including forms)
        - Traversing the DOM (finding children and parent elements)
    - Browser Object Model (BOM)
    - AJAX requests and JSON handling
  * **AJAX**
    - Difference between synchronous and asynchronous communication
    - Main elements of AJAX interaction
        - Initial HTML content
        - Request phase
        - Response document
        - Receiver phase
    - Using XMLHttpRequest in JavaScript
    - Using JSON on client (JavaScript) and server (Python) sides
  * **jQuery**
    - Including jQuery (local copy vs. from CDN)
    - Anatomy of a jQuery function (selector, event, function)
    - Selectors
        - Basic (element, class, id)
        - Special (document, this)
        - Hierarchy and attribute selectors
        - Input selectors
    - Events
        - Document/window events
        - Form events (blur, change, focus, select, submit, …)
        - Keyboard events (keydown, keypress, keyup, …)
        - Mouse events (click, dblclick, mouseover, mouseout, …)
        - Event attributes
        - Attaching and removing event handlers
    - Methods
        - Accessing and modifying html content, attributes and values
        - Accessing and modifying css properties, class attributes
        - Creating, Inserting, and removing DOM elements
        - Traversing the DOM (parent, children, siblings, etc.)
    - Animation and effects
        - Basic effects (hide, show, toggle)
        - Basic animation (fade, slide, animate)
    - AJAX calls
        - $.ajax(), $.get(), $.post()
        - load(), loadJSON()
  * **Web protocols and APIs**
    - URLs, IP addesses, domain names
    - HTTP request and response formats
        - Request methods (GET, POST, PUT, DELETE)
        - Status codes (common codes (200, 301, 404) and meaning of ranges (1xx, 2xx, 3xx, 4xx, 5xx))
        - MIME types
    - Making HTTP requests with Python, JavaScript, and jQuery
    - RESTful web APIs
    - Same-origin policy
    - JSONP
  * **Bootstrap**
    - Including Bootstrap (local copy vs. from CDN)
    - Styling fundamental HTML elements
    - Styling forms
    - Using the responsive grid system and containers
    - Using additional components (navbar, alerts, progress bars)
  * **Python**
    - Syntax (variables, functions, objects, control flows, comments)
    - Data structures (lists, sets, dictionaries)
    - Reading and writing text files
    - Routing HTTP requests
    - Serving static files and dynamic content
    - Redirecting    
    - Templates
        - Variables, filters
        - For loops
        - Template inheritance
        - Message flashing
    - Form handling
    - Cookies
        - Initializing, reading/writing values
        - Third-party cookies
    - Sessions
        - Initializing, reading/writing values
    - MySQL
        - Connecting/disconnecting
        - Executing SQL statements (INSERT, DELETE, UPDATE)
        - Fetching data (SELECT) and iterating results
    - JSON handling
