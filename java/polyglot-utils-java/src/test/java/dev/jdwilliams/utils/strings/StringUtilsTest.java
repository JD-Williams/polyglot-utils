package dev.jdwilliams.utils.strings;


import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class StringUtilsTest {

    @Test
    void isBlank_handlesNullAndWhitespace() {
        assertTrue(StringUtils.isBlank(null));
        assertTrue(StringUtils.isBlank(""));
        assertTrue(StringUtils.isBlank("   "));
        assertFalse(StringUtils.isBlank("text"));
    }

    @Test
    void normalizeWhitespace_collapsesSpaces() {
        assertEquals("hello world",
                StringUtils.normalizeWhitespace("  hello   world  "));
    }

    @Test
    void truncate_behavesCorrectly() {
        assertEquals("hello",
                StringUtils.truncate("hello", 10, "..."));

        assertEquals("hel...",
                StringUtils.truncate("hello world", 3, "..."));
    }

    @Test
    void truncate_throwsForNegativeLength() {
        assertThrows(IllegalArgumentException.class,
                () -> StringUtils.truncate("test", -1, "..."));
    }

    @Test
    void equals_handlesNullsSafely() {
        assertTrue(StringUtils.equals(null, null));
        assertFalse(StringUtils.equals(null, "a"));
        assertTrue(StringUtils.equals("a", "a"));
    }

    @Test
    void capitalize_behavesCorrectly() {
        assertEquals("Hello", StringUtils.capitalize("hello"));
        assertEquals("Hello", StringUtils.capitalize("Hello"));
        assertNull(StringUtils.capitalize(null));
    }


}
