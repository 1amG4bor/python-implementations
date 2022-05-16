import org.python.core.PyInteger;
import org.python.util.PythonInterpreter;
import org.python.core.PyObject;

import java.io.IOException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        System.out.println("Java app has started...");
        try(PythonInterpreter interpreter = new PythonInterpreter()) {
            // 1) Simple print
            interpreter.exec("print 25 * '*'");
            interpreter.exec("print 'Yaaay, Hello from Python!'");
            waitForContinue("Get calculated value from python");

            // 2) Get calculated value from python
            interpreter.exec("squares = [x ** 2 for x in range(6)]");
            PyObject PyList = interpreter.get("squares");
            System.out.println("\nPython list: " + PyList.toString());
            waitForContinue("Send and receive data from python");

            // 3) Send and receive data from python
            System.out.println("\nCalculating factorial!");
            int num = getInput();
            interpreter.execfile("src/main/java/pythonScript/factorial.py");
            interpreter.set("num", new PyInteger(num));
            interpreter.exec("result = factorial(num)");
            System.out.println("Result is: " + interpreter.get("result"));
            interpreter.exec("print 'DOCUMENTATION:', factorial.__doc__");

            System.out.println("\nVersion2.0:");
            interpreter.exec("result = factorial_v2(num)");
            System.out.println("Result with v2 is: " + interpreter.get("result"));
            interpreter.exec("print 'DOCUMENTATION:', factorial_v2.__doc__");

            // 4) Receive python exception in java code
            System.out.println("\nGenerating exception...");
            waitForContinue("Are you ready for an exception?");
            interpreter.exec("import dummy");
        }

        System.out.println("\nDone!");
    }

    private static int getInput() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number to calculate: ");
        return scanner.nextInt();
    }

    private static void waitForContinue(String msg) {
        msg = msg.isEmpty() ? "" : String.format("( Section: '%s')", msg);
        System.out.print("Press enter to continue... " + msg);
        try {
            System.in.read();
        } catch (IOException ignored) {}
    }
}
