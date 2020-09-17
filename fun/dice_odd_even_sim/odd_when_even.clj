#!/usr/bin/env clj
;; For a dice with 6 equiprobable outcomes, what is the probability of odd when even
;; we model Odd = 1, Even = 2

(defn roll [] (rand-nth [1 2]))

(defn win? [a b]
   (and (even? a) (odd? b)))


(defn run []
    (let [a (roll)
          b (roll)]
          (win? a b)))


(defn experiment [total]
    (->>
       run
       repeatedly
       (take total)
       (filter true?)
       count))


(doseq [_ (range 0 10)]
  (let [total 10000
      n (experiment total)]

      (println n "/" total " => " (double (/ n total)))))
