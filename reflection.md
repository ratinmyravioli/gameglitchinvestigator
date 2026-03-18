# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

  After getting the streamlit app to run, I noticed that the number of attempts for the easy, normal, and hard modes were inconsistent. For instance, "Easy" mode gave 5 attempts while "Normal" mode gave 7 attempts, something that would be expected to be swapped. The number ranges were also logically inconsistent, as "Normal" mode gave a range of 1 to 100 while "Hard" was 1 to 50. When playing the game, I started in Normal difficulty (with a range of 1-100) and guessed 3. The hint provided told me to go lower, so I tried 2, and then 1, yet the hint was still to go lower. I also noticed that the debug history wasn't updating correctly, as it would "lag behind" and be updated only for the previous guess. After guessing the correct number, when I tried to make a new game, the game completely stopped working, not clearing the debug information.
---

## 2. How did you use AI as a teammate?

    I solely used GitHub Copilot as a teammate for this project. One example of an incorrect AI suggestion was when I needed to update the check_guess() function and move it to logic_utils.py. When the model responded, it did far more than I needed it too, moving all the other functions into the logic_utils.py file, as well as changed the if new_game: lines. As it changed so much at once, I rejected the changes and clarified my prompt to make the changes more contained, since I was afraid too much would mean more errors. Another example of a correct AI suggestion was the fixing of the displayed range of possible answers based on difficulty. After the AI suggested a good way to alter the actual value, I was unsure of how to fix what the app displayed. Copilot suggested to change the sidebar caption to not include a fixed range within the string, but rather to use a fstring to include the actual variable names within the string.

---

## 3. Debugging and testing your fixes

To decide whether a bug was really fixed, I altered between creating pytests and manual testing, depending on whether the issue would require a lot of testing for specific inputs or the issue would require a visual glance. One test I ran was for the proper hints while guessing, which I used pytest for. In the test_game_logic.py file, I created a few pytest functions to test for specific scenarios, such as when the guess was too low, too high, or on point. The passing of these tests allowed me to verify that the fixes the AI suggested were proper, aside from manual testing. Likewise, AI helped me design these tests as I had never used pytest before. By using AI to generate and successfully run these, I was able to better understand how to structure pytest functions and use assert statements.

---

## 4. What did you learn about Streamlit and state?

The secret number kept changing in the original app because the original code had a checking block that would conditionally convert the secret number into a string rather than an integer, making comparisons sometimes off.

The rerun function in Streamlit causes the script to pause from where it currently is and rescan the whole code, meaning it can rerun or run new functionality and make the app more dynamic. It is essentially a refresh for the code so that it can update the app display and backend when functionality is used. Session state is a way to preserve variables between reruns, so that the program can continue to behave smart and keep track of things even when the script is run through again.

To make the game have a stable secret number, it was important to stop the program from setting secret number's state variable to a hardcoded number.


---

## 5. Looking ahead: your developer habits

One strategy I'd love to reuse in future projects in pytest! I'm someone who loves to make sure any test case, including edge cases, are addressed in programs. So, when I make any changes, I find I redo these tedious cases every time. To minimize these actions, I'll use pytests in the future to make super easy.

One thing I would do differently next time I work with AI is to really be specific with what "permissions" I give the chatbot. I found that when I wasn't super specific, it would make additional changes I didn't want at the time or forget to do something else related to the task at hand that I thought I implied, but the program didn't quite understand. 

This project made me realize AI generated code can be super handy, but it needs to be rigorously analyzed and/or tested to make sure unwanted changes don't occur.
