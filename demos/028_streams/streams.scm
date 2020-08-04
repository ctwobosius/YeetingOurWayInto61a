;Streams = "Lazily computed list/cons"
(cons 1
  (cons (/ 1 0) nil)
)
; What will this do?
; Error


(1 ...)

; to construct, use cons-stream
(cons-stream 1
  (cons-stream (/ 1 0) nil)
)
; What will this do?
; (1 . #[promise (not forced)])

; not forced = not computed yet

; 1 is the first, and the rest is a "promise", which basically means
; "we'll promise to compute this later"

; to get to the cdr of a cons-stream, need to use cdr-stream
; eg:
(cdr-stream someStream)


; Advantage of streams: infinite lists! Kinda like generators/iterators
(define inf_num
  ; scm> (car inf_num)
  ; 1
  ; scm> (car (cdr-stream inf_num))
  ; 1
  ; scm> (car (cdr-stream (cdr-stream inf_num)))
  ; 1
  (cons-stream 1 inf_num)
)


(define evens
  ; scm> (car evens)
  ; 2
  ; scm> (car (cdr-stream evens))
  ; 4
  ; scm> (car (cdr-stream (cdr-stream evens)))
  ; 6
  (begin
    (define (evens_helper n)
      (cons-stream (* 2 n) (evens_helper (+ 1 n)))
    )
    (evens_helper 1)
  )
)



(define (evens n)
  (cons-stream (+ 2 n) (evens (+ 2 n)))
)


(define (evens_helper n)
  (cons-stream (+ 2 n) (evens_helper (+ 2 n)))
)

(define evens n
  (evens_helper 0)
)

evens = (), ()
(define evens () ())
(define var (+ 2 3) 5)


evens = (evens_helper __)
(2 (evens_helper 2))
(2 (4 ()))
(2 4 6 8 10)
