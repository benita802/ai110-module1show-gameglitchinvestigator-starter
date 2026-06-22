# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

In difficulty level: normal i guessed 100 which was the limit but the hint told me to go higher. 
In difficulty level: easy i guessed 20 which was the limit but the hint told me to go higher. 
In difficulty level: hard i guessed 50 which was the limit but the hint told me to go higher. 
The when the attempts were done and i was asked to start a new game, when i clicked the button to start a new game, it did not refresh and gave an error message.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  Hints were backwards and the ranges for the different levels were backwards too. When i clicked new game, the game did not refresh to start a new game. 


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 20    | "go lower"(easy)  | Hint"go higher" | none
| 100   | "go lower"(hard)  | Hint"go higher" | none
| New game | start a new game | didn't start new game | "Game over. Start a new game to try again."

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). 
Swapping the "go higher" and "go lower"
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
When i run the game and it gave the right hint
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I run the game and made guesses and when it showed the result, the answer was higher than my guesses meaning the hints were right.
- Did AI help you design or understand any tests? How?
It showed me which lines needed swapping to fix the hints error and the ranges.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
Going step by step to fix the bugs
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
Ask it if it can identify any errors i might have missed. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
AI generated code is nice and does take long to be generated but sometimes it is not always right,but an AI agent can also be helpful in finding bugs you missed.
