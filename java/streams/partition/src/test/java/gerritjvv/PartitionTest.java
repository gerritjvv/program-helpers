package gerritjvv;


import org.junit.Test;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static org.junit.Assert.assertEquals;

public class PartitionTest {

    @Test
    public void testPartition() {

        List<Integer> data = Stream.iterate(1, i -> i + 1).limit(45).collect(Collectors.toList());

        Partition.stream(data, 20).forEach(l -> {
            System.out.println("Partition: " + Arrays.toString(l.toArray()));
        });

        List<List<Integer>> partitions = Partition.stream(data, 20).collect(Collectors.toList());

        assertEquals(partitions.size(), 3);

        assertEquals(partitions.get(0), Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20));
        assertEquals(partitions.get(1), Arrays.asList(21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40));
        assertEquals(partitions.get(2), Arrays.asList(41, 42, 43, 44, 45));
    }

    @Test
    public void testPartitionNull() {

        List partitions = Partition.stream(null, 20).collect(Collectors.toList());

        assertEquals(partitions.size(), 0);

    }

    @Test
    public void testPartitionEmpty() {

        List partitions = Partition.stream(Arrays.asList(), 20).collect(Collectors.toList());

        assertEquals(partitions.size(), 0);

    }

    @Test
    public void testPartitionNegativeLength() {

        List partitions = Partition.stream(Arrays.asList(), -1).collect(Collectors.toList());

        assertEquals(partitions.size(), 0);

    }
}
