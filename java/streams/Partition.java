#!/usr/bin/env java --source 11
// KEYS=[java streams partition sequence partition-all]

import com.google.common.collect.Iterables;

import java.util.Arrays;
import java.util.List;
import java.util.stream.StreamSupport;

public class Partition {
    public static void main(String arg[]) {
        Iterable<List<Integer>> lists = Iterables.partition(Arrays.asList(1, 2, 3, 4, 5, 6, 7), 3);

        StreamSupport.stream(lists.spliterator(), false)
                .forEach(System.out::println);
    }
}