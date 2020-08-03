Macros what? A macro rundown (also seen in disc11)


scm> (define (twice f) (begin f f))
twice
scm> (twice (print 'woof))
woof
>>> twice(print(“woof”))
(print 'woof) is evaluated prematurely (nil gets passed into twice)

scm> (eval ‘(+ 2 3))
5

scm> (define-macro (twice f) (list 'begin f f))
twice
scm> (twice (print 'woof))
woof
woof

(begin 23 24 2 (print 4) 9)
; evaluates each argument, but only returns the last one

the f that is passed into the macro is unevaluated, and then after passing in the f’s, it calls (eval (return_statement))
ie:
(eval (list 'begin f f))

where f is replaced by the unevaluated arguments. So the above becomes:
(eval (list 'begin '(print 'woof) '(print 'woof))
('begin '(print 'woof) '(print 'woof))

(begin (print ‘woof) (print ‘woof))
equivalent to
(begin (print 'woof) (print 'woof))

'literal
the rules for evaluating calls to macro procedures are:
1. Evaluate operator
2. Apply operator to unevaluated operands
3. Evaluate the expression returned by the macro in the frame it was called in

;https://inst.eecs.berkeley.edu/~cs61a/fa18/assets/pdfs/61a-fa18-final.pdf#page=8
;6c

;https://cs61a.org/assets/pdfs/61a-sp19-final.pdf#page=8
;8



; Not scheme:
;https://cs61a.org/exam/fa19/final/61a-fa19-final.pdf#page=6
;6
