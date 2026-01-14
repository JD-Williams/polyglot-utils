package dev.jdwilliams.utils.strings;


public final class StringUtils {

    private StringUtils() {
        // Prevent instantiation
    }

    /**
     * Returns true if the string is null, empty, or contains only whitespace.
     */
    public static boolean isBlank(String value) {
        return value == null || value.trim().isEmpty();
    }

    /**
     * Normalizes whitespace by trimming and collapsing consecutive
     * whitespace characters into a single space.
     */
    public static String normalizeWhitespace(String value) {
        if (value == null) {
            return null;
        }
        return value.trim().replaceAll("\\s+", " ");
    }

    /**
     * Truncates a string to the specified max length.
     * If truncated, appends the supplied suffix.
     */
    public static String truncate(String value, int maxLength, String suffix) {
        if (value == null) {
            return null;
        }
        if (maxLength < 0) {
            throw new IllegalArgumentException("maxLength must be non-negative");
        }
        if (value.length() <= maxLength) {
            return value;
        }
        return value.substring(0, maxLength) + (suffix == null ? "" : suffix);
    }

    /**
     * Safely compares two strings for equality.
     */
    public static boolean equals(String a, String b) {
        if (a == null && b == null) {
            return true;
        }
        if (a == null || b == null) {
            return false;
        }
        return a.equals(b);
    }

    /**
     * Capitalizes the first character of the string.
     */
    public static String capitalize(String value) {
        if (isBlank(value)) {
            return value;
        }
        return Character.toUpperCase(value.charAt(0)) + value.substring(1);
    }


}
