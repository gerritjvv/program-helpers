#!/usr/bin/env clj
; KEYS=[browser url open]

(require '[clojure.java.browse :as browse])

(def websites ["https://clojure.org"])


(doseq [site websites]
   (browse/browse-url site))

(System/exit 0)