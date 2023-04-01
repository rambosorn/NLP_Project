# Story Generator using Hugging face
Project Inspired by **Prof.Chaky** and fully support from our TA **Amanda**.
- Prof.github: https://github.com/chaklam-silpasuwanchai/Python-for-NLP

## Environment Setup
1. Install required libraries: Install the necessary Python libraries, including Flask and the Hugging Face Transformers library.
2. Load the language model: Load the pre-trained language model using the Hugging Face Transformers library.
3. Set up Flask app: Create a new Flask app and define routes for the home page and the story generation page.
5. Create HTML templates: Create HTML templates for the home page and the result page.
6. Implement story generation logic: Implement the story generation logic in the Flask app's route function for the story generation page. Use the pre-trained language model to generate a story based on the user's input.
7. Deploy the app: Deploy the Flask app to a web server or run it locally.
#### Input result
<img src="https://github.com/rambosorn/NLP_Project/blob/main/Improved%20Language%20Modeling/Story%20Generator/image/input.png" alt="Alt text"
title="Optional title">
#### Story result
<img src="https://github.com/rambosorn/NLP_Project/blob/main/Improved%20Language%20Modeling/Story%20Generator/image/result.png" title="Optional title">

However, there are also some limitations to this project. Here are some of the limitations:
- API limits: To use the GPT-3 model, you will need to have an API key, which comes with certain usage limits. You may not be able to generate an unlimited number of stories without hitting these limits.
- Quality of generated stories: While GPT-3 is one of the most advanced language models available, it is not perfect. The generated stories may contain errors, inconsistencies, or other issues that make them less than ideal for some use cases.
- Training and computational requirements: While you don't need to train the GPT-3 model yourself, you will need a powerful computer or access to cloud computing resources to generate stories in a reasonable amount of time. Additionally, generating high-quality stories may require many API calls, which can be computationally expensive.


