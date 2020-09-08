#!/usr/bin/env bb
; uses babashka clojure to run
; brew install borkdude/brew/babashka
; see https://github.com/borkdude/babashka
; KEYS=[dir file_system walk iterate file]

(defn get-files [dir]
  (file-seq (clojure.java.io/file "/tmp")))


(defn print-files [dir]
  (doseq [file (get-files dir)]
    (prn file)))

(let [[dir] *command-line-args*]
  (when (empty? dir)
     (println "Usage: <directory>")
     (System/exit -1))
  (print-files dir))
