---
layout: post
title: Machine Learning for detecting Liers
subtitle: ML tecnicques and methods to discover lier in a psycological questionnaire and reconstructing their honest response
gh-repo: FedericoZanotti/CBSD-project
gh-badge: [star, fork, follow]
tags: [test]
comments: true
---

#  Project with failure and success

**Source Code**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/FedericoZanotti/FEdericoZanotti.github.io/blob/master/project_filesCBSD_Project_IADQ.ipynb)


This was a project for the course Cognitive Behavioral and Social Data. Some databases were given to the students, composed by honest and dishonest response of the IADQ questionnaire, a psyccological test for the Adjustment disorder. The participants were asked to respond first in a dishonest way, exagerrating the adjusment disorder syntoms, with the purpose of deceive the test and gain some economic benefits from the disease. 

**The project has two objectives:** the first one was to recognize if a subject lies and then reconstruct his honest answer. This is very interesting, because there are no way to identify a lier in a psycological test, except for some control questions that psycologists insert in the questionnaires. Expecially nowadays there is no way to reconstruct the possible honest response.

The project was really challenging and to be honest our work did not resolve this problem, but I think we faced in an original way (expecially with the method Brute Force we implemented). The major problem was the data: we had a dataset of 450 answers, 225 honest and 225 dishonest, and it's very difficult to generalize and create a general algorithm. Infact how can we state if a subject lies in a dataset of 225 questionnaire answers? we need more subjects, in order to enrich the diversity of answers given by liers.

We made also a web-app that caracterizes a possible future implementation, in which a psyclogist load the answers of the questionnaire and the algorithm gives the dishonest response and their honest reconstruction.

<a id="raw-url" href="https://raw.githubusercontent.com/FedericoZanotti/FedericoZanotti.github.io/master/_posts/test.csv">Download FILE</a>
[Download Minion](https://octodex.github.com/images/minion.png "download")
**Little Demo**:  [![CBSD-project](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/federicozanotti/cbsd-project/main/app.py)



**Here is some bold text**

## Here is a secondary heading

Here's a useless table:

| Number | Next number | Previous number |
| :------ |:--- | :--- |
| Five | Six | Four |
| Ten | Eleven | Nine |
| Seven | Eight | Six |
| Two | Three | One |


How about a yummy crepe?

![Crepe](https://s3-media3.fl.yelpcdn.com/bphoto/cQ1Yoa75m2yUFFbY2xwuqw/348s.jpg)

It can also be centered!

![Crepe](https://s3-media3.fl.yelpcdn.com/bphoto/cQ1Yoa75m2yUFFbY2xwuqw/348s.jpg){: .mx-auto.d-block :}

Here's a code chunk:

~~~
var foo = function(x) {
  return(x + 5);
}
foo(3)
~~~

And here is the same code with syntax highlighting:

```javascript
var foo = function(x) {
  return(x + 5);
}
foo(3)
```

And here is the same code yet again but with line numbers:

{% highlight javascript linenos %}
var foo = function(x) {
  return(x + 5);
}
foo(3)
{% endhighlight %}

## Boxes
You can add notification, warning and error boxes like this:

### Notification

{: .box-note}
**Note:** This is a notification box.

### Warning

{: .box-warning}
**Warning:** This is a warning box.

### Error

{: .box-error}
**Error:** This is an error box.