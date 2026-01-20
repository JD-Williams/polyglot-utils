package dev.jdwilliams.utils.math;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class MathUtilsTest {

    @Test
    void testGcd() {
        assertEquals(6, MathUtils.gcd(54, 24));
        assertEquals(1, MathUtils.gcd(17, 13));
        assertEquals(5, MathUtils.gcd(-15, 10));
    }

    @Test
    void testLcm() {
        assertEquals(216, MathUtils.lcm(54, 24));
        assertEquals(221, MathUtils.lcm(17, 13));
        assertEquals(30, MathUtils.lcm(-15, 10));
        assertEquals(0, MathUtils.lcm(0, 10));
    }

    @Test
    void testIsPrime() {
        assertTrue(MathUtils.isPrime(2));
        assertTrue(MathUtils.isPrime(13));
        assertFalse(MathUtils.isPrime(1));
        assertFalse(MathUtils.isPrime(4));
        assertFalse(MathUtils.isPrime(-7));
    }

    @Test
    void testFactorial() {
        assertEquals(120, MathUtils.factorial(5));
        assertEquals(1, MathUtils.factorial(0));
        assertThrows(IllegalArgumentException.class,
                () -> MathUtils.factorial(-3));
    }
}
