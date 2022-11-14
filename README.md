# Styra

Styra is an AI powered chrome extension which detects when users get distracted, and prompts them to stay productive. Uses ML (using Python & Keras) on browser history and webcam feed.

## 🎉 What it does

Styra helps you smartly and drastically increase your personal productivity for surfing over the internet while taking care of your health and well-being. Styra acts as your personal companion by keeping constant checks over your emotions and learning your current interests as you browse.

When a user is distracted it politely reminds the user that he/she is getting distracted. It suggests user remedies like “take a break” or “have a cup of coffee” etc, based on the user's emotion.

Users are also given the choice to analyze his/her mood and number of distractions over time in order to retrospect their productivity and health.

## 👀 Demo

You can checkout Styra in action in the [![this video](https://i.imgur.com/xJ5CmTa.png)](https://www.youtube.com/watch?v=YxxHXsnLhS4)

## 🚀 Inspiration

On the modern-day internet, one can easily and unconsciously drift away to topics unrelated to their current work, hence leading to procrastination, killing productivity and time.

The current scenario of COVID-19 has forced people to work from home. A lot of people are working remotely from home on their computers. Constant exposure to screen time negatively impacts our mental health and well-being.

Keeping these issues in mind, we have built a chrome extension called “Styra”, Swedish for “steer”, which enhances user productivity and supplements their health and well-being.

## ⚙️ How we built it

We used YAKE(a derivation from the RAKE keyword extraction algorithm) keyword extractor to analyze the keyword embeddings of the user's browsing activity. These embeddings are then passed through a self-devised algorithm that finds similarities/dissimilarities between sets of web pages/documents and reports a context change. The user is then politely reminded of these changes, in case the context change was intended by the user, he/she can seamlessly inform by choosing an option in the prompt.

Microsoft Azure’s face cognitive services API is used to get the user’s current emotions. Now to get various derived emotions like “tired”, “non-vigilant” & "alert" we built our self-trained Neural Network over various iterations with TensorFlow and Keras achieving accuracies over 70-75%. We also created a dataset using our own images (over 2500+) images in order to accurately train the model.

The backend is managed through Django in order to store/alter user emotions & user browsing analysis with django-rest-framework to form API's in order to communicate with the front-end. We build a services module that contains functionalities including our managing external API calls to Azure and YAKE along with the emotion analysis model and keyword matching algorithms which are utilized by the Django server.

For building a Chrome Extension we used Manifest v3.0 (along with an options page and a Landing Page) We tried our best to build a clean, attractive and responsive UI using vanilla js and CSS and GSAP for animations. Styra’s logo is designed using Illustrator.

## ⌛ Challenges we ran into

- The extension manifest v3.0 only has limited support
- The initial extraction & DL models we built were not accurate enough. Effort had to be spent creating effective models.
- Implementing all the envisioned features required thoughtful time management
- Model tuning and forming an accurate dataset for our complex emotion derivation model

## 🎆 Accomplishments that we're proud of

- We were able to maintain a dynamic and synergetic environment with working functionalities over the user's emotion and distractions.
- We implemented our ML model with our own dataset to enable several features
- We finished it in time!!
- We have used vanilla javascript to make the extension lightweight.
- We have built a very comforting, attractive, and clean UI with minimal design.

## 📚 What we learned

- Firstly we learned some new NLP techniques, methods, and representations like doc2vec, Latent Dirichlet allocation algorithm, and BOW, we also learned some new ways in computer vision to analyze facial emotions
- Learned the importance of hyperparameter tuning for getting accurate results for our custom model
- We became proficient in using the new manifest v3.0 methods and API to build chrome extensions
- New ways we can communicate with the underlying chrome engine
- We were fairly impressed with Django’s capabilities to easily manage databases, APIs, and form endpoints to communicate with our front-end

## 🔍 Research References

- [https://onlinelibrary.wiley.com/doi/full/10.1002/hbe2.229][https://onlinelibrary.wiley.com/doi/full/10.1002/hbe2.229]
- [https://www.ijo.in/article.asp?issn=0301-4738;year=2020;volume=68;issue=11;spage=2378;epage=2383;aulast=Bahkir][https://www.ijo.in/article.asp?issn=0301-4738;year=2020;volume=68;issue=11;spage=2378;epage=2383;aulast=bahkir]
