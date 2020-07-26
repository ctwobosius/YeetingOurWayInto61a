
; Scheme: where spacing don't matter'd and parentheses are splatter'd
; rainbow-delimiters or bracket-colorizer
((((((+ 3 3))))))

; Numbers
1, 2, 333

; Strings
'String

; Booleans
#t
#f

; Evaluation
;(operator operand1 operand2...)
(+ 3 3)
; after evaluating operator, then operands, apply operator to operands

; Control
(if <predicate> <if-true> <if-false>)

(cond
        (<condition> <return>)
        ((> x 0) 'positive)
        ((< x 0) 'negative)
        (else 'zero))       ; optional else

; Defining variables and functions
(define <name> <expression>)
(define (<name> <param1> <param2> ...) <body>)
