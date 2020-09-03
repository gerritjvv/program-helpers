#!/usr/bin/env clj

(import '(java.util.zip ZipFile))

(defn filenames-in-zip [filename]
  (let [z (java.util.zip.ZipFile. filename)]
    (map #(.getName %) (enumeration-seq (.entries z)))))

(defn print-files [zip-file]
   (doseq [file (filenames-in-zip zip-file)]
     (prn file)))

(let [[zip-file] *command-line-args*]
  (when (empty? zip-file)
     (println "Usage: <zip-file>")
     (System/exit -1))
  (print-files zip-file))
