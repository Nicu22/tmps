package domain.patterns.bridge;

/**
 * Concrete implementation of the PrintTechnique interface, simulating lithographic printing.
 * This class represents one of the concrete implementations of the PrintTechnique interface.
 */
public class Lithography implements PrintTechnique {
    /**
     * Simulates printing the given content using lithographic printing technique.
     * 
     * @param content Content to be printed.
     */
    @Override
    public void print(String content) {
        System.out.println("Printing using Lithography: " + content);
    }
}