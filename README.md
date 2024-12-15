# Mastermind Game 2.0

Mastermind is a classic code-breaking game where you have to guess the correct combination of numbers within a limited number of attempts. This Python script allows you to play the game with different difficulty levels: easy, medium, and hard.

**Check out the Website: Deployment coming soon!**

## How to Play

1. Run the `main.py` script in your Python environment.
2. The game will start, and you will be prompted to choose a difficulty level: easy, medium, or hard.
3. You will have 10 attempts to guess the correct number combination based on the chosen difficulty level:
   - Easy: 4 digits
   - Medium: 6 digits
   - Hard: 8 digits
4. After selecting the difficulty level, the game will provide you with instructions on how to play and the number of digits required for that level.
5. You will be prompted to make your guesses. Enter a 4, 6, or 8-digit number (depending on the difficulty level) as your guess. For example, if you're playing on the easy level, enter a 4-digit number like "1234."
6. The game will provide feedback after each guess. You will be told how many correct numbers are in your guess and how many of them are in the correct locations. For example, if you guessed "1234" and three of the numbers are correct but only one is in the correct position, you'll be told that you have "3 correct numbers and 1 correct location."
7. Continue making guesses until you either guess the correct combination or run out of attempts (10 attempts in total).
8. If you guess the correct combination, you win the game! If not, the game will reveal the correct combination.
9. The game ends, and you can choose to play again.

To quit the game, you can use `ctrl + c` at any time.

## Code Design & Considerations
While reattempting this take-home challenge, my primary goal was to focus on code organization and the overall architecture of my program. During the first iteration of my console application, all of my code resided in a single file (main.py), making it challenging to scale or maintain. This time, I focused on encapsulating functionality and ensuring a clear separation of concerns. To achieve this, I implemented an MVC (Model-View-Controller) design pattern, which provided a structured approach to organize my application into distinct layers:

    Model (Data Layer)
        The Model serves as the data layer and incorporates all game-related business logic.
        I created two classes within this layer:
            Game: Manages overall game state and logic.
            Guess: Represents and tracks user guesses.

    Controller (Translation Layer)
        The Controller acts as an intermediary between the Model and the View, ensuring these two layers do not directly interact.
        Its responsibility is to process input, retrieve relevant data from the Model, and determine what the View should display.

    View (Presentation Layer)
        The View retrieves user input and displays output to the user.
        It is responsible for all user-facing interactions, such as displaying instructions, feedback, and game progress.

## Approach and Execution

It took time to conceptualize how best to implement this pattern. Breaking my code into distinct functional components helped me better understand separation of concerns. I focused on ensuring that each component had a clearly defined responsibility:

    Game and Guess classes: Encapsulate related game logic, such as submitting a user guess, checking if the game is over, and managing gameplay state. This also allowed me to refactor many of the original helper functions from main.py into instance methods, aligning functionality more naturally with the objects they represent.
    Controller class: Facilitates communication between the Model and View, ensuring clean interaction and avoiding direct coupling.
    View layer: Focused solely on user interaction, making the user experience independent of underlying game logic.

Through this process, I gained a deeper understanding of how to define the scope and responsibility of each component, resulting in a cleaner and more maintainable codebase.
Testing

To ensure the stability of the application, I also created tests to validate the Minimum Viable Product (MVP) functionality. These tests helped me identify potential edge cases early and confirm that core features, such as submitting guesses and tracking game state, behaved as expected.

## Challenges

One of the major challenges I encountered while refactoring was breaking the application. This taught me to implement small, incremental changes and test often. I also relied heavily on branching to experiment with modifications, ensuring I could keep track of the most stable versions of my application. Regular small commits also helped me manage and troubleshoot changes effectively.

Another challenge involved the random.org API, which often returned "service unavailable" errors. To address this, I implemented error-handling in my API calls to ensure a valid response was received before instantiating a game. This improved the robustness of the application, allowing for more graceful error handling in cases of network issues or API downtime.

## Extensions:
- Customizable levels
- tests
- art

### Future updates
I would like to extend to multi-player or add a timer.
