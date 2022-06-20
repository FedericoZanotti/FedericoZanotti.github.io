---
layout: post
title: Machine Learning for detecting Liers
subtitle: ML tecnicques and methods to discover lier in a psycological questionnaire and reconstructing their honest response
gh-repo: FedericoZanotti/CBSD-project
gh-badge: [star, fork, follow]
tags: [test]
comments: true
---

#  Can we fool liers? [<img src="[logo_github.png](https://www.google.com/search?q=github+logo&rlz=1C1GCEA_enSM987SM987&sxsrf=ALiCzsYf7vkaq5szsCtqBsUOiIF6XHq56g:1655721099441&tbm=isch&source=iu&ictx=1&vet=1&fir=Kq4l3mSBVj08zM%252CH8p6HHzcTglWAM%252C_%253BLp2OqU7fPdjSMM%252CkHlC0fHCgyWhTM%252C_%253B8AE_J5pAtu3iiM%252CTXCcjLeV5gKBaM%252C_%253BF4N7nNsmAvS0zM%252CTXCcjLeV5gKBaM%252C_%253BG9U2Dai9GVGdNM%252CJY-eVDG-JQ2uaM%252C_%253B_OjrNiGLxhfxQM%252C6c2yz7gdNvDU7M%252C_%253BfLKD7QptF_vjyM%252CH8p6HHzcTglWAM%252C_%253BkA2-FqAeptEp1M%252CaZMTzBMUx1GvGM%252C_%253BdO1l3HgJbssG8M%252CgwkaSaXL7ezQZM%252C_%253BIeefiN93NoNWmM%252CzAWdjHONKkQJQM%252C_%253BB9I6N7fsJkqtQM%252CVduUm5bUIj50qM%252C_%253BJdCuiEb92j8WmM%252ChOKru3WHzG-XsM%252C_%253B48_LdUHs4o-K2M%252Cz2e7RYj-WGKlvM%252C_%253BYj_--20JGCXo6M%252CmAJcICWgW1273M%252C_&usg=AI4_-kQcI53jk8eIc4xiPab9cSAHoVmoTQ&sa=X&ved=2ahUKEwiQs-rf6bv4AhWPzaQKHUD4DQsQ9QF6BAgqEAE&biw=1920&bih=918#imgrc=8AE_J5pAtu3iiM)" width=50/>](https://github.com/FedericoZanotti/CBSD-project.git)


**Source Code**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/FedericoZanotti/FEdericoZanotti.github.io/blob/master/project_filesCBSD_Project_IADQ.ipynb)


This was a project for the course Cognitive Behavioral and Social Data. Some databases were given to the students, composed by honest and dishonest response of the IADQ questionnaire, a psyccological test for the Adjustment disorder. The participants were asked to respond first in a dishonest way, exagerrating the adjusment disorder syntoms, with the purpose of deceive the test and gain some economic benefits from the disease. 

**The project has two objectives:** the first one was to recognize if a subject lies and then reconstruct his honest answer. This is very interesting, because there are no way to identify a lier in a psycological test, except for some control questions that psycologists insert in the questionnaires. Expecially nowadays there is no way to reconstruct the possible honest response.

The project was really challenging and to be honest our work did not resolve this problem, but I think we faced in an original way (expecially with the method Brute Force we implemented). The major problem was the data: we had a dataset of 450 answers, 225 honest and 225 dishonest, and it's very difficult to generalize and create a general algorithm. Infact how can we state if a subject lies in a dataset of 225 questionnaire answers? we need more subjects, in order to enrich the diversity of answers given by liers.

We made also a web-app that caracterizes a possible future implementation, in which a psyclogist load the answers of the questionnaire and the algorithm gives the dishonest response and their honest reconstruction.

Here I provide a **Little Demo**:  [![CBSD-project](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/federicozanotti/cbsd-project/main/app.py) and a <a id="raw-url" href="https://raw.githubusercontent.com/FedericoZanotti/FedericoZanotti.github.io/master/_posts/test.csv">Test File</a>

Here i reported the final results (discussed deeply in the colab notebook).

**Classification**
| Method  | Train Score (%)| Test Score (%)|
| ------------- | ------------- |------------|
| Logistic Regression  |86   | 89  |
| Decision Tree  | 84   | 81  |
| Random Forest  | 98 | 87  |
| KNN | 89  | 87  |
| AdaBoost | 93  | 90  |

**Reconstruction**
| Method  | Reconstruction Accuracy (%) | Mean Squared Error (MSE) |
| ------------- | ------------- |------------|
| DAE | 34 | 1.0966 |
| DBN | 34.7 | 1.0731 |
| RNN  |  34.7 | 1.0832 |
| LSTM | 34.2  | 1.0960 |
| BruteForce | 45 | 1.0087 |
| One Class SVM (withBruteForce) | 59.6 | 0.75 |
