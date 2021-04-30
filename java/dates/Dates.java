#!/usr/bin/env java --source 11
// KEYS=[java time date parse parsing timestamp instant iso]

import java.time.Instant;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;

public class Dates {

    public static String format(Instant timestamp) {
        return DateTimeFormatter.ISO_INSTANT.format(timestamp.truncatedTo(ChronoUnit.MILLIS));
    }

    public static Instant parse(String timestamp) {
        return Instant.from(DateTimeFormatter.ISO_INSTANT.parse(timestamp));
    }

}