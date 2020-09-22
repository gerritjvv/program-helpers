package gerritjvv;
// KEYS=[java streams partition sequence partition-all nodeps]

import java.util.*;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;

/**
 * Acts list the Clojure partition-all function and partitions a sequence into at most N items per partitions.
 * <p>
 * Partitioning a list of 45 items by 20 would give:
 * <pre>
 * Partition: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
 * Partition: [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
 * Partition: [41, 42, 43, 44, 45]
 * </pre>
 */
public class Partition {


    public static <T> Iterator<List<T>> iterator(Iterable<T> it, int length) {
        return PartitionIterator.iterator(it.iterator(), length);
    }

    public static <T> Spliterator<List<T>> spliterator(Iterable<T> it, int length) {
        return PartitionIterator.spliterator(it.iterator(), length);
    }

    public static <T> Stream<List<T>> stream(Iterable<T> it, int length) {
        return PartitionIterator.stream(it.iterator(), length);
    }

    public static class PartitionIterator<T> implements Iterator<List<T>> {

        final Iterator<T> it;
        final int length;
        List<T> current;

        public PartitionIterator(Iterator<T> it, int length) {
            this.it = it;
            this.length = length;
        }

        @Override
        public boolean hasNext() {

            int i = 0;
            while (it.hasNext() && i++ < length) {
                if (current == null)
                    current = new ArrayList<>(length);

                current.add(it.next());
            }

            return current != null;
        }

        @Override
        public List<T> next() {
            try {
                if (current != null) {
                    return current;
                }
                return null;
            } finally {
                current = null;
            }
        }

        public static <T> Iterator<List<T>> iterator(Iterator<T> it, int length) {
            return new PartitionIterator(it, length);
        }

        public static <T> Spliterator<List<T>> spliterator(Iterator<T> it, int length) {
            return Spliterators.spliteratorUnknownSize(new PartitionIterator<T>(it, length), 0);
        }

        public static <T> Stream<List<T>> stream(Iterator<T> it, int length) {
            return StreamSupport.stream(spliterator(it, length), false);
        }

    }

}
