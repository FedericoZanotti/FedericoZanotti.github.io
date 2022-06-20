---
layout: post
title: Machine Learning for detecting Liers
subtitle: ML tecnicques and methods to discover lier in a psycological questionnaire and reconstructing their honest response
thumbnail-img: /assets/img/psico.jpg
gh-repo: FedericoZanotti/CBSD-project
gh-badge: [star, fork, follow]
tags: [CBSD]
comments: true
---

#  Can we fool liers? [<img src="https://logos-world.net/wp-content/uploads/2020/11/GitHub-Logo.png" width=50/>](https://github.com/FedericoZanotti/CBSD-project.git)


**Source Code**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/FedericoZanotti/FEdericoZanotti.github.io/blob/master/project_filesCBSD_Project_IADQ.ipynb)


This was a project for the course Cognitive Behavioral and Social Data. Some databases were given to the students, composed by honest and dishonest response of the IADQ questionnaire, a psyccological test for the Adjustment disorder. The participants were asked to respond first in a dishonest way, exagerrating the adjusment disorder syntoms, with the purpose of deceive the test and gain some economic benefits from the disease. 

**The project has two objectives:** the first one was to recognize if a subject lies and then reconstruct his honest answer. This is very interesting, because there are no way to identify a lier in a psycological test, except for some control questions that psycologists insert in the questionnaires. Expecially nowadays there is no way to reconstruct the possible honest response.

The project was really challenging and to be honest our work did not resolve this problem, but I think we faced in an original way (expecially with the method Brute Force we implemented). The major problem was the data: we had a dataset of 450 answers, 225 honest and 225 dishonest, and it's very difficult to generalize and create a general algorithm. Infact how can we state if a subject lies in a dataset of 225 questionnaire answers? we need more subjects, in order to enrich the diversity of answers given by liers.

We made also a web-app that caracterizes a possible future implementation, in which a psyclogist load the answers of the questionnaire and the algorithm gives the dishonest response and their honest reconstruction.

Here I provide a **Little Demo**:  [![CBSD-project](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/federicozanotti/cbsd-project/main/app.py) and a <a id="raw-url" href="https://raw.githubusercontent.com/FedericoZanotti/FedericoZanotti.github.io/master/_posts/test.csv">Test File</a>

Here i reported the final results (discussed deeply in the colab notebook).

### **Classification** 


<img src="/assets/img/path.jpg" />


### **Reconstruction**

<img width=600 src="https://github.com/FedericoZanotti/FedericoZanotti.github.io/blob/master/_posts/recon.PNG" />
