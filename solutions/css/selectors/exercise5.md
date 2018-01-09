# Compute the specificity scores

  1. `* { }`
    * 0	
  1. `li { }`
    * 1 (one element)
  1. `li:first-line { }`
    * 2 (element + pseudo-element)
  1. `ul li { }`
    * 2 (two elements)
  1. `ul ol+li { }`
    * 3 (three elements)
  1. `h1 + *[rel=up] { }`
    * 11 (one attribute, one element)
  1. `ul ol li.red { }`
    * 13 (one class, three elements)
  1. `li.red.level { }`
    * 21 (two classes, one element)
  1. `style=""`
    * 1000 (one inline styling)
  1. `p { }`
    * 1 (one element)
  1. `div p { }`
    * 2 (two elements)
  1. `.sith`
    * 10 (one class)
  1. `div p.sith { }`
    * 12 (two elements and a class)
  1. `#sith`
    * 100 (one id)
  1. `body #darkside .sith p { }`
    * 112 (element, ID, class, element)
