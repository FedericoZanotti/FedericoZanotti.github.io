---
layout: post
title: Numbermind with SAT Encoding
subtitle: Game implementation using logical library Z3 of Python
thumbnail-img: /assets/img/dataset.png
tags: [Python, Logic, SAT Encoding]
comments: true
---

# Numbermind

**Source Code**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1lQVPdr7lQY1rew3nhn6ltAq6WV-nrwVF#scrollTo=X4l3oShq3fL0)

Numbermind is a classic game in which two players challenge themselves and defend their intelligence. A player is the “Guardian” of a secret code composed by 5 positions and 9 possible digits to insert in every positions. The other player has to guess the code for a limited number of trials using the feedback the other player gives him: every round the Guardian tell him how many digits in correct position the player guessed. 
The game implementation is done using SAT encoding, the process of transforming a problem into a Satisfiability problem, using basic knowledge of propositional logic.
In my case I had to implement two constraints:
1. In every positions of the sequence there is only one digit
2. Given the feedback of matches, only the number of guess can be true 

The implementation is done in python, using the [Z3 Library](https://ericpony.github.io/z3py-tutorial/guide-examples.htm): a high performance theorem prover developed at Microsoft Research used in many applications such as  software/hardware verification and testing, constraint solving, analysis of hybrid systems, security, biology (in silico analysis), and geometrical problems.
The interesting part in the implementation is that is very flexible in changing the length of the sequence to guess and the number of digits in the sequence. If you are curious just try changing the parameter *NUM_POSITIONS* (length of the sequence) and *NUM_SYMBOLS* (number of digits).











