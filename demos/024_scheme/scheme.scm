
; Scheme: where spacing don't matter'd and parentheses are splatter'd
; Capitals don't matter
; rainbow-delimiters or bracket-colorizer
((((((+ 3 3))))))

; Numbers
1, 2, 333
1.2

; Strings
'String
'(+ 1  2)

; Booleans
#t ; true
#f ; This is the ONLY false-y value, everything else is true-thy
nil ; equivalent to None
; equivalent of False from Python
; short circuiting does apply in scheme
(and )
(or )

; Evaluation
;(operator operand1 operand2 ...)
; (function arg1 arg2)
(+ 3 3)
; after evaluating operator, then operands, apply operator to operands

; Control
(if <predicate> <if-true> <if-false>)
(if (> 1 2) (+ 2 3) (- 2 3))
if predicate:
  return if_true


(cond
        (<condition> <return>)
        ((> x 0) 'positive)
        ((< x 0) 'negative)
        (else 'zero)
)       ; optional else

; Defining variables, functions, lambdas
(define <name> <expression>) ; variables name = expr
(define (<name> <param1> <param2> ...) <body>) ; functions
(lambda (<param1> <param2> ...) <body>) ; lambdas

; Lists (Linked)
(cons first rest) ; create a single link
  ; Link(first, rest)
(cons 1 (cons 2 (cons 3 nil)))

(car linkedList) ; first
(cdr linkedList) ; rest

(list item0 item1 ...)
; creates a linked list
; (list 1 2 3) is the same as (cons 1 (cons 2 (cons 3 nil)))
