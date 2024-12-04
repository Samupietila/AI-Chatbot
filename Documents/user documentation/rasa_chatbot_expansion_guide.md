
# Expanding the Rasa Chatbot

## Project: Casino Chatbot
**Languages Supported:** Finnish, English, Arabic  
**Rasa Version:** 3.1

This guide explains how to expand the Rasa-based casino chatbot by adding new languages, features, and interactivity.


---

## Expanding Language Support

### Process Overview
Adding support for a new language involves three main steps:

1. Add new user intents (sample phrases) in the desired language.
2. Translate and add bot responses in the new language.
3. Test to ensure correct functionality.

# Example: Adding Spanish

To add Spanish support, you'll need to define new intents and update responses in both the `nlu_es.yml` and `domain.yml` files.

## New Intents (nlu_es.yml)

```yml
- intent: greet
  examples: |
    - hola
    - buenos días
    - qué tal
```
## Updated Responses (domain.yml)
```yml
responses:
  utter_greet:
    - condition:
        - type: slot
          name: language
          value: "en"
      text: "Hello!"  # English
    - condition:
        - type: slot
          name: language
          value: "fi"
      text: "Hei!"  # Finnish
    - condition:
        - type: slot
          name: language
          value: "ar"
      text: "مرحباً!"  # Arabic
    - condition:
        - type: slot
          name: language
          value: "es"
      text: "¡Hola!"  # Spanish

```




## Visual Example of Multilingual Bot Functionality

<table border="1" style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="padding: 10px; text-align: left;">Language</th>
    <th style="padding: 10px; text-align: left;">User Message</th>
    <th style="padding: 10px; text-align: left;">Bot Response</th>
  </tr>
  <tr>
    <td style="padding: 10px; text-align: left;">English</td>
    <td style="padding: 10px; text-align: left;">Hello!</td>
    <td style="padding: 10px; text-align: left;">Hello!</td>
  </tr>
  <tr>
    <td style="padding: 10px; text-align: left;">Finnish</td>
    <td style="padding: 10px; text-align: left;">Hei!</td>
    <td style="padding: 10px; text-align: left;">Hei!</td>
  </tr>
  <tr>
    <td style="padding: 10px; text-align: left;">Arabic</td>
    <td style="padding: 10px; text-align: left;">مرحباً!</td>
    <td style="padding: 10px; text-align: left;">مرحباً!</td>
  </tr>
  <tr>
    <td style="padding: 10px; text-align: left;">Spanish</td>
    <td style="padding: 10px; text-align: left;">Hola!</td>
    <td style="padding: 10px; text-align: left;">¡Hola!</td>
  </tr>
</table>

# Adding New Features

New features might include supporting new games, checking bonus status, or providing game rules.

## Example: Bonus Status Check

### Sample Intent and Response:

| **Intent**                | **User Message Example**            | **Bot Response**                                   |
|---------------------------|-------------------------------------|---------------------------------------------------|
| `bonus_status`             | "What’s the status of my bonus?"    | "Your bonus is currently active."                 |
| `bonus_wagering_requirements` | "What are the wagering requirements?" | "You need to wager the bonus 10x before withdrawal." |


# Enhancing Visual Interactivity

Adding interactive buttons can improve the user experience.

# Example: Game Selection Using Buttons

When a user asks about game rules, the bot can present selectable options in button form.

| **Button**  | **Payload**              |
|-------------|--------------------------|
| Blackjack   | `/ask_blackjack_rules`    |
| Poker       | `/ask_poker_rules`        |
| Roulette    | `/ask_roulette_rules`     |
 


**Chatbot:**  
"Select the game you want to know more about:"

[ Blackjack ]   [ Poker ]   [ Roulette ]

---

# Analytics and Optimized Functionality

Analytics help track the most common user questions, allowing for targeted chatbot improvements.

# Example Analytics Table


| **Question**                          | **Frequency (per week)** |
|---------------------------------------|--------------------------|
| "How do you play blackjack?"         | 50                       |
| "What’s the status of my bonus?"     | 30                       |
| "What are the odds in roulette?"     | 20                       |

---

# Future Expansion Opportunities


| **Feature**                     | **Benefits**                                                |
|----------------------------------|-------------------------------------------------------------|
| Real-time Customer Support      | Complex queries can be forwarded to a human agent.          |
| Voice Interaction               | The bot can accept voice commands and respond audibly.       |
| Social Media Integration        | Expands usage to platforms like Facebook Messenger or WhatsApp. |
| Personalization                 | The bot tailors responses based on user history or profile. |


# Importance of Documentation and Testing

## Documentation
Ensure that files like ``nlu.yml``, ``domain.yml``, and ``stories.yml``are update
d with every change. Proper documentation is crucial for future developers.

# Training the Chatbot for New Features and Languages

Once you’ve added new languages, intents, responses, or features, it’s important to retrain the chatbot to ensure the changes are properly integrated. Follow these key steps to make sure your bot works as expected:

## 1. Train the Model

```
rasa train
```

### Testing

Test your chatbot using ```rasa shell ```for quick checks or automated testing pipelines to ensure smooth functionality.
```
rasa shell
```

# Conclusion

This documentation provides an easy-to-follow guide for expanding the Rasa chatbot. By adding new languages and features, and improving interactivity, developers can significantly enhance the chatbot experience for users.
