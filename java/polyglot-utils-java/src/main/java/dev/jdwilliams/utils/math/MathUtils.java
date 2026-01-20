package dev.jdwilliams.utils.math;

public final class MathUtils {

    private MathUtils() {
        // Prevent instantiation
    }

    /**
     *  Returns the greatest common divisor (GCD) of two integers using the
     *  Euclidean algorithm.
     */
    public static int gcd(int a, int b) {
        a = Math.abs(a);
        b = Math.abs(b);
        int max = Math.max(a, b);
        int min = Math.min(a, b);
        while (min != 0) {
            int temp = min;
            min = max % min;
            max = temp;
        }
        return max;
    }

    /**
     *  Returns the least common multiple (LCM) of two integers.
     */
    public static int lcm(int a, int b) {
        if (a == 0 || b == 0) {
            return 0;
        }
        return Math.abs(a * b) / gcd(a, b);
    }

    /**
     *  Returns true if a number is prime .
     */
    public static boolean isPrime(int n) {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 == 0 || n % 3 == 0) return false;
        for (int i = 5; i * i <= n; i+=6) {
            if (n % i == 0 || n % (i + 2) == 0) return false;
        }
        return true;
    }

    /**
     *  Returns the factorial of a non-negative integer.
     */
    public static long factorial(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("n must be non-negative");
        }
        long result = 1;
        for (int i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }
}
