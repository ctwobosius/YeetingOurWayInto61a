
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
;(operator operand1 operand2 ...)
(+ 3 3)
; after evaluating operator, then operands, apply operator to operands

; Control
(if <predicate> <if-true> <if-false>)

(cond
        (<condition> <return>)
        ((> x 0) 'positive)
        ((< x 0) 'negative)
        (else 'zero))       ; optional else

; Defining variables, functions, lambdas
(define <name> <expression>)
(define (<name> <param1> <param2> ...) <body>)
(lambda (<param1> <param2> ...) <body>)

; Lists (Linked)
(cons first rest) ; create a single link
(cons 1 (cons 2 (cons 3 nil)))
; (1 2 3)
(car linkedList) ; first
(cdr linkedList) ; rest

(list item0 item1 ...)
; creates a linked list
; (list 1 2 3) is the same as (cons 1 (cons 2 (cons 3 nil)))
