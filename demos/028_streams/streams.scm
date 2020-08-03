;Streams = "Lazily computed list/cons"
(cons 1
  (cons (/ 1 0) nil)
)

; to construct, use cons-stream
(cons-stream 1
  (cons-stream (/ 1 0) nil)
)
;(1 . #[promise (not forced)])
; 1 is the car, and the rest is a "promise", which basically means
; "we'll promise to compute this later"

; to get to the cdr of a cons-stream, need to use cdr-stream
; eg:
(cdr-stream someStream)


; advantage of streams: infinite lists! Kinda like generators/iterators
(define inf_num
  ; scm> (car inf_num)
  ; 1
  ; scm> (car (cdr-stream inf_num))
  ; 1
  ; scm> (car (cdr-stream (cdr-stream inf_num)))
  ; 1
  ___
)


(define evens
  ; scm> (car evens)
  ; 2
  ; scm> (car (cdr-stream evens))
  ; 4
  ; scm> (car (cdr-stream (cdr-stream evens)))
  ; 6
  (____
    (define (evens_helper n)
      (cons-stream ___ (____))
    )
    ____
  )
)
