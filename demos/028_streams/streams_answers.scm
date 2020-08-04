;(1 . #[promise (not forced)])

(define inf_num
  (cons-stream 1 inf_num)
)


(define evens
  (begin
    (define (evens_helper n)
      (cons-stream n (evens_helper (+ n 2)))
    )
    (evens_helper 2)
  )
)
