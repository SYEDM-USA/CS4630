### Develop a python GUI stoichiometry app that takes in a balanced chemical equation and weight of a substance, and outputs some property of other substances.

Interface:
•	2 rows of 6 column input cells: 1st row is input of the balanced equation - (up to) 3 reactants and (up to) 3 products. [implied + sign b/w reactants, & between products]
•	One of the corresponding cells in the 2nd row is also an input - lab measurement of that substance (in grams).   
•	A checkbox to specify the unit for all outputs – checked means molecules, else moles. 

User inputs the equation, checks (or unchecks) the checkbox and hits compute button. The app computes/populates the other cells of the 2nd row. Assume valid inputs (no space or illegal compounds, etc.)

Sample run [eqn: 3Hg(OH)2 + 2H3PO4 = Hg3(PO4)2 + 6H2O] with checkbox unchecked - consider adding ‘=’ to separate reactants & products. The app computes output cells 1, 4, and 5. 


