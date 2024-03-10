# Advanced Python Calculator for Software Engineering Graduate Course

## Project Overview

This midterm requires the development of an advanced Python-based calculator application. Designed to underscore the importance of professional software development practices, the application integrates clean, maintainable code, the application of design patterns, comprehensive logging, dynamic configuration via environment variables, sophisticated data handling with Pandas, and a command-line interface (REPL) for real-time user interaction.
## Instructor Video - [here](https://youtu.be/hu9YFdeSkV8)

## Project Submission

- Create a NEW repository from scratch and transfer any relevant work as you complete the assignment, **you need to show a clear history of work through your commits, or your project could be given as low as a 0 for not showing your work.**
- Submit through a GitHub repository link containing the necessary documentation, configuration examples, and a coherent commit history.
- You are required to write a short description and link to your implememtation of the design patterns you use.
- You need to provide a description of how you used environment variables and link to your code to illustrate.
-  You need to explain and link to how you are using logging.
-  You need to link to and explain how you are using try/catch / exceptions to illustrate  "Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP)/
- Create a 3-5 minute video demonstration of using the calculator, highlighting its key features and functionalities. Link the video to the repository readme.
-  Submit a link to your repository to Canvas.  
-  Keep your repository private while working on it, so people don't copy your work.  Make the repository public within a day of the project being due, so we can grade it.
- **REQUIRED - YOU MUST USE GITHUB ACTIONS AND YOUR CODE MUST PASS ALL THE TESTS ON GITHUB**

## Core Functionalities

### Command-Line Interface (REPL)

Implement a Read-Eval-Print Loop (REPL) to facilitate direct interaction with the calculator. This interface should support:
- Execution of arithmetic operations (Add, Subtract, Multiply, and Divide)
- Management of calculation history.
- Access to extended functionalities through dynamically loaded plugins.

### Plugin System

Create a flexible plugin system to allow seamless integration of new commands or features. This system should:
- Dynamically load and integrate plugins without modifying the core application code.
- Include a REPL  "Menu" command to list all available plugin commands, ensuring user discoverability and interaction.

### Calculation History Management with Pandas

Utilize Pandas to manage a robust calculation history, enabling users to:
- Load, save, clear, and delete history records through the REPL interface.


### Professional Logging Practices

Establish a comprehensive logging system to record:
- Detailed application operations, data manipulations, errors, and informational messages.
- Differentiate log messages by severity (INFO, WARNING, ERROR) for effective monitoring.
- Dynamic logging configuration through environment variables for levels and output destinations.

### Advanced Data Handling with Pandas

Employ Pandas for:
- Efficient data reading and writing to CSV files.
- Managing calculation history.

### Design Patterns for Scalable Architecture

Incorporate key design patterns to address software design challenges, including:
- **Facade Pattern:** Offer a simplified interface for complex Pandas data manipulations.
- **Command Pattern:** Structure commands within the REPL for effective calculation and history management.
- **Factory Method, Singleton, and Strategy Patterns:** Further enhance the application's code structure, flexibility, and scalability.

## Development, Testing, and Documentation Requirements

### Testing and Code Quality

- Achieve a minimum of 90% test coverage with Pytest.
- Ensure code quality and adherence to PEP 8 standards, verified by Pylint.

### Version Control Best Practices

- Utilize logical commits that clearly group feature development and corresponding tests, evidencing clear development progression.

### Comprehensive Documentation

- Compile detailed documentation in `README.md`, covering setup instructions, usage examples, and an in-depth analysis of architectural decisions, particularly emphasizing the implementation and impact of chosen design patterns and the logging strategy.


## Evaluation Criteria

### Total Points: 100

#### Functionality (40 Points)

- **Calculator Operations:** 20 points for implementing basic and statistical operations.
- **History Management:** 10 points for effective management using Pandas.
- **Configuration via Environment Variables:** 5 points for flexible application configuration.
- **REPL Interface:** 5 points for a user-friendly command-line interface.

#### Design Patterns (20 Points)

- **Implementation and Application:** 10 points for the effective use of design patterns.
- **Documentation and Explanation:** 10 points for thorough documentation of design pattern rationale and implementation.

#### Testing and Code Quality (20 Points)

- **Comprehensive Testing with Pytest:** 10 points for extensive test coverage.
- **Code Quality and Adherence to Standards:** 10 points for clean, maintainable code.

#### Version Control, Documentation, and Logging (20 Points)

- **Commit History:** 10 points for logical and informative commit messages.
- **README Documentation:** 5 points for comprehensive setup and usage instructions.
- **Logging Practices:** 5 points for implementing adaptable and informative logging.

